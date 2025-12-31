def is_fifteendigits(number):
    length = 0
    temp = number
    while temp > 0:
        temp //= 10
        length += 1
    return length == 15


def sixteen_digits(number):
    length = 0
    temp = number
    while temp > 0:
        temp //= 10
        length += 1
    return length == 16


def is_thirteendigits(number):
    length = 0
    temp = number
    while temp > 0:
        temp //= 10
        length += 1
    return length == 13


while True:
    card_number = int(input("Enter your credit card number: "))
    if 1 <= card_number <= 9999999999999999:
        break

first       = card_number % 10
second      = (card_number % 100) // 10
third       = (card_number % 1000) // 100
fourth      = (card_number % 10000) // 1000
fifth       = (card_number % 100000) // 10000
sixth       = (card_number % 1000000) // 100000
seventh     = (card_number % 10000000) // 1000000
eighth      = (card_number % 100000000) // 10000000
ninth       = (card_number % 1000000000) // 100000000
tenth       = (card_number % 10000000000) // 1000000000
eleventh    = (card_number % 100000000000) // 10000000000
twelfth     = (card_number % 1000000000000) // 100000000000
thirteenth  = (card_number % 10000000000000) // 1000000000000
fourteenth  = (card_number % 100000000000000) // 10000000000000
fifteenth   = (card_number % 1000000000000000) // 100000000000000
sixteenth   = (card_number % 10000000000000000) // 1000000000000000

sum_ = 0

for digit in [second, fourth, sixth, eighth, tenth, twelfth, fourteenth, sixteenth]:
    doubled = digit * 2
    if doubled > 9:
        sum_ += (doubled % 10) + 1
    else:
        sum_ += doubled

# Add remaining digits
sum_ += first + third + fifth + seventh + ninth + eleventh + thirteenth + fifteenth

# Validity check
if sum_ % 10 == 0:
    print("Valid credit card number")
else:
    print("Invalid credit card number")

# Card type detection
if is_fifteendigits(card_number):
    if fifteenth == 3 and (fourteenth == 4 or fourteenth == 7):
        print("American Express")

elif sixteen_digits(card_number):
    if sixteenth == 4:
        print("Visa")
    elif sixteenth == 5 and 1 <= fifteenth <= 5:
        print("MasterCard")

elif is_thirteendigits(card_number):
    if thirteenth == 4:
        print("Visa")
