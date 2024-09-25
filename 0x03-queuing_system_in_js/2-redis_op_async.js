import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (error) => {
  console.log("Redis client not connected to the server:", error);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);
const deleteAsync = promisify(client.del).bind(client);

const setNewSchool = async (schoolName, value) => {
  try {
    let setResult = await setAsync(schoolName, value);
    console.log("Reply:", setResult);
  } catch (error) {
    console.log(error);
  }
};

const displaySchoolValue = async (schoolName) => {
  try {
    let getResult = await getAsync(schoolName);
    console.log(getResult);
  } catch (err) {
    console.log(err);
  }
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
