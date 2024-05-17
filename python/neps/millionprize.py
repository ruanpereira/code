def main():

    n = int(input()) # number of inputs

    day = 0; total_acess = 0

    for i in range(n):
        acess = int(input())
        total_acess += acess

        if n == 1:
            if acess >= 1e6:
                day = 1

        elif total_acess <= 1e6:
            day += 1

    print(day)

if __name__ == "__main__":
    main()

