#!/usr/bin/env python3

def slice_email(email):
    username, domain = email.split('@')
    return(f"Username: {username}\nDomain: {domain}")


if __name__ == '__main__':
    email = input("Enter the email to slice: ")
    print(slice_email(email))
