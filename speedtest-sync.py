from datetime import datetime
from dotenv import load_dotenv
import os
import subprocess
import json
import requests

load_dotenv()

api_path = "https://data.herron.dev"

api_user = os.getenv('API_USER')
api_password = os.getenv('API_PASSWORD')

current_time = datetime.utcnow().replace(microsecond=0).isoformat() + "+00:00"

# Measure speed
# This requires the speedtest cli: https://www.speedtest.net/apps/cli
command = "speedtest --server-id=12652 --format=json"
speedtest_result_string = subprocess.check_output(command, shell=True)

speedtest_result = json.loads(speedtest_result_string)

download = float(speedtest_result["download"]["bytes"])
upload = float(speedtest_result["upload"]["bytes"])

# Write to API
download_point_id = "a60c7956-7592-4095-8c04-ab6cc41e431a"
upload_point_id = "5350f77a-9e80-4e8e-8b81-047545a97a63"

token_request = requests.get(f"{api_path}/api/auth/token", auth=(api_user, api_password))
token_request.raise_for_status()
api_token = token_request.json()["token"]

download_request = requests.post(
    f"{api_path}/api/recs/{download_point_id}/history",
    headers = {"Authorization": f"Bearer {api_token}"},
    json = {
        "ts": current_time,
        "value": download
    }
)
download_request.raise_for_status()

upload_request = requests.post(
    f"{api_path}/api/recs/{upload_point_id}/history",
    headers = {"Authorization": f"Bearer {api_token}"},
    json = {
        "ts": current_time,
        "value": upload
    }
)
upload_request.raise_for_status()
