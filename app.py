# -- This script is made by --
# --      Omar Ashraf       --
# ----------------------------
import random
letters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '$', '@',
'!', '#', '%', '*', '(', '&', ')', '1', '2',
 '3', '4', '5', '6', '7', '8', '9']
length = 0
while length < 8 or length > 100:
    try:
        length = int(input("Enter the password length (min 8, max 100): "))
    except:
        length = int(input("Please try again: "))
password = ""
for i in range(length):
    lindex = random.randint(0, len(letters) - 1)
    password += str(letters[lindex])
print(password)
