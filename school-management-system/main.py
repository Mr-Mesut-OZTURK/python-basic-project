"""
This is my main program.
----------------------------
Created by Mesut.

"""

from document import password
from functions import sign_in
from pages import director, teacher, student

def main():

    print("""
            Welcome to my program!...
            What do you want to do?
    """)

 
    valid = []
    while True:
        print("""
            1 - Sign In
            2 - Exit
        """)

        task = input("What do you want to do : ").title().strip()
        print("*" * 50)


        # burası şifre kontrolu yapar
        if task == "1" or task == "Sign In":
            valid = sign_in.signin(password.paswords)
        elif task == "2":
            print("Take care of yourself!...")
            print("*" * 50)
            break
        else:
            print("Pleade enter correct number!...")
            print("*" * 50)



        # burası sayfaya yönlendirir eğer şifre doğruysa
        if valid:
            if valid["title"] == "director":
                director.director(valid)
            elif valid["title"] == "teacher":
                teacher.teacher(valid)
            elif valid["title"] == "student":
                student.student(valid)
        else:
            print("Kayıtlı kullanıcı değil...")
            print("*" * 50)



if __name__=="__main__":
    main()
    
