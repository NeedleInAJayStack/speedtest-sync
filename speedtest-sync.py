from datetime import datetime
from dotenv import load_dotenv
import os
import subprocess
import json
import psycopg2

load_dotenv()

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

current_time = datetime.now()

# Measure speed
# This requires the speedtest cli: https://www.speedtest.net/apps/cli
command = "speedtest --server-id=12652 --format=json"
speedtest_result_string = subprocess.check_output(command, shell=True)

speedtest_result = json.loads(speedtest_result_string)

download = speedtest_result["download"]["bytes"]
upload = speedtest_result["upload"]["bytes"]

# Write to SQL
download_point_id = "a60c7956-7592-4095-8c04-ab6cc41e431a"
upload_point_id = "5350f77a-9e80-4e8e-8b81-047545a97a63"

conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
cur = conn.cursor()

cur.execute("INSERT INTO his (\"pointId\", ts, value) VALUES (%s, %s, %s)", (download_point_id, current_time, download))
cur.execute("INSERT INTO his (\"pointId\", ts, value) VALUES (%s, %s, %s)", (upload_point_id, current_time, upload))

conn.commit()
cur.close()
conn.close()
