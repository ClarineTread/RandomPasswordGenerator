from ntpath import join
import random
n = int(input("Enter the number of digits for your random password"))
Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower_case = "abcdefghijklmnopqrstuvwqyz"
Num_ = "1234567890"
Spl_char = "!@#$%^&*.?"
combined_chars = Upper_case + Lower_case + Num_ + Spl_char
len = n
psw = "".join(random.sample(combined_chars,len))
print("Your password is", psw)