import sys
import os
import time

def show_text(text):
    height = 10

    cur_height = 1
    direction = 1

    while True:
        os.system('cls')
        print("="*20)
        for _ in range(cur_height):
            print("")

        print(text)

        for _ in range(height - cur_height):
            print("")

        print("="*20)
        

        if cur_height >= height or cur_height <= 0:
            direction *= -1

        cur_height += direction
        time.sleep(0.3)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Type text to be shown")
        exit(1)
    show_text(sys.argv[1])
