import random 
import string


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
symbols = string.punctuation
digits  = string.digits

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits 
if syms:
    all += symbols

length = 20
amount = 5

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
    










