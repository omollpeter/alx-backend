const createPushNotificationsJobs = (jobs, queue) => {
  if (jobs.constructor !== Array) {
    throw new Error("Jobs is not an array");
  }

  jobs.forEach((job) => {
    const notificationJob = queue
      .create("push_notification_code_3", job)
      .save((error) => {
        if (!error) {
          console.log(`Notification job created: ${notificationJob.id}`);
        }
      });

    notificationJob
      .on("complete", (result) => {
        console.log(`Notification job ${notificationJob.id} completed`);
      })
      .on("failed", (errorMessage) => {
        console.log(
          `Notification job ${notificationJob.id} failed: ${errorMessage}`
        );
      })
      .on("progress", (progress) => {
        console.log(
          `Notification job ${notificationJob.id} ${progress}% complete`
        );
      });
  });
};

export default createPushNotificationsJobs;
