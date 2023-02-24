#SOURCE CODE
print(''' MENU
1.STACK
2.QUEUE''')
l=[]
import  time as t
ch='y'
while ch=='y':
    l.append(input('Enter the item:'))
    ch=input('Do you want to enter(y/n):')
    if ch!='y':
        break
c=int(input('Enter the choice(1/2):'))
if c==1:#stacks
    print('Performing stack')
    t.sleep(1)
    print('existing contents in the list ...')
    print(l)
    t.sleep(1)
    print('push a element')
    user=input('Enter the item:')
    l.append(user)
    t.sleep(1)
    print('The updated list is ...')
    print(l)
    t.sleep(1)
    print('poping an element out...')
    if len(l)!=0:
        print(l.pop(-1))
        print('The updated list is :',l)
    else:
        print('stack empty')
elif c==2:#queue
    print('performing queue...')
    print('Existing contents in the list .... ')
    print(l)
    t.sleep(1)
    print('push a element')
    user=input('Enter the item:')
    l.append(user)
    t.sleep(1)
    print('The updated list is ...')
    print(l)
    t.sleep(1)
    print('poping an element out...')
    if len(l)!=0:
        print(l.pop(0))
        print('The updated list is :',l)
    else:
        print('stack empty')
