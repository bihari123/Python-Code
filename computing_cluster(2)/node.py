class Node: 
    
    def __init__(self,minne_størrelse,prosessor_antall): #minne_størrelse= memory_size, prosessor_antall= processor_number

        self.minne_størrelse=minne_størrelse 

        self.prosessor_antall=prosessor_antall   #antall=number of

    
    def antProsessorer(self):
        return self.prosessor_antall 

    def nokMinne(self, paakrevdMinne):   #paakrevdMinne= requiredMemory
        if paakrevdMinne <= self.minne_størrelse:
            return True

