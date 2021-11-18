
from node import Node
from rack import Rack

class Regneklynge:  # class ComputerCluster

	def __init__(self, noder_per_rack): #nodes_per_rack
		self.regneklynge = list()  #regneklynge = computercluster
		self.noder_per_rack = noder_per_rack
		self.antall_rack = 0 

	def addNode(self, node):
		if self.num_antall_racks() == 0: 
			self.regneklynge.append(Rack())

			self.regneklynge[self.antall_rack].add(node)  #antall / ant = number of
		elif (self.regneklynge[self.antall_rack].erFull()) >= self.noder_per_rack: 
			self.antall_rack += 1 
			self.regneklynge.append(Rack())  
			self.regneklynge[self.antall_rack].add(node) 
		else:
			self.regneklynge[self.antall_rack].add(node)

	def antProsessorer(self): 
		total_antall_prosessorer = 0
		for i in self.regneklynge: 
			total_antall_prosessorer += i.antProsessorer() 
		return total_antall_prosessorer

	def noderMedNokMinne(self, paakrevdMinne):  
		total_antall = 0
		for i in self.regneklynge:
			total_antall += i.noderMedNokMinne(paakrevdMinne) #noderMedNokMinne=nodesWithEnoughMemory
		return total_antall

	def num_antall_racks(self):
		return len(self.regneklynge)
