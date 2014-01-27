def main():
    s = 0
    i = 0
    while i < 1000:
        if i%5 ==0:
            s += i
        elif i % 3 == 0:
            s += i
        i+=1
    print(s)


main()
