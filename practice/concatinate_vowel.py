my_string = input('PLEASE ENTER ALPHABETS ONLY :')
my_string = my_string.upper()
my_list = []
for char in my_string:
    if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        my_list.append(char)
print(my_list)
