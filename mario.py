while True:
    number = int(input("Enter any number: ")) 
    if number > 0 and number < 9:
       break
for i in range(number+1):
    for j in range(number-i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print()
