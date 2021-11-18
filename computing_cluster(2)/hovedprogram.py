

from regneklynge import Regneklynge
from node import Node
from rack import Rack


def hovedprogram(): 
    abel = Regneklynge(12) 



    for i in range(650):
        abel.addNode(Node(64,1))


 
    for i in range(16):
        abel.addNode(Node(1024,2))



 

    print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
    print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
    print("Noder med minst 128 GB:", abel.noderMedNokMinne(128))
    print("Antall prosessorer:", abel.antProsessorer())
    print("Antall rack:", abel.num_antall_racks())

hovedprogram()  
