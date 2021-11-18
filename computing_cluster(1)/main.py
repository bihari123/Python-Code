from computingCluster import Computing_cluster
from Node import Node
from Rack import Rack

def main():
    abel= Computing_cluster(12)
    for i in range(650):
        abel.addNode(Node(64,1))

    for j in range(16):
        abel.addNode(Node(1024,2))

    print("nodes with atleast 32 GB memory: "+str(abel.moderMedNokMinne(32)))
    print("nodes with atleast 64 GB memory: "+str(abel.moderMedNokMinne(64)))
    print("nodes with atleast 128 GB memory: "+str(abel.moderMedNokMinne(128)))
    print("number of processoers: "+str(abel.antProsessor()))
    print("number of racks: "+str(abel.num_of_racks()))

if __name__=="__main__":
    main()
        
