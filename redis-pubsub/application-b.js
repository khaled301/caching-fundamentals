// import necessary modules as per your need
const Redis = require('ioredis');
const redisAppBSub = new Redis();
const redisAppBPub = new Redis();

async function appB(){
    console.log("Application B is starting...");

    await redisAppBSub.subscribe("get-company", (err, count) => {
        if (err) console.error(err?.message);
    });

    redisAppBSub.on("message", async (channel, message) => {
        if (channel == "get-company" && message == "requestDBData"){
        const dbData = await fetchDataFromDatabase();
        console.log(dbData, ` <<----- dbData`);

        redisAppBPub.publish("send-company", dbData, (err) => {
            if (err) console.log(err?.message)
            console.log("response sent to Application A")
        });
        }
    });

    async function fetchDataFromDatabase() {
        // Your data fetching logic here

        // Simulate fetching data with a delay using a Promise
        return new Promise((resolve) => {
            setTimeout(() => {
                resolve(JSON.stringify({data: "data from database"}));
            }, 5000);
        });
    }
}

// call as per your need
appB().catch(err => console.error(`Application B error: ${err?.message}`));