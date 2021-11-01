"""
This is sign in modul.
"""

# import password

def signin(password):
    username = input("Please enter your user name : ").lower().strip()
    passwd = input("Please enter your password : ").strip()
    password = password
    control = user_control(username,passwd,password)
    return control


 

def user_control(username,passwd,password):
    
    for i in password:
        if (i["name"] == username) and (i["password"] == passwd):
            return i
    return ""


if __name__=="__main__":
    signin()