import json
import boto3

content_type = "application/json"
request_body = {"text": "This is a test with NER in America with \
            Amazon and Microsoft in Seattle, writing random stuff."}

endpoint_name="sg"

runtime_sm_client = boto3.client(service_name='sagemaker-runtime')

#Serialize data for endpoint
#data = json.loads(json.dumps(request_body))
payload = json.dumps(request_body)

#Endpoint invocation
response = runtime_sm_client.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType=content_type,
        Body=payload)

#Parse results
result = json.loads(response['Body'].read().decode())
print(result)