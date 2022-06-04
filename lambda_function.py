import json
import boto3
from random import randint

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    
    queue="<SQS-URL>";
    
    departments = ["finance", "sales"]
    text = ""
    
    for i in range(50):
        
        random = randint(0, 1)
        
        department = departments[random]
        
        if(department == "finance"):
            text = "Lot of consumers, but this is a sensitive and personal information that only finance department can read"
        else:
            text = "Lot of consumers, sensitive / personal information directly for sales department, just them can read"
    
        message={"department": department, "data":text+" (could be a json)"};
    
        msg = sqs.send_message(QueueUrl = queue, MessageBody = json.dumps(message))

    print("end")