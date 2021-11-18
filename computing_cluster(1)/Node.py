class Node:
    def __init__(self,mem_size,pro_num):
        self.mem_size=mem_size #memory size
        self.pro_num=pro_num   # number of processors

    # defining getters for returning the value of number of processors and
    #memory size
    def get_processor_num(self):
        return self.pro_num 

    def get_mem_size(self):
        return self.mem_size
