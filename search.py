#Search for names present in the list eg. Say list of strings has Vivek Rao,VishaL Rao,Vishwas Pandit,Vivek Bhatt,Vishal Chopra,Vishwas Mukherjee,Pratheep Kumar,Pratheep Nadar,Pranab Mukherjee,Siddharth Singh,Siddharth Malhotra,Siddhanth Singh,Siddesh Chopra,Raj Sanghavi,Rajesh Sanghavi,Raj Chopra
names=[] #Empty list initially...later appended with user input strings or name
x=1
while x==1:
    name=input('\nEnter name in the list : ')
    name=name.lower() #Converting to lowercase
    names.append(name)
    while True:
        choice=input('\nDo you want to enter more names.\n\nEnter 1 for yes and 2 for no.\n')
        if choice=='1':
            break
        elif choice=='2':
            x=0
            break
        else:
            print('You have made a wrong choice. Please choose again.\n')
            continue
print('\nYour list of names looks like this --',names)
print('\nThere are a total of',len(names),'names in the list')
while True:
    search=input('\nSearch a name from the list. Type in the name here - : ') #Asking user to search for names in the list by typing the initial letters eg. viv will give vivek rao and vivek bhatt
    search=search.lower()
    print('\nMatching Results : \n')
    count=0
    for i in names: #Compares the searched initials with each name in the list
        if search in i[0:len(search)]:
            print(i) #Gives the search results if it is present in the name
        else:
            count=count+1 #keeps a count of the names in which search initials were not present
    if count==len(names): #incase if search initials were not present in all names in the list, then prints the no matching results message
        print('OOPS! No Matching Results\n')
