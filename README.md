# ServerlessWebForm

Web Application Deployment Guide
This guide provides detailed instructions on how to deploy a web application using AWS services, including AWS Amplify, Lambda, API Gateway, DynamoDB, and IAM. The application is a web form that interacts with AWS services to perform create, read, update, and delete (CRUD) operations.
Prerequisites
Before you start, make sure you have an AWS account. If you do not have one, you can create it at AWS Management Console.
Steps to Deploy the Web Application
Hosting with AWS Amplify
Prepare Your Application:
Ensure your application's files (HTML, CSS, JavaScript) are ready. This includes your index.html file and any associated scripts.
Navigate to AWS Amplify:
Log into the AWS Management Console.
Find and select "Amplify" from the services list.
Create a New App:
In the AWS Amplify Console, click on "Get Started" under "Deliver".
Choose "Host your web app".
Deploy Your App:
Drag and drop your web application files (including index.html, and any JavaScript or CSS files) into the console or connect your code repository if your project is managed using Git.
Once the files are uploaded, Amplify will automatically deploy your application.
After deployment, AWS Amplify provides a URL to access your web application.

Setting Up AWS Lambda Functions
Create Lambda Functions:
Navigate to the AWS Lambda Console within the AWS Management Console.
Click on "Create function" and set up new functions for handling POST, GET, and DELETE operations, using the provided postlambda.py, Getlambda.py, and deletelambda.py.
Assign appropriate roles to these Lambda functions, ensuring they have access to interact with DynamoDB.

Configuring API Gateway
Create a New API:
Go to the API Gateway Console and create a new REST API.
Set up resources and methods (GET, POST, DELETE) corresponding to your Lambda functions.
Ensure that each method is correctly linked to its corresponding Lambda function.
Enable CORS:
For each method, enable CORS to allow your web application to interact with these endpoints.
You can enable CORS by selecting the method, clicking on "Actions", and selecting "Enable CORS".

Creating a DynamoDB Table
Set Up DynamoDB Table:
Go to the DynamoDB Console and create a new table, e.g., form.
Define the primary key as 'id'.

Configuring IAM Role for Lambda
Assign IAM Role:
In the IAM Console, ensure that the execution role assigned to your Lambda functions has the necessary permissions to access DynamoDB.
You can use the provided IAM role inline policy.json as a reference to set up the policy.

Testing and Validation
After setting up, visit the URL provided by AWS Amplify to access your application.
Test the functionality of adding, viewing, and deleting data to ensure that the Lambda functions and API Gateway are correctly configured and interacting with DynamoDB.

Troubleshooting
If you encounter issues, check the AWS CloudWatch logs for your Lambda functions.
Verify that CORS is correctly enabled in API Gateway.
Ensure that the IAM roles have the appropriate permissions.

Conclusion
Once deployed, your web application should be able to perform CRUD operations, interfacing with AWS services. For any updates or changes, you can re-upload your files to AWS Amplify or adjust configurations in the Lambda, API Gateway, or DynamoDB consoles.
Manage AWS Resources - AWS Management Console - AWS
Manage your AWS cloud resources easily through a web-based interface using the AWS Management Console.
