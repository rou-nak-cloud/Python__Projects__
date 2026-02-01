import json #to store the user data in json format while the app is closed
import random #to generate random account number
import string #to generate random account number with string and digits
from pathlib import Path #to create a path to the json file


class Bank:
    database = Path(__file__).parent / "data.json" #path to the json file
    information = [] #list to store multiple user data as a DUMMY data loading from the json
    
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                information = json.loads(fs.read()) #loading the data from the json file
        else:
            print("No database found!")
    except Exception as err:
        print(f"Error loading database: {err}")
    
    #create a static method to update the json file whenever there is a change in the data
    @classmethod
    def __update(cls):
        try:
            with open(cls.database,'w') as fs:
                fs.write(json.dumps(cls.information)) #writing the updated data to the json file
        except Exception as err:
            print(f"Error updating database: {err}")
            
    
    def deposit_amount(self):
        account_no = input("Enter your account number: ")
        pin_no = input("Enter your 4 digit PIN: ")
        #print(Bank.information) #to see the existing data
        
        '''Searching for the user in the existing data'''
        user_data = [i for i in Bank.information if i['account_no'] == account_no and i['pin'] == pin_no] 
        if user_data:
            print(f"Welcome {user_data[0]['first_name']} {user_data[0]['last_name']}! for depositing money.")
            
            amount = float(input("Enter the amount to deposit: "))
            if amount < 0 or amount > 10000:
                print("Transactions Limited! Please enter a valid amount below 10,000 as per rules.")
                return
            else:
                user_data[0]['balance'] += amount #changes in the dummy data information
                Bank.__update() #update the json file with the new balance
                print(f"Amount ₹{amount} deposited successfully. Your new balance is ₹{user_data[0]['balance']}")
        else:
            print("Invalid Account Number or PIN!")
            
    def withdraw_amount(self):
        account_no = input("Enter your account number: ")
        pin_no = input("Enter your 4 digit PIN: ")
        #print(Bank.information) #to see the existing data
        
        '''Searching for the user in the existing data'''
        user_data = [i for i in Bank.information if i['account_no'] == account_no and i['pin'] == pin_no] 
        if user_data:
            print(f"Welcome {user_data[0]['first_name']} {user_data[0]['last_name']}! for withdrawing money.")
            
            amount = float(input("Enter the amount to withdraw: "))
            if user_data[0]['balance'] < amount:
                print("Insufficient Balance!")
                return
            else:
                user_data[0]['balance'] -= amount #changes in the dummy data information
                Bank.__update() #update the json file with the new balance
                print(f"Amount ₹{amount} withdrawn successfully. Your new balance is ₹{user_data[0]['balance']}")
        else:
            print("Invalid Account Number or PIN!")
            
            
            
    def view_details(self): #to view the details of the user
        account_no = input("Enter your account number: ")
        pin_no = input("Enter your 4 digit PIN: ")
        
        '''Searching for the user in the existing data'''
        user_data = [i for i in Bank.information if i['account_no'] == account_no and i['pin'] == pin_no] 
        if user_data:
            print(f"Welcome {user_data[0]['first_name']} {user_data[0]['last_name']}! Here are your details:")
            for i in user_data[0]:
                print(f"{i.replace('_',' ').title()} : {user_data[0][i]}")
        else:
            print("Invalid Account Number or PIN!")


    def update_details(self): 
        account_no = input("Enter your account number: ")
        pin_no = input("Enter your 4 digit PIN: ")
        
        user_data = [i for i in Bank.information if i['account_no'] == account_no and i['pin'] == pin_no] 
        if user_data == False:
            print("Invalid Account Number or PIN!")
            return
        else:
            print(f"Welcome {user_data[0]['first_name']} {user_data[0]['last_name']}! You can update your details here.")
            print("Fill the details below (Leave blank if you don't want to change):")
            
            # creating new information dictionary
            new_user_data = {
                "first_name": input(f"Enter first name or press enter to keep:"),
                "last_name": input(f"Enter last name or press enter to keep:"),
                "email": input(f"Enter email or press enter to keep:"),
                "pin": input(f"Enter new 4-digit pin or press enter to keep:"),
                "aadhar": input(f"Enter new 12 digit Aadhar number or press enter to keep:"),
                "phone": input(f"Enter new phone number or press enter to keep:"),
                "account_type": input(f"Enter new account type or press enter to keep:")
            }
            #checking for blank entries and keeping old data if blank
            if new_user_data["first_name"] == "":
                new_user_data["first_name"] = user_data[0]["first_name"]
            if new_user_data["last_name"] == "":
                new_user_data["last_name"] = user_data[0]["last_name"]
            if new_user_data["email"] == "":
                new_user_data["email"] = user_data[0]["email"]
            if new_user_data["pin"] == "":
                new_user_data["pin"] = user_data[0]["pin"]
            if new_user_data["aadhar"] == "":
                new_user_data["aadhar"] = user_data[0]["aadhar"]
            if new_user_data["phone"] == "":
                new_user_data["phone"] = user_data[0]["phone"]
            if new_user_data["account_type"] == "":
                new_user_data["account_type"] = user_data[0]["account_type"]
            
            #not changing the account number and balance as well as age
            new_user_data["age"] = user_data[0]["age"]
            new_user_data["account_no"] = user_data[0]["account_no"]
            new_user_data["balance"] = user_data[0]["balance"]
            new_user_data["gender"] = user_data[0]["gender"]
            
            # PIN validation
            if not str(new_user_data['pin']).isdigit() or len(str(new_user_data['pin'])) != 4:
                print("Invalid PIN! PIN must be exactly 4 digits.")
                return

            # Aadhaar validation
            if not str(new_user_data['aadhar']).isdigit() or len(str(new_user_data['aadhar'])) != 12:
                print("Invalid Aadhar Number! Aadhar must be exactly 12 digits.")
                return  
            
            
            #updating the user data with the new data
            for i in new_user_data:
                if new_user_data[i] == user_data[0][i]:
                    continue
                else:
                    user_data[0][i] = new_user_data[i]
                    
            Bank.__update() #updating the json file with the new data
            print("Details updated successfully!")
            



    def delete_account(self):
        account_no = input("Enter your account number: ")
        pin_no = input("Enter your 4 digit PIN: ")
        
        user_data = [i for i in Bank.information if i['account_no'] == account_no and i['pin'] == pin_no] 
        if user_data == False:
            print("Invalid Account Number or PIN!")
            return
        else:
            confirmation = input(f"Are you sure you want to delete the account {account_no} with type of {user_data[0]['account_type']}? This action cannot be undone. (yes/no): ")
            if confirmation.lower() == 'yes':
                Bank.information.remove(user_data[0]) #removing the user data from the dummy data
                Bank.__update() #updating the json file
                print("Account deleted successfully!")
            else:
                print("Account deletion cancelled.")


    
    @classmethod
    def __account_number(cls):
        '''Generate a unique 10-digit account number.'''
        alpha = random.choices(string.ascii_uppercase,k=4)
        nums = random.choices(string.digits,k=6)
        id = alpha + nums # return a list of characters
        random.shuffle(id) #shuffle the list to make it random
        return ''.join(id) #join the list to make it a string and return
    
    
    def create_account(self):
        data = {
            "first_name": input("Enter your first name: "),
            "last_name": input("Enter your last name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "gender": input("Enter your gender (M/F/Other): "),
            "aadhar": input("Enter your Aadhar number: "),
            "account_type": input("Enter account type (Savings/Current): "),
            "pin": input("Set your 4-digit PIN: "),
            "phone": input("Enter your phone number: "),
            "account_no": Bank.__account_number(),
            "balance": 0.0
        }
        
        if data['age'] < 18 or len(str(data['pin'])) != 4 or len(str(data['aadhar'])) != 12:
            print("Invalid details provided. Account creation failed.")
            return
        else:
            print("\nAccount created successfully!\n")
            # to see the user filled data
            for i in data:
                print(f"{i} : {data[i]}")
            print("Please check your filled details and please keep your account number safe as well as note down your pin.")
            
            # then update the details
            Bank.information.append(data) #class data is updated with the new user data
            Bank.__update() #through update function 


user = Bank() #Creating an object of Bank class

print("Welcome to the Bank Management System!")
print("Press 1 for Creating Account")
print("Press 2 for Deposit Amount")
print("Press 3 for Withdraw Amount")
print("Press 4 for Details")
print("Press 5 for Updating Details")
print("Press 6 for Deleting Account")


check = int(input("Enter your choice: "))

if check == 1:
    print("Creating Account is in progress...")
    user.create_account() #Calling create_account method using object
    
if check == 2:
    print("Deposit Money...")
    user.deposit_amount() 

if check == 3:
    print("Withdraw Money...")
    user.withdraw_amount()
    
if check == 4:
    print("View Details...")
    user.view_details()
    
if check == 5:
    print("Updating Details...")
    user.update_details()
    
if check == 6:
    print("Deleting Account...")
    user.delete_account()



