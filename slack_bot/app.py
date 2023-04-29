import json


def lambda_handler(event, context):
    print("event")
    print(str(event))
    print("context")
    print(str(context))

    decoded_body = json.loads(event["body"])
    challenge = decoded_body["challenge"]
    resp = {"challenge": challenge}

    return {
        "statusCode": 200,
        "body": json.dumps(resp),
    }
