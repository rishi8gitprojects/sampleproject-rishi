import random
import string

aplha, nums, punctuations = string.ascii_letters, string.digits, string.punctuation
chosen1, chosen2, chosen3 = random.choices(aplha, k=8), random.choices(nums, k=4), random.choices(punctuations, k=4)

password = chosen1 + chosen2 + chosen3

print("Your password" )
print("".join(password))