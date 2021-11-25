import crypto
import sys

incryption = crypto.crypto
key = incryption.keygen(0, len(incryption.alfa), "key.txt")


app = input("enter the application: ")
username = input("enter the username: ")
password = input("enter your password: ")

new_password = incryption.Encryption(0, password, "key.txt")



f = open("password.txt", "a")
f.writelines(app + " - username{" + username + "} password{"+ new_password +"} \n")
f.writelines("key{"+key+"}\n\n")
f.close

print("done!")

input("password creator will now exit: ")




