#!/usr/bin/env python

from user import User
def create_account(first_name,last_name,email,password):
        
        new_account = User(first_name,last_name,email,password)
        
        return new_account

def save_account(account):
        
        account.save_account()

# def log_in()

    
from user import Credentials
def create_credential(account_name, email, password):
        
        credential = Credentials(account_name, email, password)
        
        return credential

def save_credentials(credential):
        
        credential.save_credentials()

def save_multiple_credentials(account):
        
        account.save_multiple_credentials()

def display_credentials():
        return Credentials.display_credentials()

def delete_credentials():
        Credentials.delete_credentials





      

def main():
    print("Hello, I'm PaLo..otherwise known as Password Locker.I save your passwords for various accounts. Before we get to that part, I will need you to create an account or Log in:")
    print('\n')
    print("Use these short codes") 
    print("cc - create an account")
    print("lg - log in")
    print('\n')

    short_code = input().lower()
    if short_code == 'cc':
        print("Let's create a shiny new ac for you. I will need some information for that:")
        print('\n')
        print("First Name")
        first_name = input()
        print('\n')
        print("Second Name")
        last_name = input()
        print('\n')
        print("Email Address")
        email = input()
        print('\n')
        print("Password")
        print("-"*8)
        password = input()
        print('\n')
        save_account(create_account(first_name, last_name, email,password))
        print('\n')
        print(f"Welcome {first_name}, let's get started, shall we?")
        print('\n')

    elif short_code == 'lg':
        print('\n')
    #     print("Log In into your account:")
    #     print('\n')
    #     print("Email Address:")

    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list")
    short_code = input().lower()
    print('\n')
    if short_code == 'cc':
        print("New Credential")
        print("-"*10)
        print('\n')

        print("Account Name")
        account_name = input()
        print('\n')

        print("Email Address or Username")
        email = input()
        print('\n')

        print("Account's Password")
        password = input()

        save_credentials(create_credential(account_name, email, password))
    
    
    elif short_code == 'dc':
        if display_credentials():
                print("Here's your vault") 
                print('\n')
                for credential in display_credentials():
                        print(f"{credential.account_name} {credential.email} {credential.password}")
                print('\n')
        
        else:
                print('\n')
                print("Your vault is empty") 
                print('\n')  


    print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list")
    short_code = input().lower()
    print('\n')

if __name__ == '__main__':
    
    main()