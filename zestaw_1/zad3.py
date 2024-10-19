import datetime
import time

def show_time():
    while True:
        now = datetime.datetime.now()

        hour = now.hour
        minute = now.minute
        second = now.second

        print(chr(16) + f" {hour:02}:{minute:02}:{second:02} " + chr(17), end="\r")
        time.sleep(0.5)

if __name__ == "__main__":
    show_time()