def encrypt(message, shift):
    encrypted_value = ""
     

    for letter in message:
        if letter.isalpha():
         if letter.isupper() :

            encrypted_value += chr((ord(letter) - ord("A") + shift) % 26 +ord("A"))
         else:
            encrypted_value += chr((ord(letter) - ord("a") + shift)% 26 +ord("a"))   
        else:
            encrypted_value += letter

    return encrypted_value
def decrypt(message,shift):
   decrypted_value = ""
   decrypted_value += encrypt(message,-shift)
   return decrypted_value

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))


encrypted_value =encrypt(message,shift)
print( "encrypted value is : ",encrypted_value)
decrypted_value = decrypt(encrypted_value,shift)
print("decrypted value is : ",decrypted_value)