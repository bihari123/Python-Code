class StudentRecordClass:
    # constructor
    def __init__(self,fodselNummer ='',firstName ='',lastName = '',age = '',email='',programmingCourse =''):
        self.fodselNummer=fodselNummer
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.email=email
        self.programmingCourse=programmingCourse
         

    def WriteInfo(self,fileName="StudentRecord.txt"):  # for writing the info to file
        try:
            data=open(fileName,'a+')  # opening data file
            fodselNumber=input('Enter the fodsel number of the student') # prompting the user
            fname= input(' Enter the first name ')
            lname=input('Enter the last name ')
            age=input('Enter the age')
            email=input('Enter the email')
            pcourse=input('Enter the programming course')
            # error handling, in case the file could not be created   
            try:
                student_info=str(fodselNumber)+","+str(fname)+","+str(lname)+","+str(age)+","+str(email)+","+str(pcourse)+"\n"
                # ensuring that the data is in valid format
                if(fodselNumber.isnumeric() and age.isnumeric() and  (not fname == " ") and (not email == " ") and (not pcourse == " ")):
                    data.write(str(student_info))
                else:
                    print("Please enter valid details \n")
                    
            except :
                print("Ooops something is buggy \n")
                
        except IOError:  
             print("the file \'StudentRecord.txt\' could not be created \n")

        finally:
             data.close() # close the file in the end



        
    def DisplayStudents(self,fileName="StudentRecord.txt"):
        student_list=[]
        # check whether the file exists or not
        try:
            data=open(fileName,'r')
            for each_line in data:
                try:
                    a=StudentRecordClass()
                    (a.fodselNummer,a.firstName,a.lastName,a.age,a.email,a.programmingCourse) =each_line.split(",")          
                    student_list.append(str(a.firstName)+" "+str(a.lastName))
                   
                except:
                    pass


            for x in range(len(student_list)):
                print(student_list[x],sep="\n")


        except IOError:
             print("the file \'StudentRecord.txt\' doesn\'t exist")


        finally:
             data.close()


    def DisplaySubjectClassList(self,subjectName,fileName= "StudentRecord.txt"):
        subject_class_list=[]
        # check whether the file exists or not
        try:
            data=open(fileName,'r')
            for each_line in data:
                try:
                    if not each_line.find(str(subjectName)) == -1:  # finding the entries matching subject name
                        a=StudentRecordClass()
                        (a.fodselNummer,a.firstName,a.lastName,a.age,a.email,a.programmingCourse) =each_line.split(",")          
                        subject_class_list.append(str(a.firstName)+" "+str(a.lastName))
                   
                except:
                    pass
            print("The students registered for subject " + subjectName + " are")
            for x in range(len(subject_class_list)):
                print(subject_class_list[x],sep="\n")  # printing th name of the student


        except IOError:
             print("the file \'StudentRecord.txt\' doesn\'t exist")


        finally:
             data.close()


    def DisplayOldest(self,fileName="StudentRecord.txt"):
        max_age=0
        student_list=[]
        oldest=[]
        try:
            data=open(fileName,'r')
            for each_line in data:
                try:
                    
                    a=StudentRecordClass()
                    (a.fodselNummer,a.firstName,a.lastName,a.age,a.email,a.programmingCourse) =each_line.split(",")          

                    student_list.append(a) # make a list of the students while reading from the file
                except:
                    pass


        except IOError:
             print("the file \'StudentRecord.txt\' doesn\'t exist")


        finally:
             data.close()        
        
        # now compare their ages 
        for i in range(len(student_list)):
            if(int(student_list[i].age)>max_age):
                if not len(oldest)>1 :
                    del oldest[:]


                oldest.append(i)
                max_age=int (student_list[i].age)
                 
            elif(int(student_list[i].age)==max_age):
                    oldest.append(i)

            
                
  

        print("The oldest student is ")
        for j in range(len(oldest)):
           print(str(student_list[oldest[j]].firstName)+" "+str(student_list[oldest[j]].lastName) + " at age " + str(student_list[oldest[j]].age))


    def DisplayYoungest(self,fileName="StudentRecord.txt"):
        min_age=100
        student_list=[]
        youngest=[]
        try:
            data=open(fileName,'r')
            for each_line in data:
                try:
                    
                    a=StudentRecordClass()
                    (a.fodselNummer,a.firstName,a.lastName,a.age,a.email,a.programmingCourse) =each_line.split(",")          

                    student_list.append(a)
                except:
                    pass


        except IOError:
             print("the file \'StudentRecord.txt\' doesn\'t exist")


        finally:
             data.close()        
        

        for i in range(len(student_list)):
            if(int(student_list[i].age)<min_age):
                if not len(youngest)>1 :
                    del youngest[:]


                youngest.append(i)
                min_age=int (student_list[i].age)
                 
            elif(int(student_list[i].age)==min_age):
                    youngest.append(i)

            
                
  

        print("The youngest student is ")
        for j in range(len(youngest)):
           print(str(student_list[youngest[j]].firstName)+" "+str(student_list[youngest[j]].lastName) + " at age " + str(student_list[youngest[j]].age))



