import boto3

dynamodb = boto3.resource('dynamodb', region_name=region)

tables = list(dynamodb.tables.all())
print(tables)