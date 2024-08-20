# ZenoPay/utils.py

def log_error(message):
    with open('error_log.txt', 'a') as error_log:
        error_log.write(message + "\n")
