# Program Name : Bank Manager
# The purpose of this program is allow users to login to their bank account and
# withdraw or deposit money

import os

# The MAIN MENU that shows up when program is started
def mainMenu():
  print("Welcome to our bank! What would you like to do? \n")
  choice = input("==============Main Menu============== \n\
Login \n\
Register \n\
Exit \n\
\n").lower()
  if choice == "login":
    os.system('clear')
    login()
  elif choice == "register":
    os.system('clear')
    register()
  elif choice == "exit":
    print("\nYou have exited")
    exit()
  else:
    os.system('clear')
    print("\nPlease pick Login or Register")
    print("")
    mainMenu()  

def register():
  name = input("\nFull Name: ")
  pinNumber = int(input("Pin Number: "))

  # This if statement makes sure the pin number is not long
  if len(str(pinNumber)) > 5:
    print("\nA pin number can only be 5 numbers or less")
    register()
    
  username = input("Username (for login): ")
  password = input("Password: ")
  confirmPassword = input("Confirm Password: ")
  
  # Password confirmation
  if password != confirmPassword:
    print("\nYour passwords do not match up")
    register()

  # Adding the information that has been registered into a text file using a list
  account = []

  account.append(name)
  account.append(pinNumber)
  account.append(username)
  account.append(password)
  account.append(0)

  
  accountFile = open("accounts.txt","a")
  accountFile.write("\n")
  accountFile.write(str(account)) 
  accountFile.close()

  os.system('clear')
  print("\nYou have successfully registered your account, you now may login\n")
  mainMenu()  

def login():
  global accountInfo
  
  accountInfo = []
  
  loginUsername = input("\nUsername: ")
  
  accountFile = open("accounts.txt","r")

  # Check if login details in the Bank's database
  for Line in accountFile:
    if loginUsername in Line:
      accountInfo = eval(Line)
      if accountInfo[2] == loginUsername:
        loginPINnumber = input("Pin Number: ")
        if str(accountInfo[1]) == loginPINnumber:
          loginPassword = input("Password: ")
          if accountInfo[3] == loginPassword:
            os.system('clear')
            print("\nHello " + accountInfo[0] + ", you have successfully logged in")
            moneyMenu()
          else:
            print("\nPassword does not match the account")
            login()
        else:
          print("\nPin Number does not math with username")
          login()

  print("\nThat username is not in our database, try registering it\n")
  mainMenu()

# Options for balance, withdraw, and deposit are in the money MENU
def moneyMenu():
  choice = input("\n==============Menu============== \n\
Balance \n\
Withdraw \n\
Deposit \n\
Logout \n\
\n").lower()

  if choice == "balance" or choice == "bal":
    os.system('clear')
    balance()
  elif choice == "withdraw" or choice == "with":
    os.system('clear')
    amount = int(input("Withdraw amount: "))
    withdraw(amount)
  elif choice == "deposit" or choice == "dep":
    os.system('clear')
    amount = int(input("\nDeposit amount: "))
    deposit(amount)
  elif choice == "logout":
    os.system('clear')
    mainMenu()
  else:
    os.system('clear')
    print("\nPlease pick Balance or Withdraw or Deposit or Logout")
    moneyMenu()       

# Uses the parameter to get the amount from the user and change the value in the txt file by removing money
def withdraw(amount):
  if amount > accountInfo[4]:
    print("\nYou cannot withdraw more money then you have, check your balance to see how much you have")
    moneyMenu()
  elif amount < 0:
    print("\nAmount cannot be less then 0")
    moneyMenu()
  else:
  # Begin Cited Code 
  # Code is based off the link bellow
  # https://pynative.com/python-delete-lines-from-file/
    with open("accounts.txt", "r") as file:
      lines = file.readlines()

    with open("accounts.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != str(accountInfo):
                file.write(line)
  # End Cited Code
              
    accountInfo[4] -= amount 
    
    accountFile = open("accounts.txt","a")
    accountFile.write(str(accountInfo)) 
    accountFile.close()

    print("\nYou have successfully withdrawn $" + str(amount) + " from your account")
    print("\nYour new balance is $" + str(accountInfo[4]))
    moneyMenu()

# Uses the parameter to get the amount from the user and change the value in the txt file by adding money
def deposit(amount):
  if amount < 0:
    print("\nAmount cannot be less then 0")
    moneyMenu()

  # Begin Cited Code 
  # Code is based off the link bellow
  # https://pynative.com/python-delete-lines-from-file/
  with open("accounts.txt", "r") as file:
    lines = file.readlines()

  with open("accounts.txt", "w") as file:
      for line in lines:
          if line.strip("\n") != str(accountInfo):
              file.write(line)
  #End Cited Code

  accountInfo[4] += amount 

  accountFile = open("accounts.txt","a")
  accountFile.write(str(accountInfo)) 
  accountFile.close()

  print("\nYou have successfully deposited $" + str(amount) + " from your account")
  print("\nYour new balance is $" + str(accountInfo[4]))
  moneyMenu()

# This simply prints your balance
def balance():
  print("Balance : $" + str(accountInfo[4]))
  moneyMenu()

mainMenu()
