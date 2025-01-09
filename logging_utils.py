import datetime

LOG_FILE = "data/authentication_log.txt"

def log_authentication(status, user_id):
    with open(LOG_FILE, 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - Status: {status}, User ID: {user_id}\n")
