#Search for names present in the list eg. Say list of strings has Vivek Rao,VishaL Rao,Vishwas Pandit,Vivek Bhatt,Vishal Chopra,Vishwas Mukherjee,Pratheep Kumar,Pratheep Nadar,Pranab Mukherjee,Siddharth Singh,Siddharth Malhotra,Siddhanth Singh,Siddesh Chopra,Raj Sanghavi,Rajesh Sanghavi,Raj Chopra
names=[] #Empty list initially...later appended with user input strings or name
x=1
while x==1:
    name=input('\nEnter name in the list : ')
    name=name.lower().strip() #Converting to lowercase and stripping off whitespaces
    namelst=name.split() #Lines 7 and 8 of code is added to prevent extra spaces that user might enter sometimes in between the sentence eg. user enters name as Vivek   Rao although it should be entered as Vivek Rao - so it takes care of that.
    name=' '.join(namelst) #Joining elements of the list with space between them.
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
    search=search.lower().strip()
    searchlst=search.split() #This is done so that if someone searches eg. vivek  rao...note there are two extra spaces here but in the list there will be just vivek rao and hence searched entry will not match with one in the list hence splitting
    search=' '.join(searchlst) # So even if you search Vivek     Rao or Vivek Rao or Vivek      Rao...it's gonna split them into Vivek and Rao and join them with a single space so that it is Vivek Rao    
    print('\nMatching Results : \n')
    count=0
    for name in names: #Compares the searched initials with each name in the list
        if name.startswith(search): #Object Method - String Method checks if name string starts with the searched name - yes then gives the search results
            print(name) 
        else:
            count=count+1 #keeps a count of the names in which search initials were not present
    if count==len(names): #incase if search initials were not present in all names in the list, then prints the no matching results message
        print('OOPS! No Matching Results\n')
