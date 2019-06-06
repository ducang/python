while True:
        username = input("enter ur username:")
        while True:
                email = input("enter ur email:")
                if '@' and '.com' in email:
                        if ' ' in email:
                                print('invalid')
                        else:
                                break
                else:
                        print('invalid')
        while True:
                password = input("enter ur password:")
                if password.isdigit():
                        print("not strong enough re-enter")
                elif password.isalpha():
                        print("not strong enough re-enter")
                elif len(password)<8:
                        print('not strong enough re-enter') 
                else:
                        break 
        while True:                             
                repass = input("re-enter ur password:")
                if repass == password:
                        break
                else:
                        print('invalid')

        