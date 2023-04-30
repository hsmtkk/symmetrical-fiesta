import json
import os

import requests


def lambda_handler(event, context):
    print("event")
    print(str(event))
    print("context")
    print(str(context))

    decoded_body = json.loads(event["body"])

    if decoded_body["type"] == "url_verification":
        challenge = decoded_body["challenge"]
        resp = {"challenge": challenge}
        return {"statusCode": 200, "body": json.dumps()}

    token = os.environ["BOT_TOKEN"]
    channel = decoded_body["event"]["channel"]
    text = "dummy"
    for elem in decoded_body["event"]["blocks"][0]["elements"][0]["elements"]:
        if elem["type"] == "text":
            text = elem["text"]

    payload = {
        "token": token,
        "channel": channel,
        "text": text,
    }

    resp = requests.post("https://slack.com/api/chat.postMessage", data=payload)
    print("response")
    print(resp.status_code)
    print(resp.json())

    return {"statusCode": 200}
