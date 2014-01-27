def main():
    num = 600851475143
    largest = num
    while largest != 0:
        num = largest
        largest  = largestPF(largest)
    print(num)

def largestPF(num):
    i = 2
    while i < num:
        check = num % i
        if check == 0:
            return num/i
        i+=1
    return 0
main()
