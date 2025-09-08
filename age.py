while True:
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if 0 <= age <= 120:
        break
    else:
        print("Enter a valid age inside the range (0-120)")
print(age)