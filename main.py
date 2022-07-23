def submit():
    global info
    user = input("user: ")
    passw = input("pass: ")
    cpassw= input("pass again: ")
    if(user in info):
        print("username already exist")
        return
    elif(len(passw)<4):
        print("password length error")
        return
    elif(passw!=cpassw):
        print("pass error!!")
        return
    else:
        info[user]=passw
        print("submit done!!")
    print(info)
def login():
    global info
    user = input("user: ")
    passw = input("pass: ")
    if((user in info) and (info[user]==passw)):
        print("welcome your page")
    else:
        print("wrong user or pass")
def delete():
    global info
    user = input("user: ")
    passw = input("pass: ")
    #key=False
    if ((user in info) and (info[user] == passw)):
        confirm = input("are you sure? [yes/no] ")
        if(confirm=="yes"):
            info.pop(user)
            print("deleted your account")
        else:
            print("canceled by user")
            return
    else:
        print("wrong pass or user")


info={}
while(True):
    choice=input("enter your plan: ")
    if(choice=="submit"):
        submit()
    elif(choice=="login"):
        login()
    elif(choice=="delete"):
        delete()
    elif(choice=="exit"):
        break
    else:
        print("wrong input")