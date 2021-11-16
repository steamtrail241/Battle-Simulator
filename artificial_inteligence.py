import jasons_and_ronys_functions as ja
import log as lo
import random, time

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
		self.scouting = 0
		self.cav_losses = 0
		self.arti_losses = 0
		self.simtension = 0
		self.player = self.friendlyVars()
		self.seeplayer = self.friendlyVars()
		self.seeplayer1 = self.friendlyVars()
		# simulated variables
		# self.size1 = 0
		self.count1 = 0
		self.morale1 = 0
		self.cav1 = 0
		self.inf1 = 0
		self.arti1 = 0
		self.suppresion1 = 0
		self.organization1 = 0
		self.defense1 = 0
		self.position1 = 0
		self.commands1 = 0
		# self.center1 = 0
		# self.flank1 = 0
		
	def originalset(self, max):
		"""set inf, arti, and cav to random variables"""
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

	def reset_seeplayer1(self):
		self.seeplayer1.count = self.seeplayer.count
		self.seeplayer1.morale = self.seeplayer.morale
		self.seeplayer1.suppresion = self.seeplayer.suppresion
		self.seeplayer1.organization = self.seeplayer.organization
		self.seeplayer1.cav = self.seeplayer.cav
		self.seeplayer1.inf = self.seeplayer.inf
		self.seeplayer1.arti = self.seeplayer.arti
		self.seeplayer1.scouting = self.seeplayer.scouting
		self.seeplayer1.position = self.seeplayer.position
		self.seeplayer1.defense = self.seeplayer.defense
		self.seeplayer1.commands = self.seeplayer.commands
		self.seeplayer1.damage = self.seeplayer.damage

	def predict(self, thati, simpart, deapth, thelist, player=False):
		# formula is (bot's total)-(players total)
		# bot wants to maximize
		# player wants to minimize
		if deapth == 0:
			self.simtension = 0
			a = 0
			for i in thelist[0]:
				a+=i
			for i in thelist[1]:
				a-=i
			return a
			
			
		elif player:
			if simpart == 7:
				if self.simtension<=60:
					alist = self.simp1b(thati, thelist)
					outcomes = []
					for i in range(1,8):
						lo.ws(str(i), [deapth, "bot move"])
						if deapth == 1:
							avar = self.simp1p(i, alist, tf=True)
							alist = avar[0]
							avar1 = avar[1]
							avar = avar[2]
						outcomes.append(self.predict(i, simpart, deapth-1, alist))
						if deapth == 1:
							alist[avar1]-=avar
							print("yay!!!!")
							arandomvariablethatnoonecaresabout = 1
							print(arandomvariablethatnoonecaresabout)
					lo.ws("outcomes on bot", outcomes)
					return int(self.max(outcomes))

				else:
					simpart = 5
			
			if simpart == 5:
				if self.simtension<=60:
					lo.ws("got to simtension = 5 bot ", [])
					return 10000
			else:
				print("something went whong with sim part")
		else:
			if simpart == 7:
				if self.simtension<=60:
					alist = self.simp1p(thati, thelist)
					outcomes = []
					for i in range(1,8):
						lo.ws(str(i), [deapth, "player move"])
						if deapth == 1:
							avar = self.simp1b(i, alist)
							alist = avar[0]
							avar1 = avar[1]
							avar = avar[2]
						outcomes.append(self.predict(i, simpart, deapth-1, alist, player=True))
						if deapth == 1:
							alist[avar1]-=avar
						print("player outcomes")
					lo.ws("outcomes on player ", outcomes)
					a = self.min(outcomes)
					return a
				else:
					simpart = 5
			if simpart == 5:
				if self.simtension <=60:
					print("got to simpart = 5 player")
					return 1000


	def min(self, the_list):
		print(the_list)
		smollest = 10000
		for i in range(3):
			for v in the_list:
				if v<smollest:
					smollest = v
		return v
	
	def max(self, thelist):
		largest = 100000000000
		for i in range(3):
			for v in thelist:
				if v>largest:
					largest = v
		return v

	def sim2b(self, Command_num):
		self.simtension += random.randint(1, 3)
		if self.simtension > 30:
			print(self.simtension)
			Maneuver_check = 0
			Skirmish_check = 0
			Battle_check = 1
		if Army_terrain == 1:
			if Command_num == 1:
				Rand_num = random.randint(2, 3)
				self.seeplayer1.organization += Rand_num * 2
			elif Command_num == 2:
				Rand_num = random.randint(1, 5)
				self.seeplayer1.command = Rand_num - 2
			elif Command_num == 3:
				Subturn_count = 1
				Subturn_count += 1
			Command_num = int(jas.input_checks("", 4, Friendly, Turn_count, Maneuver_check))
			if Subturn_count == 3:
				Subturn_count = 0
			if Command_num == 1:
				Rand_num = random.randint(3, 5)
				self.seeplayer1.damage = self.seeplayer1.arti * (Rand_num) * (1 - (self.seeplayer1.suppresion) / 100) * (1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
				Friendly.inf_losses = self.seeplayer1.damage
				Friendly.center -= (Friendly.inf_losses / Friendly.size) * 40
				Friendly.inf -= self.seeplayer1.damage
				Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
				Friendly.suppresion += (self.seeplayer1.damage / Friendly.size) * 40
				Subturn_count += 1
			elif Command_num == 2:
				Rand_num = random.randint(3, 4)
				self.seeplayer1.damage = self.seeplayer1.arti * (Rand_num) * (1 - (self.seeplayer1.suppresion) / 100) * (1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
				Friendly.inf_losses = self.seeplayer1.damage
				Friendly.flank -= (Friendly.inf_losses / Friendly.size) * 40
				Friendly.inf -= Friendly.player.damage
				Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
				Friendly.suppresion += (self.seeplayer1.damage / Friendly.size) * 40
				Subturn_count += 1
			elif Command_num == 3:
				Rand_num = random.randint(2, 3)
				self.seeplayer1.damage = self.seeplayer1.arti * (Rand_num) * (1 - (self.seeplayer1.suppresion) / 100) * (1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
				Friendly.inf_losses = self.seeplayer1.damage
				Friendly.inf -= self.seeplayer1.damage
				Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
				Friendly.suppresion += (self.seeplayer1.damage / Friendly.size) * 100
				Subturn_count += 1
			elif Command_num == 4:
				Rand_num = random.randint(5, 7)
				self.seeplayer1.damage = self.seeplayer1.arti * (Rand_num) * (1 - (self.seeplayer1.suppresion) / 100) * (1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
				Friendly.inf_losses = self.seeplayer1.damage
				Friendly.inf -= self.seeplayer1.damage
				Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 40
				Friendly.suppresion += (self.seeplayer1.damage / Friendly.size) / 40
				Subturn_count += 1
			elif Command_num == 5:
				Subturn_count = 0
		elif Command_num == 4:
			Subturn_count = 1
			while Subturn_count != 0:
				Subturn_count += 1
				jas.easyprint("SKIRMISH ATTACK",[["COMBINED ARMS HARRASMENT", Subturn_count], ["MORALE: ", self.seeplayer1.inf_losses],["ORGANISATION: ", self.seeplayer1.organization], ["POSITION", self.seeplayer1.defense],["SUPPRESSION: ", self.seeplayer1.suppresion, 1]])
				jas.easyprint("BATTLE STATISTICS",[["INFANTRY: ", self.seeplayer1.inf], ["INFANTRY LOSSES: ", self.seeplayer1.inf_losses],
					["CAVALRY: ", self.seeplayer1.cav], ["CAVALRY LOSSES: ", self.seeplayer1.cav_losses],
					["ARTILLERY: ", self.seeplayer1.arti], ["ARTILLERY LOSSES: ", self.seeplayer1.arti_losses],
					["TOTAL TROOP COUNT: ", self.seeplayer1.inf + self.seeplayer1.cav + self.seeplayer1.arti],
					["TOTAL LOSSES: ",self.seeplayer1.inf_losses + self.seeplayer1.cav_losses + self.seeplayer1.arti_losses]])

				jas.pwc("Harrasment options", "blue")
				print("[1] pick of isolated groups (-enemy_recon,+morale damage)\n[2] raid supply lines (-enemy_position,+morale damage,)\n[3] feignt a charge (+suppresion,+morale damage)\n[4] call off attack")
				Command_num = int(jas.input_checks("", Army_points, Friendly, Turn_count, Maneuver_check))
				if Subturn_count == 3:
					Subturn_count = 0
				if Command_num == 1:
					Rand_num = random.randint(5, 10)/100
					self.seeplayer1.damage = (self.seeplayer1.inf + self.seeplayer1.cav) / 8 * (Rand_num) * (
							1 - (self.seeplayer1.suppresion) / 200) * (1 - (Friendly.defense) / 100) * (
							1 - (Friendly.organization) / 50)
					Friendly.inf_losses = self.seeplayer1.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
					Friendly.inf -= Friendly.inf_losses
					Friendly.cav_losses = self.seeplayer1.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
					Friendly.cav -= Friendly.cav_losses
					Friendly.morale -= ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 50
					Friendly.suppresion += (self.seeplayer1.damage / Friendly.size) * 50
				if Command_num == 2:
					Rand_num = random.randint(2, 5)/100
					self.seeplayer1.damage = (self.seeplayer1.inf + self.seeplayer1.cav) / 8 * (Rand_num) * (
						1 - (self.seeplayer1.suppresion) / 500) * (1 - (Friendly.defense) / 500) * (
						1 - (Friendly.organization) / 500)
					Friendly.inf_losses = self.seeplayer1.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
					Friendly.inf -= Friendly.inf_losses
					Friendly.cav_losses = self.seeplayer1.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
					Friendly.cav -= Friendly.cav_losses
					Friendly.morale -= 3 + ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 50
					Friendly.suppresion += 1 + (self.seeplayer1.damage / Friendly.size) * 50
					Friendly.position -= 2
				if Command_num == 3:
					Rand_num = random.randint(0, 0)
					Friendly.player.damage = (Friendly.player.inf + Friendly.player.cav) / 8 * (Rand_num) * (
							1 - (Friendly.player.suppresion) / 500) * (1 - (Friendly.defense) / 500) * (
							1 - (Friendly.organization) / 500)
					Friendly.inf_losses = Friendly.player.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
					Friendly.inf -= Friendly.inf_losses
					Friendly.cav_losses = Friendly.player.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
					Friendly.cav -= Friendly.cav_losses
					Friendly.morale -= 6 + ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 50
					Friendly.suppresion += 1 + (Friendly.player.damage / Friendly.size) * 50
				elif Command_num == 4:
					Subturn_count = 0
		elif Command_num == 5:
			Subturn_count = 1
			while Subturn_count != 0:
				Subturn_count += 1
				jas.easyprint("SKIRMISH ATTACK",
							[["CAVALRY HARRASMENT, TURN: ", Subturn_count], ["MORALE: ", Friendly.player.inf_losses],
							["ORGANISATION: ", Friendly.player.organization], ["POSITION: ", Friendly.player.defense],
							["SUPPRESSION: ", Friendly.player.suppresion, 1]])
				jas.easyprint("BATTLE STATISTICS",
							[["INFANTRY: ", Friendly.player.inf], ["INFANTRY LOSSES: ", Friendly.player.inf_losses],
							["CAVALRY: ", Friendly.player.cav], ["CAVALRY LOSSES: ", Friendly.player.cav_losses],
							["ARTILLERY: ", Friendly.player.arti], ["ARTILLERY LOSSES: ", Friendly.player.arti_losses],
							["TOTAL TROOP COUNT: ", Friendly.player.inf + Friendly.player.cav + Friendly.player.arti],
							["TOTAL LOSSES: ",
								Friendly.player.inf_losses + Friendly.player.cav_losses + Friendly.player.arti_losses]])
				jas.pwc("Harrasment options", "blue")
				print(
					"[1] pick of isolated groups (-enemy_recon,+morale damage)\n[2] raid supply lines (-enemy_position,+morale damage,)\n[3] feignt a charge (+suppresion,+morale damage)\n[4] call off attack")
				Command_num = int(jas.input_checks("", Army_points, Friendly, Turn_count, Maneuver_check))
				if Subturn_count == 3:
					Subturn_count = 0
				if Command_num == 1:
					Rand_num = random.randint(0.10, 0.20)
					Friendly.player.damage = Rand_num * (Friendly.player.cav) / 4 * (Rand_num) * (
							1 - (Friendly.player.suppresion) / 200) * (1 - (Friendly.defense) / 100) * (
													1 - (Friendly.organization) / 50)
					Friendly.inf_losses = Friendly.player.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
					Friendly.inf -= Friendly.inf_losses
					Friendly.cav_losses = Friendly.player.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
					Friendly.cav -= Friendly.cav_losses
					Friendly.morale -= ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 100
					Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 25
				if Command_num == 2:
					Rand_num = random.randint(0.05, 0.10)
					Friendly.player.damage = Rand_num * (Friendly.player.cav) / 4 * (Rand_num) * (
							1 - (Friendly.player.suppresion) / 500) * (1 - (Friendly.defense) / 500) * (
													1 - (Friendly.organization) / 500)
					Friendly.inf_losses = Friendly.player.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
					Friendly.inf -= Friendly.inf_losses
					Friendly.cav_losses = Friendly.player.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
					Friendly.cav -= Friendly.cav_losses
					Friendly.morale -= ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 200
					Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 10
				if Command_num == 3:
					Rand_num = random.randint(0.5, 0.8)
					Friendly.player.damage = Rand_num * (Friendly.player.cav) / 4 * (Rand_num) * (
							1 - (Friendly.player.suppresion) / 500) * (1 - (Friendly.defense) / 500) * (
													1 - (Friendly.organization) / 500)
					Friendly.morale -= ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 200
					Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 10
				if Command_num == 4:
					Subturn_count = 0
				pass
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			Tension += 8
			Friendly.player.position += Rand_num + 2
			Friendly.player.defensse += Rand_num + 2
			if Rand_num == 1:
				jas.pwc("Your army is delayed and begraggled by bad conditions, limited work is done to secure positions",
						co.Red)
			if Rand_num == 2:
				jas.pwc(
					"Your army arrives at the forward positions, though interference denies them the opportunity to fully fortify",
					co.Yellow)
			if Rand_num == 3:
				jas.pwc("Your army obliges with the march, fortifying themselves in advanced strongpoints", co.Green)
			if Rand_num == 4:
				jas.pwc("Your army marches forward, entrenching themselves deep against enemy lines", co.Green)
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			Friendly.player.morale += Rand_num * 2
			if Rand_num == 1:
				jas.pwc("You perform a speech to your troops, it had a mediocre impact on the troops", co.Red)
			if Rand_num == 2:
				jas.pwc("You perform a speech to your troops, reinvigorating your army", co.yellow)
			if Rand_num == 3:
				jas.pwc("You perform a brilliant speech to your troops, your army becomes estatic and determined", co.Green)
			pass

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

	def simp1b(self,Command_num, thelist, tf=False):
		# list index repersent
		# 0 : count
		# 1 : morale
		# 2 : supresion
		# 3 : organization
		# 4 : cav
		# 5 : inf
		# 6 : arti
		# 7 : scouting
		# 8 : position
		# 9 : defense
		# 10: commands
		# 11: damage
		if Command_num == 1:
			Rand_num = random.randint(1, 3)
			thelist[0][9] += Rand_num
		# =============================================================================
		elif Command_num == 2:
			Rand_num = random.randint(1, 5)
			thelist[0][10] += Rand_num - 2
		# =============================================================================
		elif Command_num == 3:
			Rand_num = random.randint(1, 3)
			self.morale += Rand_num * 2
			thelist[0][3] += Rand_num - 5
		# =============================================================================
		elif Command_num == 4:
			Rand_num = random.randint(1, 4)
			self.simtension += 2
			# self.scouting1 += Rand_num
			#if self.scouting1 >20:
			#	self.scouting1 = 20
		# =============================================================================
		elif Command_num == 5:
			Rand_num = random.randint(2, 3)
			thelist[0][8] += Rand_num
			self.simtension += 5
		# =============================================================================
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			# yo rony why didn't the terminal run???
			self.simtension += 8
			thelist[0][8] += Rand_num * 2
			thelist[0][1] += Rand_num - 5
		# =============================================================================
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			thelist[0][1] += Rand_num + 1
		if tf is False:
			return thelist
		else:
			return [thelist, Rand_num, Command_num-1]
	
	def simp1p(self,Command_num, thelist, tf=False):
		# list index repersent
		# 0 : count
		# 1 : morale
		# 2 : supresion
		# 3 : organization
		# 4 : cav
		# 5 : inf
		# 6 : arti
		# 7 : scouting
		# 8 : position
		# 9 : defense
		# 10: commands
		# 11: damage
		if Command_num == 1:
			# defense
			Rand_num = random.randint(1, 3)
			thelist[1][9] += Rand_num
		# =============================================================================
		elif Command_num == 2:
			Rand_num = random.randint(1, 5)
			# commands
			thelist[1][10] += Rand_num - 2
		# =============================================================================
		elif Command_num == 3:
			Rand_num = random.randint(1, 3)
			# morale and organization
			thelist[1][1] += Rand_num * 2
			thelist[1][3] += Rand_num - 5
		# =============================================================================
		elif Command_num == 4:
			Rand_num = random.randint(1, 4)
			self.simtension += 2
			# scouting
			thelist[1][7] += Rand_num
			if thelist[1][7] >20:
				thelist[1][7] = 20
		# =============================================================================
		elif Command_num == 5:
			Rand_num = random.randint(2, 3)
			# position
			thelist[1][8] += Rand_num
			self.simtension += 5
		# =============================================================================
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			# position and morale
			self.simtension += 8
			thelist[1][8] += Rand_num * 2
			thelist[1][1] += Rand_num - 5
		# =============================================================================
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			# morale
			thelist[1][1] += Rand_num + 1
		if tf is False:
			return thelist
		else:
			return [thelist, Rand_num, Command_num-1]
	
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
			self.scouting = 0
			self.position = 0
			self.defense = 0
			self.commands = 0
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
for i in range(1,8):
	print(i)