import kue from "kue";

const push_notification_code = kue.createQueue();
const jobData = {
  phoneNumber: "+254700000000",
  message: "This is a job test message",
};

const job = push_notification_code
  .create("push_notification_code", jobData)
  .save((error) => {
    if (!error) {
      console.log("Notification job created:", job.id);
    }
  });

job
  .on("complete", (result) => {
    console.log("Notification job completed");
  })
  .on("failed", (errorMessage) => {
    console.log("Notification job failed");
  });

