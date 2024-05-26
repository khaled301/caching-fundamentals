"""
Main Worker app
This app listens messages into the redis queue
"""
import random
from json import loads

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
        print("*********WORKER ERROR************")
        print(e)
        print("*********WORKER ERROR************")
        return None
    
    
def redis_queue_push(db, message):
    # push message to tail of the queue (left of the list) incase worker could not process the message
    db.lpush(config.redis_queue_name, message)
    
def redis_queue_pop(db):
    # pop from the head of the queue (right of the list)
    # the `b` in `brpop` indicates this is a blocking call (waits until an message becomes available)
    _, message_json = db.brpop(config.redis_queue_name)
    return message_json

def process_message(db, message_json):
    message = loads(message_json)
    print(f"Message received: id={message['id']} message_number={message['data']['message_number']}")
    
    # mimic potential processing errors
    processed_ok = random.choices((True, False), weights=(5, 1), k=1)[0]
    
    if processed_ok:
        print(f"\tProcessed successfully")
    else:
        print(f"\tProcessing failed - requeuing ...")
        redis_queue_push(db, message_json)


def main():
    """_summary_
        Consumes messages from the redis queue
    """
    
    # connect to Redis
    db = redis_db()
    
    while True:
        # wait until there is a message in the queue
        # here we can potentially loss the message if the worker is not able to process it
        message_json = redis_queue_pop(db)
        
        if message_json:
            # process the message
            process_message(db, message_json)
            
if __name__ == '__main__':
    main()