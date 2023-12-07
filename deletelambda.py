import boto3
import json

def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('form')
    
    # Check if pathParameters exists and has an 'id' key
    path_parameters = event.get('pathParameters')
    if not path_parameters or 'id' not in path_parameters:
        return {
            'statusCode': 400,
            'body': json.dumps('No ID provided in pathParameters')
        }
    
    item_id = path_parameters.get('id')

    # Proceed to delete the item from the DynamoDB table
    try:
        response = table.delete_item(
            Key={
                'id': item_id
            }
        )
        # Depending on your DynamoDB setup, you might need to handle the response differently
        # especially if you are using conditions or expecting certain return values

        return {
    'statusCode': 200,
    'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'  # or the specific domain you want to allow
    },
    'body': json.dumps('Item deleted successfully')
}
    except Exception as e:
        # Handle any exceptions that occur during the delete operation
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
