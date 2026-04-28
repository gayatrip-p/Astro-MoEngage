import requests
import json

url = "https://zre7gcptjg.execute-api.ap-south-1.amazonaws.com/dev/ingest"

# Replace with your actual token
token = "eyJraWQiOiJmZFBOUzJcL0duSkpuZFltTkZ3WFpid011dFBWYURNUE9mYms2XC9lNk5WSVk9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI3YXQ3cHAxcTJ0YW4ydmVtZGp1NDV1MHY2bSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoibW9lbmdhZ2UtYXN0cm8tZGV2XC93cml0ZSBtb2VuZ2FnZS1hc3Ryby1kZXZcL3JlYWQiLCJhdXRoX3RpbWUiOjE3NzU2Mzk2OTMsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoLTFfYkE5ZWRYa2JSIiwiZXhwIjoxNzc1NzI2MDkzLCJpYXQiOjE3NzU2Mzk2OTMsInZlcnNpb24iOjIsImp0aSI6ImU1NGE0YTYxLWIwODAtNDkyYi1iOTJhLWQ0YTdkYjhlNGY1NiIsImNsaWVudF9pZCI6IjdhdDdwcDFxMnRhbjJ2ZW1kanU0NXUwdjZtIn0.LI8h_YpsLU5XgB0AsoOZZrTO_4sWwEzIsc-1VnKXsaz_ibTE9UIejwPwaAPReyQsOY9997RHXyjT4fo_0HWNyjgbDPPPPy1N2n_F7RYSsHAdn4KJAkmXi9orVgyTIs99PQIO0TyFt0XYAcAaJf82k9k6L9GheSvvF0ig-NvEcubyT1QYOtEN4xejwBSB61p1FivATNxfCFlAiu8FgvurCZWs6aSGMcnHlQ6rpK8cgJOKTEGFhYJVm8hWcdeiOIdq-eWVZZKEcuWBvaWdOx2s5oOTbuFio5dVIB6QRgj1QkvVnovrH6I1bYV_ypwRad62vDYGD4n4WY1BFQc6y3qHOQ"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

for i in range(1, 11):
    payload = {
        "workspace": "Portals",
        "segment": "Sports_Sports",
        "segmentID": f"seg_{i}",
        "MOEID": f"user_{i}",
        "ADID": "",
        "IDFA": "",
        "EPUID": ""
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    print(f"Request {i}: Status Code = {response.status_code}")