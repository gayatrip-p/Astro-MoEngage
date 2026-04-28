import requests

token_url = "https://ap-south-1ba9edxkbr.auth.ap-south-1.amazoncognito.com/oauth2/token"

client_id = "7at7pp1q2tan2vemdju45u0v6m"
client_secret = "5difhqhppv8kplrg6f6jsmq3as5rn4o7047njiof9jquc1rl53v"

data = {
    "grant_type": "client_credentials",
    "scope": "moengage-astro-dev/read moengage-astro-dev/write"
}

response = requests.post(
    token_url,
    auth=(client_id, client_secret),
    data=data
)

token_data = response.json()

access_token = token_data.get("access_token")
expires_in = token_data.get("expires_in")
token_type = token_data.get("token_type")

print("Access Token:", access_token)
print("Expires In:", expires_in)
print("Token Type:", token_type)