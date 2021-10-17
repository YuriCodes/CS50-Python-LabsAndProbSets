from cs50 import get_int

# Get input from user
height = get_int("Height: ")

# Check if the input is a positive int or no more than 8
while height > 8 or height < 1:
    height = get_int("Height: ")

#For loop for height, start at range 1, height+1
for i in range(1, height + 1):
    # Add spaces for each loop height-1
    print((height - i) * " ", end="")
    # Add hashtag for each i 
    print((i) * "#")