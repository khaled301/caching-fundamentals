"""
This app pushes messages to a redis queue
"""

import random
from datetime import datetime 
from json import dumps
from time import sleep
from uuid import uuid4

import redis

import config

# create connection to redis database/server
def redis_db():
    try:
        db = redis.Redis(
            host=config.redis_host,
            port=config.redis_port,
            db=config.redis_db_number,
            password=config.redis_password,
            decode_responses=True
        )
        
        # make sure the redis is up and running
        db.ping()
        return db
    except Exception as e:
        print(e)
        return None
    
    
def redis_queue_push(db, message):
    # push message to tail of the queue (left of the list)
    db.lpush(config.redis_queue_name, message)
    
def main(num_messages: int, delay: float = 1):
    """_summary_
    Generate random num_messages and push them to the redis queue
    Args:
        num_messages (int): _description_
        delay (float, optional): _description_. Defaults to 1.
    """
    
    # connect to Redis
    db = redis_db()
    
    for i in range(num_messages):
        # Create message data
        message = {
            "id": str(uuid4()),
            "ts": datetime.utcnow().isoformat(),
            "data": {
                "message_number": i,
                "x": random.randrange(1, 100),
                "Y": random.randrange(1, 100),
            }
        }
        
        # We'll store the data as JSON in Redis
        message_json = dumps(message)
        
        # Push message to queue
        print(f"Sending message {i+1} (id={message['id']})") 
        redis_queue_push(db, message_json)
        
        # wait a bit so we have time to start up workers and see how things interact 
        sleep(delay)
        

if __name__ == '__main__':
    main(3000, 0)