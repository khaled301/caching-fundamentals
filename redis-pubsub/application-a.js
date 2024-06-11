// import necessary modules as per your need
const Redis = require('ioredis');
const redisAppA = new Redis();

async function appA(){

    await redisAppA.subscribe("send-company", (err, count) => {
        if (err) console.error(err?.message);
    });

    redisAppA.on("message", async (channel, message) => {
        if (channel === "send-company") {
            console.log(message);

            // handle the received message here

            // unsubscribe if required
            // redisAppA.unsubscribe();
        }
    });

    // Possible solution for the query ["My question is, is there a way in the application A first channel call to await a return response from application B through the second channel ?"]

    async function requestDataFromAppB(){
        return new Promise((resolve, reject) => {
            redisAppA.publish("get-company", "requestDBData", (err) => {
                if (err) return reject(err);

                console.log("request sent to Application B");
            });

            // Temporary subscription to listen and resolve the response
            redisAppA.on("message", (channel, message) => {
                if (channel == "send-company"){
                    resolve(message)
                }
            });
        });
    }

    // call the requestDataFromAppB and get the response
    const response = await requestDataFromAppB();                       
}

// call as per your need
appA()