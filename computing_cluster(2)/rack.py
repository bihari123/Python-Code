from node import Node
class Rack:
	def __init__(self):
		self.liste_av_rack = list()  #liste_av_rack  = list_of_rack

	def add(self, node):
		self.liste_av_rack.append(node)


	def erFull(self): #erFull=isFull
		return len(self.liste_av_rack)

	def antProsessorer(self): #antProsessorer = processorNumber
		antall_prosessorer = 0
		for i in self.liste_av_rack:
			antall_prosessorer += i.antProsessorer()
		return antall_prosessorer

	def noderMedNokMinne(self, paakrevdMinne):
		antall_noder = 0 #antall_noder= numberOf_nodes
		for i in self.liste_av_rack:
			if i.nokMinne(paakrevdMinne):
				antall_noder += 1
		return antall_noder
