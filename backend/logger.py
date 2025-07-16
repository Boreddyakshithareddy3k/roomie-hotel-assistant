import csv
from datetime import datetime

def log_chat(user, bot):
    with open("chat_logs.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), user, bot])
