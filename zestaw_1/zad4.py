import sys
import time


def progress_bar(seg_len):

    for i in range(0, 101):
        bar = "|"
        done_segments = i * seg_len // 100

        bar += done_segments * "="
        bar += (seg_len - done_segments) * "-"
        bar += "|" + f" {i}%"

        time.sleep(0.2)
        print(bar, end="\r")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Type length of a progress bar")
        exit(1)

    length = int(sys.argv[1])
    if length < 1:
        print("Length must be greater than 1")
        exit(1)
    
    progress_bar(length)