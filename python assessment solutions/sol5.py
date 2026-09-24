l = list(map(int, input("Enter numbers separated by space: ").split()))

while True:
    print("\n1. Add all numbers")
    print("2. Find highest number")
    print("3. Find average")
    print("4. Find number with highest frequency")
    print("5. Exit")

    c = int(input("Enter your choice: "))

    if c == 1:
        print("Sum =", sum(l))

    elif c == 2:
        print("Highest number =", max(l))

    elif c == 3:
        print("Average =", sum(l) / len(l))

    elif c == 4:
        m = 0
        x = l[0]

        for i in l:
            f = l.count(i)

            if f > m:
                m = f
                x = i

        print("Number with highest frequency =", x)
        print("Frequency =", m)

    elif c == 5:
        print("Program ended")
        break

    else:
        print("Invalid choice")