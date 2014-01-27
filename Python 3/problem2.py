def main():
    curr = 1
    prev = 0
    s = 0
    while curr <= 4000000:
        if curr % 2 == 0:
            s += curr
        temp = curr
        curr = prev + curr
        prev = temp

    print(s)
main()
