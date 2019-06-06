username = input("username:")
email = input("email:")
password = input("password:")
while True:
    repass = input("re-enter password:")
    if repass == password:
            print("ok")
            break
    else:
        print("invalid")
       