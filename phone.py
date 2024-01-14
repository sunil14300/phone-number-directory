a="LOVELY PROFESSIONAL UNIVERSITY"

print(a.center(120,' '))

b="PHONE NUMBER DIRECTORY"
print(b.center(120,' '))
c='*'
print(c*150)
ch = ''
while(ch !=4):
    details= {'sanjai':3565656565,
              'dev':6545555546,
              'anujit':54646464,
              'vikas':564464654,
              'ashwini':96656959856,
              'honey':7897984645,
              'vinay':89764584784,
              'adamya':789465464865,
              'ansh':87946486896,
              'shalu':784694986,
              'shreya':987954897,
              'snehasis':4897964615,
              'devdivyanshu':7419696855,
              'sunil':9625591889,
              }
    ch=int(input('''
     PRESS 1 FOR CHECK PHONE NO OF SINGLE STUDENT
     PRESS 2 FOR DISPLAY ALL CONTACTS
     PRESS 3 FOR CHECKING PHONE NUMBER FOR MULTIPLE STUDENT
     PRESS 4 to Exit
     ENTER YOUR CHOICE: '''))
    while ch==1:
        print('CHECK PHONE NO OF SINGLE STUDENT')
        name = input("\t\tEnter the name\t:\t").lower()
        if name in details:
            print("\t\tcontact number\t:\t",details[name])
        else:
            print("\t\t",name, "Not Found in a directory")
        ch = input("\t\tPress x to exit or Enter to continue : ") or int(1)

    if ch==2:
        print('DISPLAY ALL CONTACTS')
        for i in details:
            print(i.capitalize(),":",details[i])
    elif ch==3:
        print('CHECKING PHONE NUMBER FOR MULTIPLE STUDENT')
        a=input('Enter multiple name by giving space: ').split()
        for i in a:
            if i in details:
                print(i,details[i])
            else:
                print(i,"Not Found in a directory")
