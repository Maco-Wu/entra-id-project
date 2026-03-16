import msal
import requests
import json
import uuid

# --- 1. Authentication Credentials ---
TENANT_ID = "YOUR_CLIENT_SECRET_HERE"
CLIENT_ID = "YOUR_CLIENT_SECRET_HERE"
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
DOMAIN = "YOUR_DOMAIN_HERE" 

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["https://graph.microsoft.com/.default"]

# --- 2. Authenticate with Microsoft Entra ID ---
print("Authenticating with Azure...")
app = msal.ConfidentialClientApplication(
    CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
)
result = app.acquire_token_for_client(scopes=SCOPES)

if "access_token" in result:
    print("Authentication Successful! Token acquired.")
    access_token = result["access_token"]
else:
    print("Authentication Failed.")
    print(result.get("error_description"))
    exit()

# --- 3 & 4. Loop to Generate 50 Users ---
print("Beginning bulk user creation...")
endpoint = "https://graph.microsoft.com/v1.0/users"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Loop from 1 to 50
for i in range(1, 51):
    first_name = "Cloud"
    last_name = f"User{i}"
    display_name = f"{first_name} {last_name}"
    nickname = f"cuser{i}"
    
    temp_password = f"SecurePass!{uuid.uuid4().hex[:8]}" 
    
    user_data = {
        "accountEnabled": True,
        "displayName": display_name,
        "mailNickname": nickname,
        "userPrincipalName": f"{nickname}@{DOMAIN}",
        "passwordProfile": {
            "forceChangePasswordNextSignIn": True,
            "password": temp_password
        }
    }

    print(f"[{i}/50] Attempting to create user: {display_name}...")
    response = requests.post(endpoint, headers=headers, json=user_data)

    if response.status_code == 201:
        print(f"  -> Success! Password: {temp_password}")
    else:
        print(f"  -> Failed. Status Code: {response.status_code}")
        # We don't exit the loop on failure, so it continues trying the rest