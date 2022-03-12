from ntpath import join
import random
n = int(input("Enter the number of digits for your random password")) # Max length is 72
Upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Uppercase letters
Lower_case = "abcdefghijklmnopqrstuvwqyz" #Lowercase letters
Num_ = "1234567890" #Numbers
Spl_char = "!@#$%^&*.?" #Special characters
combined_chars = Upper_case + Lower_case + Num_ + Spl_char
len = n # length based on user input
psw = "".join(random.sample(combined_chars,len))
print("Your password is", psw) 
