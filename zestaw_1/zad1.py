import sys

def factorize(num):
    k = 2
    
    numbers = [] #[num, exponent]
    while k*k <= num:
        count = 0
        while num % k == 0:
            num = num // k
            count += 1
        if count > 0:
            #print(k)
            numbers.append([k, count])
        k += 1
    if num > 1:
        numbers.append([num, 1])

    return numbers

def print_factorization(numbers):
    for i in range(len(numbers)):
        if numbers[i][1] > 1:
            print(f"{numbers[i][0]}^{numbers[i][1]}", end="")
        else:
            print(f"{numbers[i][0]}", end="")
        if i < len(numbers) - 1:
            print("*", end="")
    print()

if __name__ == "__main__":    
    argv = sys.argv[1:]

    for i in range(len(argv)):
        print(f"{argv[i]} = ", end="")
        print_factorization(factorize(int(argv[i])))

