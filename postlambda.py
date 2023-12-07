import boto3
import json

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Parse the event body to get form data
    body = json.loads(event['body'])
    
    # Extract form data
    first_name = body['first_name']
    last_name = body['last_name']
    contact_number = body['contact_number']
    address = body['address']
    
    # Define the DynamoDB table
    table = dynamodb.Table('form')
    
    # Create a new record in the DynamoDB table
    response = table.put_item(
        Item={
            'id': context.aws_request_id,  # Unique ID for the entry
            'first_name': first_name,
            'last_name': last_name,
            'contact_number': contact_number,
            'address': address
        }
    )
    
    # Return a successful HTTP response
    return {
        'statusCode': 200,
        'body': json.dumps('Form submitted successfully')
    }
