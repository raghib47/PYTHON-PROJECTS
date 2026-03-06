import random
import string

length = int(input("Enter password length: "))

lower = random.choice(string.ascii_lowercase)
upper = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)

remaining = length - 4
all_chars = string.ascii_letters + string.digits + string.punctuation

password = lower + upper + digit + symbol + ''.join(random.choice(all_chars) for i in range(remaining))

password_list = list(password)
random.shuffle(password_list)

final_password = ''.join(password_list)

print("Strong Password:", final_password)