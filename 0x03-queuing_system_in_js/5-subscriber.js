import redis from "redis";

const subscriber = redis.createClient({
  host: "localhost",
  port: 6379,
});

subscriber.on("connect", () => {
  console.log("Redis client connected to the server");
});

subscriber.on("error", (error) => {
  console.log("Redis client not connected to the server:", error);
});

subscriber.subscribe("holberton school channel");

subscriber.on("message", (channel, message) => {
  if (message == "KILL_SERVER") {
    subscriber.unsubscribe(channel);
    subscriber.quit();
  }
  console.log(message);
});
