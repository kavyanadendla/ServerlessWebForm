import boto3
import json

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('form')

    # Perform the query to retrieve all items
    response = table.scan()

    # The scan method can retrieve all items in the table, which can be expensive and slow
    # Consider using the query method if you're dealing with a large amount of data
    # or need to filter the results.

    items = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(items),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'  # Required for CORS support to work
        }
    }
