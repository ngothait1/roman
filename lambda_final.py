import json
import logging
import time
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
bucket_name = "lambda-files-bucker-roman"
calc_logs = {}

logs_filename = "logs_calc.txt"

def handleEmptyPath():
    get_file = s3.get_object(
        Bucket=bucket_name,
        Key=logs_filename
        )
    logs_body = get_file["Body"].read().decode("utf-8")
    return {
        'statusCode': 200,
        'body': json.dumps(logs_body)
    }


template = {
            "number_1": "int",
            "number_2": "int",
            "operation": "str, within {+, -, *, /}"
            }

def handleCalculations(method, data):
    if method == "GET":
        return {
            'statusCode': 200,
            'body': json.dumps(template)
        }
    elif method == "POST":
        data = json.loads(data)
        number_1 = data["number_1"]
        number_2 = data["number_2"]
        if not isinstance(number_1, int):
            return {
                'statusCode': 400,
                'body': json.dumps(f"{number_1} is not an integer")
            }
        if not isinstance(number_2, int):
            return {
                'statusCode': 400,
                'body': json.dumps(f"{number_2} is not an integer")
            }
        if data["operation"] == "+":
            result = number_1 + number_2
        elif data["operation"] == "-":
            result = number_1 - number_2
        elif data["operation"] == "*":
            result = number_1 * number_2
        elif data["operation"] == "/":
            if number_2 == 0:
                return {
                    'statusCode': 400,
                    'body': json.dumps("Cannot divide by zero")
                }
            result = number_1 / number_2
        else:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Opepator {data["operation"]} unsupported.")
            }

        result_str = f"{number_1} {data["operation"]} {number_2} = {result}"

        get_file = s3.get_object(
            Bucket=bucket_name,
            Key=logs_filename
            )
        calc_logs[time.time()] = result_str

        s3.put_object(
            Bucket=bucket_name,
            Key=logs_filename,
            Body=json.dumps(calc_logs)
            )

        return {
            'statusCode': 200,
            'body': json.dumps(result_str)
        }

def lambda_handler(event, context):
    path = event["path"]
    method = event["httpMethod"]
    data = event["body"]
    if path == "/":
        return handleEmptyPath()
    elif path == "/calc":
        return handleCalculations(method, data)