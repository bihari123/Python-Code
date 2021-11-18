
class Rack:

    def __init__(self,max_processors):
        self.rack=list() # list for storing the nodes
        self.max_processors=max_processors # max number of nodes in a rack
    # tresting if the rack is full or not 
    def isFull(self):
        if (len(self.rack) == self.max_processors):
            return True
        else:
            return False
    # inserting a node to list rack
    def insertNode(self,b):
        self.rack.append(b)
        
