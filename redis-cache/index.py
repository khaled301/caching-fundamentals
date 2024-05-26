import http.server
from http import HTTPStatus
import socketserver

import json
import redis

import mysql_gateway

import config

class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.redis_server = redis.Redis(
            host=config.redis_host,
            port=config.redis_port,
            db=config.redis_db_number,
            password=config.redis_password
        )
        
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        query_string = "select * from products"
        
        resp = {}
        
        if self.redis_server.get(query_string) is None:
            
            obj = mysql_gateway.MysqlGateway()
            
            products = obj.query_mysql(query_string)
            
            if products is not None:
                resp = {
                    "_source": "MySQL Server",
                    "data": products
                }
            
                self.redis_server.setex(query_string, 10, value = json.dumps(products))
                
            else:
                print(f"No products found!")

        else:
            products = json.loads(self.redis_server.get(query_string).decode("utf-8"))
            
            resp = {
                "_source": "Redis Server - Retrieved from Cache",
                "data": products
            }
            
        self.wfile.write(bytes(json.dumps(resp, indent = 2), "utf8"))
            
httpd = socketserver.TCPServer(("", 8080), HttpHandler)
print("The HTTP server is running at port 8080...")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
    print("The HTTP server is stopped...")