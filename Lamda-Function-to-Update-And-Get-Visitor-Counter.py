import boto3


def lambda_handler(event, context):
    tableName = "site-visit"
    DB = boto3.resource('dynamodb')
    table = DB.Table(tableName)
    
    #Key - which object should be updated
    #ExpressionAttributeValues - map with new values
    #UpdateExpression - how these new values should be applied to the object in the table
    response1 = table.update_item( Key={
        'Name': 'TotalVisitor'
    }, 
    UpdateExpression='ADD Amount :a',  
    ExpressionAttributeValues={
        ':a': 1
    },
    ReturnValues="UPDATED_NEW"
    
    )

    response = table.get_item(Key={'Name': 'TotalVisitor'})['Item']

    
    return response

    