# InjectMyServerlessEvent

![Logo](https://raw.githubusercontent.com/Voulnet/InjectMyServerlessEvent/master/InjectMyServerlessEvent.png)
A sample AWS Lambda code that contains a Serverless Event Injection vulnerability (OS injection). 

To run this, you need to give it an execution role (doesn't need any particular permision), then create a cloudwatch rule that sends S3 bucket level event PutBucketPolicy to this serverless function.

This should run on Lambda python 3.8. The only thing it needs to run is a configured cloudwatch rule. To make sure your cloudwatch rules trigger correctly, create an empty CloudTrail Trail.

