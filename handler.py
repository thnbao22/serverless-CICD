import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }
    print(event)

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
