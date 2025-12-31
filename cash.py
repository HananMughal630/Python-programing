from cs50 import get_float

while True:
    change = get_float("Enter a positive amount of change (dollars): ")
    if change > 0:
        break

change = round(change * 100)
quater = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickle = change / 5
change = change % 5

pennie = change
pennie = change

total_coin = int(quater + dimes + nickle + pennie)
print(f"Total amount is : {total_coin}")

