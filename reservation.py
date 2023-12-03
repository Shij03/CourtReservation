import random
import sys

courts = []
queue = []
people = {}
passwords = ["bear", "cat", "dog", "bat", "fox", "deer", "bird"]
def user_screen():  #enter name to computer generated password is given
    check = True
    while check:
        user = input("Enter your name: ")
        rand = random.randint(-1, 6)
        if user not in people:
            people.update({user:passwords[rand]})
            print("Your name is: " + user)
            print("Your password is: " + people.get(user))
            check = False
            home_screen()
        else:
            print("This name is taken! Please choose another name!")


def home_screen():  #display courts(name, time remain), display queue, ability to sign up for courts
        print("\n1. View Courts\n"
              "2. View Queue\n"
              "3. Sign up\n"
              "4. Sign out\n"
              "5. Player Sign up\n"
              "6. Exit")
        choice = int(input("What would you like to do?\n"))
        if choice == 1:
            print("Current courts: ")
            print(courts)
            home_screen()
        if choice == 2:
            print("People in queue: ")
            print(queue)
            home_screen()
        if choice == 3:
            signup_screen()
        if choice == 4:
            signout_screen()
        if choice == 5:
            user_screen()
        if choice == 6:
            sys.exit(0)

def signup_screen():
    check = True
    while check:
      name_check = input("Name: ")
      pass_check = input("Password: ")
      #then checks if court is available
      #if court is not available, add to queue
      for i in people:
          if name_check in people.keys() and pass_check in people.values():
            if len(courts) == 2:
                queue.append(name_check)
                check = False
                home_screen()
            elif len(courts) < 2:
                courts.append(name_check)
                if name_check in queue:
                    queue.remove(name_check)
                check = False
                home_screen()
          else:
            print("Name not found! Please try again!")

def signout_screen():
    check = True
    while check:
        inp_name = input("Name: ")
        inp_pass = input("Password: ")
        for i in courts:
            if inp_name in people.keys() and inp_pass in people.values():
                courts.remove(inp_name)
                check = False
            else:
                print("Name not found! Please try again!")