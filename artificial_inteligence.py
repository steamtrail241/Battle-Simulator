import Jasons_functions as ja
import log as lo
import random

class AI(object):
	def __init__(self):
		self.size = 0
		self.count = 0
		self.morale = 0
		self.cav = 0
		self.inf = 0
		self.arti = 0
		self.suppresion = 0
		self.organization = 0
		self.defense = 0
		self.position = 0
		self.commands = 0
		self.center = 0
		self.flank = 0
		self.inf_losses = 0
		self.scouting = 20
		self.cav_losses = 0
		self.arti_losses = 0
		self.simtension = 0
		self.player = self.friendlyVars()
		self.seeplayer = self.friendlyVars()
		# simulated variables
		self.size1 = 0
		self.cout1 = 0
		self.morale1 = 0
		self.cav1 = 0
		self.inf1 = 0
		self.arti1 = 0
		self.suppresion1 = 0
		self.organization1 = 0
		self.defense1 = 0
		self.position1 = 0
		self.commands1 = 0
		self.center1 = 0
		self.flank1 = 0
		
	def originalset(self, max):
		nf = round(max * 0.32)
		ten = round(max-(nf*3))
		smth = 0
		while smth != max:
			self.cav = nf + random.randint(1, ten)
			self.inf = nf + random.randint(1, ten)
			self.arti = nf + random.randint(1, ten)
			smth = self.cav + self.inf + self.arti
			# print(smth)
		print(self.cav)
		print(self.inf)
		print(self.arti)
	
	def setrandom(self):
		self.scouting = random.randint(1,20)

	def setvars(self):
		self.seeplayer.count = self.afunc(self.player.count, self.scouting)
		self.seeplayer.morale = self.afunc(self.player.count, self.scouting)
		self.seeplayer.suppresion = self.afunc(self.player.suppresion, self.scouting)
		self.seeplayer.organization = self.afunc(self.player.organization, self.scouting)
		self.seeplayer.cav = self.afunc(self.player.cav, self.scouting)
		self.seeplayer.cav_losses = self.afunc(self.player.cav_losses, self.scouting)
		self.seeplayer.inf =self.afunc(self.player.inf, self.scouting)
		self.seeplayer.inf_losses = self.afunc(self.player.inf_losses, self.scouting)
		self.seeplayer.arti = self.afunc(self.player.arti, self.scouting)
		self.seeplayer.arti_losses = self.afunc(self.player.arti_losses, self.scouting)
		self.seeplayer.scouting = self.afunc(self.player.scouting, self.scouting)
		self.seeplayer.position = self.afunc(self.player.position, self.scouting)
		self.seeplayer.defense = self.afunc(self.player.defense, self.scouting)
		self.seeplayer.commands = self.afunc(self.player.commands, self.scouting)
		self.seeplayer.damage = self.afunc(self.player.damage, self.scouting)
		lo.ws("What AI sees", [self.seeplayer.count, self.seeplayer.morale, self.seeplayer.suppresion, self.seeplayer.organization, self.seeplayer.cav, self.seeplayer.inf, self.seeplayer.arti, self.seeplayer.scouting, self.seeplayer.position, self.seeplayer.defense, self.seeplayer.commands, self.seeplayer.damage])
		lo.ws("AI scouting", [self.scouting])

	def afunc(self, othervar, howmuch):
		c1 = False
		avar = 0
		while c1 is False:
			tf_up = random.randint(1,2)
			if tf_up == 1:
				avar = othervar + random.randint(round((-0.155 * self.scouting) + 5), round((-0.5*self.scouting)+17))
			else:
				avar = othervar - random.randint(round((-0.155 * self.scouting) + 5), round((-0.5*self.scouting)+17))
			if avar>0:
				return round(avar)
	
	def simp1b(self,Command_num):
		if Command_num == 1:
			Rand_num = random.randint(1, 3)
			self.defense1 += Rand_num
		# =============================================================================
		elif Command_num == 2:
			Rand_num = random.randint(1, 5)
			self.commands1 += Rand_num - 2
		# =============================================================================
		elif Command_num == 3:
			print("not done")
			Rand_num = random.randint(1, 3)
			self.morale += Rand_num * 2
			self.organization1 += Rand_num - 5
		# =============================================================================
		elif Command_num == 4:
			Rand_num = random.randint(1, 4)
			self.simtension += 2
			self.scouting1 += Rand_num
			if self.scouting1 >20:
				self.scouting1 = 20
		# =============================================================================
		elif Command_num == 5:
			Rand_num = random.randint(2, 3)
			self.position1 += Rand_num
			self.simtension1 += 5
		# =============================================================================
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			# yo rony why didn't the terminal run???
			self.simtension += 8
			self.position1 += Rand_num * 2
			self.morale1 += Rand_num - 5
		# =============================================================================
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			self.morale1 += Rand_num + 1
	
	def simp1p(self,Command_num):
		if Command_num == 1:
			Rand_num = random.randint(1, 3)
			self.defense += Rand_num
		# =============================================================================
		elif Command_num == 2:
			Rand_num = random.randint(1, 5)
			self.commands += Rand_num - 2
		# =============================================================================
		elif Command_num == 3:
			print("not done")
			Rand_num = random.randint(1, 3)
			self.morale += Rand_num * 2
			self.organization += Rand_num - 5
		# =============================================================================
		elif Command_num == 4:
			Rand_num = random.randint(1, 4)
			self.simtension += 2
			self.scouting += Rand_num
			if self.scouting >20:
				self.scouting = 20
		# =============================================================================
		elif Command_num == 5:
			Rand_num = random.randint(2, 3)
			self.position += Rand_num
			self.simtension += 5
		# =============================================================================
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			# yo rony why didn't the terminal run???
			self.simtension += 8
			self.position += Rand_num * 2
			self.player.morale += Rand_num - 5
		# =============================================================================
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			self.morale += Rand_num + 1
	
	class friendlyVars():
		def __init__(self):
			self.count = 0
			self.morale = 5
			self.suppresion = 0
			self.organization = 5
			self.cav = 0
			self.cav_losses = 0
			self.inf = 0
			self.inf_losses = 0
			self.arti = 0
			self.arti_losses = 0
			self.scouting = 5
			self.position = 5
			self.defense = 5
			self.commands = 3
			self.damage = 0

co = ja.fg

#with open("main.py", "r+") as a:
#	data = a.readlines()
#a = 0
#for line in data:
#	a += 1
#	if "random.randint(" in line:
#		print(line)
#		print(a)
#	if "if " in line:
#		print(line)
#		print(a)
