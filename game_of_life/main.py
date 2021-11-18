from spillebrett import GameBoard
from celle import Celle
def main():
    x=' ' 
    b=GameBoard(10,10)
    # printing initial board
    b.tegnBrett()
    print("the number of living cells are ",end=" ")
    print(b.finnAntallLevende())
    while(x!='q'):
        x=input("Enter to continue \n Press q to exit")
        b.oppdatering()
        b.tegnBrett()
        print("the number of living cells are ",end=" ")
        print(b.finnAntallLevende())



if __name__== "__main__":
  main()
            
