from cs50 import get_string
import string

# Get input from user 

sentence = get_string("Text: ")
# print(sentence)

# Initialize variables
letters = 0
words = 1
sentences = 0

for letter in sentence:
    if letter == "!" or letter == "." or letter == "?":
        sentences = sentences + 1
    elif letter in string.whitespace:
        words = words + 1
    elif letter in string.punctuation:
        continue
    else:
        letters = letters + 1
        
    # Apply the formula
    L = letters / words * 100
    S = sentences / words * 100
    grade = round(0.0588 * L - 0.296 * S - 15.8)

# Check the results and print them

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade: {grade} ")