# encapsulation 
# getter and setter

class chatbook:
    
    __user_id = 0

    
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = "Default User"
        self.username = ""
        self.password = ""
        self.loggedin = False
        #self.menu()
    
    @staticmethod
    def get_id(self):
        return self.__user_id
    
    def set_id(self,value):
        chatbook.__user_id = value   

    def menu(self):
        user_input = input("""Welcome to Chatbook!!, How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           ->""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.mypost()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter your email here ->")
        pwd = input("Setup your password here ->")
        self.username = email
        self.password = pwd
        print("You have signedup successfully!!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print('Please signup first by pressing 1 in the main menu')
        else:
            uname = input("enter your email/password here ->")
            pwd = input ("enter your password here ->")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully") 
                self.loggedin = True
            else:
                print("Please enter the correct credentials")
        print("\n")
        self.menu()

    def mypost(self):
        if self.loggedin == True:
            txt = input("Enter your message here ->")
            print(f"Following content has been posted -> {txt}")
        else:
            print("You need to signin first to post something!!")

        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here ->")
            friend = input("Whom to send the message? ->")
            print(f"Your message has been sent to {friend}")
        else:
            print("You need to signin first to send message!!")
        print("\n")
        self.menu()

