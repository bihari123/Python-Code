#Repetition1.py
# Author: Waleed Nasir



# Comment: The function slaaSamen is a user-defined function used to
# join two strings
# input: string1, string2
# output: string1+string2

def slaaSamen(str1,str2):
    return str1+str2;

# the procedure writeUt prints the items in a list
#input: a list (say aList)
# output: prints all the items one by one
def writeUt(aList):
    for item in aList:
        print (item)

# declaring an empty list mineOrd
mineOrd=list()

# Using some print statements for good presentation
print("Welcome to Repetition1. Follow the instructions below to proceed")



# Loop run as long as user wants.
#normally while loop is defined as follow
# while( condition to be tested)
# but here we have placed 1 in place
# of condition because we want it to run for
# an indefinite number of times
# here 1 means same as in digital electronics
# it means true
while (1):
    x=input("Enter \n i for joining two strings \n u to display the contents of the list mineOrd \n s to exit\n")
    # in the above statement \n character is used to bring new line so that the presentation looks clean
    if x=='i':
        y=input("Enter the first string")
        z=input("Enter the second string")
        mineOrd.append(slaaSamen(y,z))# append method is used to add an element to the string
    elif x=='u':
        writeUt(mineOrd)
    elif x=='s': # if the user has entered s break from the loop or exit
        print("You have exit the program")
        break
    else:
        print("Please enter a valid value")
