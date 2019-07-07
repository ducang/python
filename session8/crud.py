lis = ['1','2','3']
print(lis)
while True:
    action = input('enter action (C;R;U;D) or Exit:')
    if action == 'C':
        add = input('enter ur number:')
        lis.append(add)
        print('ur list here:',lis)
    elif action == 'R':
        if lis == []:
            print('list has nothing inside')
        else:
            for i in lis:
                print(i)
    elif action == 'U':
        update = input('update ur number:')
        position = int(input('enter the position:')) - 1
        lis[position] = update
        print('new list:',lis)
    elif action == 'exit':
        break
    else:
        delete = input('enter what you want to delete:')
        lis.remove(delete)
        print(lis)
    
    