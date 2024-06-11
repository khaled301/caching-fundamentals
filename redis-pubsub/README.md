# Question:

There are two NodeJs Express applications linked to two different database, for convenience let's call the first application A and the second B, both are linked to the same redis instance with Ioredis.

A can't access directly B database, it needs to do an HTTP request in order to get data from B database.

In an application A endpoint, We need to check a value from application B database, it is a really high traffic endpoint with hundreds of requests per minutes, We can't simply do an http request to get data from application B, the performance loss will be too high.

A solution that We found is redis Pub/Sub, We can register from two channels in application A and B.

If the required value is not present in redis We'll use two channels :

One channel to send messages from application A channel to application B in order to persist objects from database into redis.

A second channel to send messages from application B to application A in order to persist and return the object that was fetch from database.

The question is, is there a way in the application A first channel call to await a return response from application B through the second channel ?