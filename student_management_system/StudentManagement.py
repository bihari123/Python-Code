# importing classes from other files
from EncodeDecodeClass import EncodeDecodeClass
from StudentRecordClass import StudentRecordClass

# defining the main function        
def main():
    #defining a StudentRecordClass object
    a=StudentRecordClass()
    # prompting the user
    ip1=input(" Would you like to enter a student\'s information ? Enter Y or y for yes and N or n for no \n")
    # keep asking until no
    while ip1 == 'Y' or ip1 == 'y':
        a.WriteInfo()
        ip1=input(" Would you like to enter a student\'s information ? Enter Y or y for yes and N or n for no \n")


    
        
    if ip1 == 'N' or ip1 == 'n':    
        
        ip2=input(" 1.Would you like to see a list of all registered students? \n 2.Would you like to see a class list for specific subject? \n 3. Would you like to see who your oldest student is? \n 4. Would you like to see who your youngest student is ? \n Enter the number for the selected task, or X to skip this : \n")
        #keep asking until "x"
        while(not (ip2 == 'X' or ip2 == 'x')):
         
            if ip2 == '1':
                a.DisplayStudents()

            elif ip2 == '2':
                subject_name= input("which subject class details do you want ? \n ")
                a.DisplaySubjectClassList(subject_name)

            elif ip2 == '3':
                a.DisplayOldest()
            elif ip2 == '4':    
                a.DisplayYoungest()


            ip2=input(" 1.Would you like to see a list of all registered students? \n 2.Would you like to see a class list for specific subject? \n 3. Would you like to see who your oldest student is? \n 4. Would you like to see who your youngest student is ? \n Enter the number for the selected task, or X to skip this : \n")
        


        if (ip2 == 'X' or ip2 == 'x'):
            ip3= input("Would you like to encrypt the file? \n Press Y or y for yes and N or n for no \n")
            b=EncodeDecodeClass()  # defining a EncodeDecodeClass object
            if(ip3 == 'y' or ip3 == 'Y'):
                b.EncodeStudentsList()
                
            elif(ip3 == 'n' or ip3 == 'N'):
                ip4=input("Would you like to decode the file")
                if(ip4 == 'y' or ip4 == 'Y'):
                    b.DecodeStudentsList()
                else:
                    print("Assignment over, have a nice day") # bye
                
            

if __name__ == '__main__':  
    main()    #calling the main function
        
