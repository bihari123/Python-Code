from Node import Node
from Rack import Rack

class Computing_cluster:

    def __init__(self,nodes_per_rack):
        self.nodes_per_rack=nodes_per_rack
        self.list_end=0
        self.list_of_racks=list() # list for storing rack objects

    # getter for returning the number of racks
    def num_of_racks(self):
        return len(self.list_of_racks)

    # function for adding the node
    def addNode(self,b):
        #if there is no element in the list_of_racks list()
        if (len(self.list_of_racks) == 0):
            #insert a new Rack object into the list
            self.list_of_racks.append(Rack(self.nodes_per_rack))
            # insert the node into that Rack object.
            #remember we have created Rack object to save node
            # in a list, we have defined the insertNode method
            # in class Rack
            self.list_of_racks[self.list_end].insertNode(b)
        elif (self.list_of_racks[self.list_end].isFull()): # if the list is full
            # increment the last index of list
            # this helps in creating a new element in the list_of_racks list
            # to store the Node object
            self.list_end=self.list_end+1
            self.list_of_racks.append(Rack(self.nodes_per_rack))
            self.list_of_racks[self.list_end].insertNode(b)
        else:
            # if there is still space available in the current list
            # store in that list
            self.list_of_racks[self.list_end].insertNode(b)

    # method for returning the number of nodes with minimum given memory        
    def moderMedNokMinne(self,paakrevdMinne):
        num_of_nodes=0
        # we compare the memory size of every Node saved
        # now note, Node is saved into list Rack
        # list Rack is in turn saved into list list_of_racks
        # this means it is a 2D list
        for i in range(len(self.list_of_racks)):
            for j in range(len(self.list_of_racks[i].rack)):
                if(self.list_of_racks[i].rack[j].get_mem_size() >= paakrevdMinne):
                    num_of_nodes=num_of_nodes+1

        return num_of_nodes            
    # method for returning the number of processors
    # number of processors is equal to
    # number of nodes X processors per node
    def antProsessor(self):
        sum_of_processors=0
        for i in range(len(self.list_of_racks)):
            for j in range(len(self.list_of_racks[i].rack)):
                sum_of_processors=sum_of_processors + self.list_of_racks[i].rack[j].get_processor_num()

        return sum_of_processors        
