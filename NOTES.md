## Few Message Queues
1. Redis
    - https://redis.io/glossary/redis-queue/
2. RabbitMQ
3. Elastic MQ
4. SQS
5. Kafka
6. Cassandra

### To avoid performance issue on I/O bound applications we can use ASYNC AWAIT or Multi threading

### sub-processing confined workers in the same host and it is not good for scaling

### Multithreading won't work either as the Python is inherently single threaded.

## We can use Redis Message-Queue to distribute the worker nodes between multiple host computers to avoid the scaling issue
### it will help us to run the workers concurrently based on the message in the Queue

## what is really important here is that the Order of execution must not impact the end result. FIFO can't help here as we can not control the task completion orders of the workers apps. 

## So we have to make sure in the Main App that the workers apps process the data the same way the messages are pushed to the queue

## To solve the message loses issues with Redis (other queue like SQS and all have that), we have to maintain using another queue and redis has documentation about it 
1. 
    - [Pattern: Reliable Queue](https://redis.io/commands/lmove/)
    - https://sonus21.medium.com/introducing-rqueue-redis-queue-d344f5c36e1b