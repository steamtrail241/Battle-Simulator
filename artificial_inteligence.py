import functions as ja
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
		self.size1 = 0
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
		self.center1 = 0
		self.flank1 = 0
		
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


	def predict(self, simpart):
		"""simpart can be three options:6
		1 = setup phase
		2 = setup and next phase
		"""
		a = time.time()
		highestnum=0
		path=[]
		self.reset_seeplayer1()		
		for i in range(1,8):
			self.simp1b(i)
			for i1 in range(1,8):
				self.simp1p(i1)
				for i2 in range(1,8):
					self.simp1b(i2)
					for i3 in range(1,8):
						self.simp1p(i3)
						for i4 in range(1,8):
							self.simp1b(i4)
							thistime = 0
							cheak = False
							if self.simtension<60:
								if self.count1>=self.seeplayer1.count:
									thistime += 1
									cheak = True
								if self.morale1>=self.seeplayer1.morale:
									thistime += 1
									cheak = True
								if self.cav1>=self.seeplayer1.cav:
									thistime+=1
									cheak = True
								if self.inf1>=self.seeplayer1.inf:
									thistime+=1
									cheak = True
								if self.arti1>=self.seeplayer1.arti:
									thistime+=1
									cheak = True
								if self.suppresion1>=self.seeplayer1.suppresion:
									thistime+=1
									cheak = True
								if self.organization1>=self.seeplayer1.organization:
									thistime+=1
									cheak = True
								if self.defense1>=self.seeplayer1.defense:
									thistime+=1
									cheak = True
								if self.position1>=self.seeplayer1.position:
									thistime+=1
									cheak = True
								if self.commands1>=self.seeplayer1.commands:
									thistime+=1
									cheak = True
								if cheak is False:
									print("nothing was bigger")
								self.simtension = 0
								if thistime>highestnum:
									highestnum = thistime
									path=[i,i2,i4]
									print(thistime)
									print(self.seeplayer1.count)
									print(self.seeplayer1.morale)
									print(self.seeplayer1.suppresion)
									print(self.seeplayer1.organization)
									print(self.seeplayer1.cav)
									print(self.seeplayer1.inf)
									print(self.seeplayer1.arti)
									print(self.seeplayer1.scouting)
									print(self.seeplayer1.position)
									print(self.seeplayer1.defense)
									print(self.seeplayer1.commands)
									print(self.seeplayer1.damage)
									print("=======")
									print(self.size1)
									print(self.count1)
									print(self.morale1)
									print(self.cav1)
									print(self.inf1)
									print(self.arti1)
									print(self.suppresion1)
									print(self.organization1)
									print(self.defense1)
									print(self.position1)
									print(self.commands1)
									print(self.center1)
									print(self.flank1)
								self.reset_seeplayer1()
							else:
								break
						
		if self.simtension >= 60:
			pass
		print(path)
		print(time.time()-a)


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
			Rand_num = random.randint(1, 3)
			self.morale += Rand_num * 2
			self.organization1 += Rand_num - 5
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
			self.position1 += Rand_num
			self.simtension += 5
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
			self.seeplayer1.defense += Rand_num
		# =============================================================================
		elif Command_num == 2:
			Rand_num = random.randint(1, 5)
			self.seeplayer1.commands += Rand_num - 2
		# =============================================================================
		elif Command_num == 3:
			Rand_num = random.randint(1, 3)
			self.seeplayer1.morale += Rand_num * 2
			self.seeplayer1.organization += Rand_num - 5
		# =============================================================================
		elif Command_num == 4:
			Rand_num = random.randint(1, 4)
			self.simtension += 2
			self.seeplayer1.scouting += Rand_num
			if self.seeplayer1.scouting >20:
				self.seeplayer1.scouting = 20
		# =============================================================================
		elif Command_num == 5:
			Rand_num = random.randint(2, 3)
			self.seeplayer1.position += Rand_num
			self.simtension += 5
		# =============================================================================
		elif Command_num == 6:
			Rand_num = random.randint(1, 4)
			# yo rony why didn't the terminal run???
			self.simtension += 8
			self.seeplayer1.position += Rand_num * 2
			self.seeplayer1.morale += Rand_num - 5
		# =============================================================================
		elif Command_num == 7:
			Rand_num = random.randint(1, 3)
			self.seeplayer1.morale += Rand_num + 1
	
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
