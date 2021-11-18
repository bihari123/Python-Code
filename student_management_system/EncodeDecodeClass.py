class EncodeDecodeClass:
    def __init_(self):
        pass

    
    def EncodeStudentsList(self,fileName1 = "StudentRecord.txt", fileName2= "EncodedStudentRecord.txt"):
        my_list=[]
        count=0
        lines_read=0
        lines_write=0
        try:
            data1=open(fileName1,'r') # file to read
            data2=open(fileName2,"a+") # file to write the encoded data

            lines_read = self.lines_count(fileName1) # no of lines in the original file
            lines_write=self.lines_count(fileName2)  # no of lines already written in the encoded file

            for each_line in data1:
                if lines_read >= lines_write:  # only encode the new entries in the original file
                    count+=1
                    # do not touch the entries that are already encoded
                    if count> lines_write:   # encoding the new entries
                        # splliting the line by a comma and retrieving the values
                        (fodselNumber,firstName,lastName,age,email,programmingCourse) =each_line.split(",")

                        enc_fodselNumber=self.encodeText(fodselNumber)
                        enc_firstName=self.encodeText(firstName)
                        enc_lastName=self.encodeText(lastName)
                        enc_age=self.encodeText(age)
                        enc_email=self.encodeText(email)
                        enc_programmingCourse=self.encodeText(programmingCourse)
                        # preparing an encoded text
                        encodedText=str(enc_fodselNumber)+","+str(enc_firstName)+","+str(enc_lastName)+","+str(enc_age)+","+str(enc_email)+","+str(enc_programmingCourse)+"\n"
                        # write encoded data to the file
                        data2.write(str(encodedText))
                    else:
                        continue
            print("File encrypted")
            
        except IOError:
            print("the file \'StudentRecord.txt\' doesn\'t exist")

        finally:
            data1.close()
            data2.close()


    def encodeText(self,text):
        result=" "
        if(text.isnumeric()): # for encoding the numbers
            result=self.swap_first_last(text) # this functions swaps the first and the last digit
        else:    # for encoding the text
            for elem in text: 
                if (elem >= 'a' and elem <='z') or (elem >='A' and elem <= 'Z'):
                    result=result+self.shiftCipher(elem)
                elif (elem == "@" or elem == '.'):
                    result= result + elem


        return result

    def lines_count(self, file):  # counting the lines
        count =0
        try:
            data = open(file , "r")  # reading the file
            for each_line in data:
                count +=1            # counting the lines

        except:
            pass
        finally:
            data.close()              # close the file at the end
        return count

    def swap_first_last(self,text):
        list1=list(text)
        list1[0], list1[-1] = list1[-1], list1[0]   # swap the first and the last digit
        return ''.join(list1)                       # join the parts as last + rest of the num + fist
        


    def shiftCipher(self, ch):
        # prepare a list of alphabets in both the cases
        list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        for i in range(len(list1)):
            if list1[i] == ch:    # check for the position of the character, if it is lowercase
                if i+5 <=25:
                    return list1[i+5]   # shift the char by 5 places
                else:
                    return list1[(i+5)-26]  # if reached the end, then rotate
            elif list2[i] == ch:   # check for the position of the character, if it is uppercase    
                if i+5 <=25:
                    return list2[i+5]
                else:
                    return list2[(i+5)-26]
            



    def DecodeStudentsList(self,fileName1 = "EncodedStudentRecord.txt", fileName2= "DecodedStudentRecord.txt"):
        my_list=[]        
        count=0
        lines_read=0
        lines_write=0
        try:
            data1=open(fileName1,'r')
            data2=open(fileName2,"a+")

            lines_read = self.lines_count(fileName1)
            lines_write=self.lines_count(fileName2)

            for each_line in data1:   
                if lines_read >= lines_write:
                    count+=1
                    if count> lines_write:
                        (enc_fodselNumber,enc_firstName,enc_lastName,enc_age,enc_email,enc_programmingCourse) =each_line.split(",")
                        # decoding the text part by part  
                        dec_fodselNumber=self.decodeText(enc_fodselNumber)
                        dec_firstName=self.decodeText(enc_firstName)
                        dec_lastName=self.decodeText(enc_lastName)
                        dec_age=self.decodeText(enc_age)
                        dec_email=self.decodeText(enc_email)
                        dec_programmingCourse=self.decodeText(enc_programmingCourse)
                        # joining the decoded text
                        decodedText=str(dec_fodselNumber)+","+str(dec_firstName)+","+str(dec_lastName)+","+str(dec_age)+","+str(dec_email)+","+str(dec_programmingCourse)+"\n"
                        # write the decoded data
                        data2.write(str(decodedText))
                    else:
                        continue

            print("File decoded")
            
        except IOError:
            print("the file \'EncodedStudentRecord.txt\' doesn\'t exist")

        finally:
            data1.close()
            data2.close()






    def decodeText(self,encoded_text):
        result=" "
        if(encoded_text.isnumeric()):  # decoding the number
            result=self.swap_first_last(encoded_text)
        else:       # decoding the text
            for elem in encoded_text:
                if (elem >= 'a' and elem <='z') or (elem >='A' and elem <= 'Z'):
                    result=result+self.deCipher(elem)
                elif (elem == "@" or elem == '.'):
                    result= result + elem


        return result


    def deCipher ( self,ch):
        list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

        for i in range(len(list1)):
            if list1[i] == ch:
                return list1[i-5] #shifting the char by 5 places in reverse direction
            elif list2[i] == ch:
                return list2[i-5]
               
