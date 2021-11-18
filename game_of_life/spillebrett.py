from random import randint
from celle import Celle

class GameBoard:

    def __init__(self,rader,kolonner):
        self.rader=rader
        self.kolonner=kolonner
        self.a = [[None for _ in range(kolonner)] for _ in range(rader)]
       
        # building the 2 D board with objects Celle()
        for i in range(self.rader):
            for j in range(self.kolonner):
                self.a[i][j]=Celle()
       
        self.generer() # calling generer method from constructor
        self.generation_number=0


    def generer(self):
         for i in range(self.rader):
             for j in range(self.kolonner):
                 k=randint(1,3)# randomly making the cells alive
                 if (k == 2):
                     self.a[i][j].setLevende()
        
                     
                         
                 
    def tegnBrett(self):
         # printing some blank lines 
         for k in range(5):
            print("")
         # printing the 2D board   
         for i in range(self.rader):
             for j in range(self.kolonner):
                 print(self.a[i][j].char_represent(), end=' ')
                
             print()

    # function forn storing the neighbors in a list 
    def finnNabo(self,row,col):
        i=0
        neighbor=list()
        if(row > 0 and col > 0):
            neighbor.insert(i,self.a[row-1][col-1])
            i=i+1
        if(row > 0):
            neighbor.insert(i,self.a[row-1][col])
            i=i+1
        if(row > 0 and col < self.kolonner-1):
            neighbor.insert(i,self.a[row-1][col+1])
            i=i+1
        if(col > 0):
            neighbor.insert(i,self.a[row][col-1])
            i=i+1
            if(row < self.rader-1):
                neighbor.insert(i,self.a[row+1][col-1])
                i=i+1
        
        
        if(col < self.kolonner-1):        
            neighbor.insert(i,self.a[row][col+1])
            i=i+1
        if(row < self.rader-1):
            neighbor.insert(i,self.a[row+1][col])
            i=i+1

        if(row <self.rader-1 and col < self.rader-1):
            neighbor.insert(i,self.a[row+1][col+1])
            
            

        return neighbor # returning the list of neighbors

    # function for updating the status of the cells
    def oppdatering(self):
        will_be_dead=list() # to store the cells which will die
        will_be_alive=list()# to store the cells which will come alive
        dead_count=0
        liv_count=0
        for i in range(self.rader):
            for j in range(self.kolonner):
                
                if(self.a[i][j].erLevende()): # check if the cell is alive
                    count1=0;
                    for k in range(len(self.finnNabo(i,j))):
                    
                        if(self.finnNabo(i,j)[k].erLevende()): # checking the number of alive neighbors
                            count1=count1 + 1
                        else:
                            pass

                        
                    if(count1 > 3 or count1 < 2): # if more than 3 or less than 2 neighbors are alive
                        will_be_dead.insert(dead_count,self.a[i][j]) # the cell has to die
                        dead_count=dead_count+1
                   
                    
                else:
                    count2=0;
                    for n in range(len(self.finnNabo(i,j))):
                      
                        if(self.finnNabo(i,j)[n].erLevende()):# checking the number of alive neighbors
                            count2=count2 + 1
                        else:
                            pass

                    if(count2==3): #if exactly 3 neighbors are alive
                        will_be_alive.insert(liv_count,self.a[i][j])# the cell comes alive
                        liv_count=liv_count+1
                    
        
        for m in range(len(will_be_dead)):
            will_be_dead[m].setDoed(); # updating the status of the3 cells

         
        for x in range(len(will_be_alive)):
            will_be_alive[x].setLevende() # updating the status of the3 cells

        self.generation_number=self.generation_number+1 #incrementing the generation number
        print("Generation ",end=" ")
        print(self.generation_number)



    def finnAntallLevende(self):
        count=0;
        for i in range(self.rader):
            for j in range(self.kolonner):
                if(self.a[i][j].erLevende()):
                    count=count+1    # finding the number of alive cells
                    
        return count
    
                       
