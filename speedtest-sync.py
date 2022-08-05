import datetime
from dotenv import load_dotenv
import os
import psycopg2
import speedtest

load_dotenv()

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

print(db_host)

# s = speedtest.Speedtest()
# s.get_servers()
# s.get_best_server()
# s.download()
# s.upload()
# s.results.share()
# results_dict = s.results.dict()
# download = results_dict["download"]
# upload = results_dict["upload"]

# conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)
# cur = conn.cursor()

# cur.execute("INSERT INTO his (pointId, ts, val) VALUES (%s, %s, %s)", ("", datetime.now(), download))

