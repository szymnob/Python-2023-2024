import sys

def ruler(length):
    seg_len = 5

    ruler = ""

    for i in range(length):
        ruler += "|" + (seg_len-1)*"." 
    ruler += "|\n0"

    for i in range(1, length+1):
        num_len = len(str(i))
        ruler += (5 - num_len) * " " + str(i)

    print(ruler)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Type length of a ruler")
        exit(1)

    length = int(sys.argv[1])
    if length < 1:
        print("Length must be greater than 0")
        exit(1)
    
    ruler(length)