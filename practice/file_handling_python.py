import os
file = open('C://Users\chinn\OneDrive\Desktop\student_data.txt', 'r')

print("this file is empty" + file.read())
file = open('C://Users\chinn\OneDrive\Desktop\student_data.txt', 'w')
file.write(" 1previous data cleared")
file.close()