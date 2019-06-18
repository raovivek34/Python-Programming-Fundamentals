#Line,Character,Word Counter - File Version
import string
print('\nWelcome to the File Counter wherein we calculate the number of lines,characters and words in the file.')
while True:
    try:
        filename=input('\nEnter the name of the file to be read : ') #Remember if we want information like name,age and other info, we can use strings, but if lot of text required then better to use files.
        filename=filename.strip()
        fhand=open(filename,'r') #Whenever we deal with files (flat text file .txt) we first find the file handle (sequence of lines) with open(filename,mode)
        break
    except:
        print('\n\nThe filename you entered does not exist. Try again by entering the right filename')
        continue
linecount=0
charactercount=0
wordcount=0
print('\nReading the file.....\n\n')
for line in fhand: #Goes through every line in the file - through filehandle which is sequence of lines
    linecount=linecount+1 #Line Counter
    line=line.rstrip() #Strips off whitespace...also the \n in files are treated as whitespaces
    charactercount=charactercount+len(line) #Character Counter
    currentline=line.split()
    for word in line.split(): #Nested for loops to check whether atleast a single letter - uppercase or lowercase or number should be present to be counted as a word...only if special characters are present,it can't be counted as a word
        count=0
        for character in string.ascii_letters+string.digits: #string.ascii_letters and string.digits are string constants which are all letters(lowercase and uppercase) and numbers respectively
            if character in word: #if either the letters - lowercase as well as uppercase or number present then counted as word
                break
            else: #but if letters or numbers not present then a count is kept and 62 count depicts that not a single letter or number present hence it isn't counted as a word
                count=count+1
                continue
        if count==62:
            currentline.remove(word) #if it isn't counted as a word then remove it from the currentline list so that the count is not kept.
            continue
        else:
            continue
    wordcount=wordcount+len(currentline) #Word Counter
    print(line)
print('\n\nThe number of lines is',linecount)
print('\nThe number of characters is',charactercount)
print('\nThe number of words is',wordcount)
#Note - The line count and the character count is fairly easy - just go through every line in the file and keep a count of the number of lines and characters through each line.
#Note - But for the word counter, logic used is slightly different because if suppose sentence is -- Hey @ this is Vivek 123 . -- Here there are 5 words - Hey,this,is,Vivek,123 ... @ isn't counted a word as there is not a single letter or number accompanying it.
#Note - Hence for word count, went through each line of the file, splitted it for every element in the line and checked if any letter(lowercase and uppercase) or number is present -- if nothing is present that is all 62 (letters plus numbers) count is kept of nothing present then it is not treated as a word and hence for the count that element is removed from the list.
