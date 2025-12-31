from cs50 import get_string
text = get_string("Enter text: ")

letter = 0
words = 0
sentence = 0
for char in text:
    if char.isalpha():
        letter += 1
    elif char in ".!?":
        sentence += 1

words = len(text.split())
# Coleman-Liau formula
L = (letter / words) * 100
S = (sentence / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before grade 1")
elif index <= 16:
    print("Grade is 16+")
else:
    print(f"Grade is: {index}")