import json
import boto3
import base64
import torch
import torchaudio
import numpy as np

import copy

content_type = "application/json"
request_body = {"text": "你好,我是amazon sagemaker ChatTTS,欢迎你."}

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

# save
# wavs = base64.b64decode(result['wavs'])
# wavs = np.array(json.loads(wavs))
wavs = result['wavs']
for i in range(len(wavs)):
    with open (f"output_{i}.wav", "wb+") as f:
        f.write(base64.b64decode(wavs[i]))
