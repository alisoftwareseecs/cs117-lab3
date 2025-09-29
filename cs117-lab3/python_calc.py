while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Even/Odd\n6. Percentage\n7. Exit")
    choice = input("Choice: ")

    if choice == "7":
        break

    if choice in ["1","2","3","4","6"]:
        a = float(input("First number: "))
        b = float(input("Second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            print("Result:", a / b)
        elif choice == "6":
            print("Result:", (a / b) * 100, "%")

    elif choice == "5":
        n = int(input("Enter number: "))
        print("Even" if n % 2 == 0 else "Odd")
