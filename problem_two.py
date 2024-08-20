class login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self,id,pas):
        if(self.id == id and self.pas == pas):
            print ("Login success!")
        else:
            print("Error: Login failed!")

log = login("admin", "admin")
log.check(input("Enter Login ID:"), input("Enter password: "))

#print("Login Page") 
