import random
import string 

length = int(input("PASSWORD LENGTH: "))

chars = (
    string.ascii_letters +
    string.digits+
    string.punctuation

)

password = "".join(
    random.choice(chars)

    for _ in range(length)


)

print(" \n Generated Password: ")
print(password)