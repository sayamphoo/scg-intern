import requests
import datetime
 
# === Config ===
webhook_url = "https://prod-47.southeastasia.logic.azure.com:443/workflows/ef25b5edd96c4013ac7cc6fb0ad8ec75/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=hr-HWHQjDGotmELlAHuzqOgU_IEjFUOM1raccWhS3RI"
headers = {
    "Content-Type": "application/json"
}
 
# === Message Construction ===

def send_alarm(message = None) :

    if not message:
        return 
    
    payload = {
        "text": message
    }

    # === Send POST ===
    try:
        response = requests.post(webhook_url, headers=headers, json=payload)
        response.raise_for_status()
        print("✅ Message sent successfully!")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("❌ Failed to send message:", e)