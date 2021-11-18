class Celle:
    def __init__(self,status="dead"): # default status is dead
        self.status=status

    def setDoed(self):
        self.status="dead"

    def setLevende(self):
        self.status="living"

    def erLevende(self):
        if (self.status == "living"):
            return True
        else:
            return False

    def char_represent(self):
        if ( self.status == "living"):
            character="O" #representation of living cell
        elif(self.status == "dead"):
            character="." #representation of dead cell

        return character    
        
