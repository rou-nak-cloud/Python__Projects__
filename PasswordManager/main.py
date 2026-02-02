from pathlib import Path
from cryptography.fernet import Fernet

'''writing the key, for one time use
def write_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)        
write_key() 
'''
# load the previously generated key
def load_key():
    file = open("secret.key", "rb")
    key = file.read()
    file.close()
    return key

print("Master Password?")
master_pwd = input("Hint: You are the system administrator: ")
# Check master password
if master_pwd.lower() == "admin":
    key = load_key() + master_pwd.encode()  # convert to bytes
    fer = Fernet(key)

else:
    print("Wrong master password! Access denied.")
    quit()


database = Path(__file__).parent/'password.txt'

def add():
    name= input("Account Name: ")
    pwd = input("Password: ")
    
    with open(database,'a') as fs:
        fs.write(name + ' | ' + str(fer.encrypt(pwd.encode()).decode()) + "\n") # encoding the pwd to its byte string form and then decode top its string form to store it


def view():
    with open(database,'r') as fs:
        for line in fs.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print("User:", user, "Password:", fer.decrypt(passw.encode()).decode()) # as we stored it in string form we need to encode it back to byte string form for decrypting

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? Type 'q' to quit. ").lower()
    if mode == 'q':
        break
    
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue