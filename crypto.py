import random

class crypto():

    alfa = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%^&*()[]'#;/.,=-_+{}~@:?><\|`¬"
    def Encryption(self, password, keyfilename):
        keyfile = open(keyfilename, "r")
        key = keyfile.readline()
        scrambledpassword = ""
        for letter in password:
            for alletter in alfa:
                if alletter == letter:
                    scrambledpassword += key[alfa.index(alletter)]
        keyfile.close()
        return scrambledpassword
    

    def keygen(self, amountofchars, keyfilename):
        key = ""
        if amountofchars >= 55:
            return "Error 1: Amount of charecters is larger then the array lenth please use a value less then 55"
        indexArray = []
        lenOfIndexArray = indexArray
        for num in range(len(alfa)):
            indexArray.append(num)

        for letters in range(amountofchars):
            ranindexnum = random.choice(lenOfIndexArray)
            key += alfa[ranindexnum]
            indexArray.remove(ranindexnum)

        try: 
            keyfile = open(keyfilename, "w")
            keyfile.write(key)
            keyfile.close
            return key
        except FileExistsError:
            return key

    def Decryption(self, scrambledpassword, key):
        Decryptedpassword = ""
        for letter in scrambledpassword:
            for alletter in key:
                if letter == alletter:
                    Decryptedpassword += alfa[key.index(alletter)]
        return Decryptedpassword




