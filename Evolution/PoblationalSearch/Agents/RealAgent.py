from random import random, gauss
from .Agent import Agent

class RealAgent(Agent):

	def init(self, size, _min=0, _max=1, exogenous=False):
		self.genome = [random()*(_max - _min) + _min for _ in range(size)]
		if exogenous:
			self.exogenous = self.init_exogenous()

	def evaluate(self, function):
		if self.fitness is None:
			self.fitness = function(self.genome)

	def mutate(self, sigma=0.1, rate=-1):
		if rate < 0:
			rate = 1/len(self.genome)
		for i in range(len(self.genome)):
			if random() < rate:
				self.genome[i] = gauss(self.genome[i], sigma)
		
	def init_exogenous(self):
		return [random() for _ in range(len(self.genome))]
	
	def mutate_exogenous(self):
		self.exogenous = [gauss(ex, ex) for ex in self.exogenous]
		for i in range(len(self.genome)):
			self.genome[i] = gauss(self.genome[i], self.exogenous[i])
		
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def __str__(self):
		S = ''
		ft = '{:0.4f} '
		for value in self.genome:
			S += ft.format(value)
		return S + '| ' + ft.format(self.fitness)