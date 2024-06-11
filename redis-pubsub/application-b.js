// import necessary modules as per your need
const Redis = require('ioredis');
const redisAppB = new Redis();

async function appB(){
    await redisAppB.subscribe("get-company", (err, count) => {
        if (err) console.error(err?.message);
    });

    redisAppB.on("message", async (channel, message) => {
        if (channel == "get-company" && message == "requestDBData"){
        const dbData = await fetchDataFromDatabase();
        
        redisAppB.publish("send-company", dbData, (err) => {
            if (err) console.log(err?.message)
            console.log("response sent to Application A")
        });
        }
    });

    async function fetchDataFromDatabase() {
        // your logic here
    }
}

// call as per your need
appB();