import random


class Colors():
	Black        = "\033[30m"
	Red          = "\033[31m"
	Green        = "\033[32m"
	Yellow       = "\033[33m"
	Blue         = "\033[34m"
	Magenta      = "\033[35m"
	Cyan         = "\033[36m"
	LightGray    = "\033[37m"
	DarkGray     = "\033[90m"
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"
	White        = "\033[97m"
	END          = "\003[0m"

class bc():
	BLACK   = '\033[40m'
	RED     = '\033[41m'
	GREEN   = '\033[42m'
	YELLOW  = '\033[43m'
	BLUE    = '\033[44m'
	MAGENTA = '\033[45m'
	CYAN    = '\033[46m'
	WHITE   = '\033[47m'
	RESET   = '\033[49m'

fg = Colors()
bg = bc()

# stands for print with color
def pwc(words, color, endtf=False):
  """stands for print with color"""
  if endtf is False:
    print(color+words+fg.LightRed)
  else:
    print(color+words+fg.LightRed, end="")

# ============================================================================
# holds the .stat function
# ============================================================================
# I do not know your funny words, how do I turn this into something typeable so that my code doesn't have an aneurysm?
# ya know whats funny about this, you've written so much code and i've seen your write random.randint() with floats inside BUT THE CODE NEVER GO THERE BECAUSE OF CONSTAN ERRIRS
# CALCULATION FOR COMBAT
def damage(base, suppresion_effect, defense_effect, organization_effect, suppresion, defense, organization):
  suppresion_effect /= 100
  defense_effect /= 100
  organization_effect /= 100
  return (base - suppresion*suppresion_effect - defense*defense_effect - organization*organization_effect)

def dmgEffect(damage, moralval, orgval, suprval, inf_num, cav_num, arti_num, enemy_size):
  moralval /= enemy_size
  orgval /= enemy_size
  suprval /= enemy_size
  val1 = inf_num + cav_num + arti_num
  infval = inf_num/val1
  cavval = cav_num/val1
  artival = arti_num/val1
  return (damage*moralval), (damage*orgval), (damage*suprval), (damage*infval), (damage*cavval), (damage*artival)

def recon(stringinput, recon, subj_var):
	val1 = random.randint(1,5)/5
	val2 = 20 - recon
	val3 = val1 * val2
	pwc(stringinput+": "+str(subj_var-val3)+"-"+str(subj_var+val3), fg.Yellow)


def inputprint(prompt, Friendly, Turn_count, MC):
  c1 = False
  while c1 is False:
    avar = input(prompt)
    # see's if the input is a interger
    try:
      randomvarable = int(avar)
      c1 = True
      break
    except: pass
    # see's if the input is "Jason sucks"
    if avar == "Jason sucks":
      return avar
    # real .stat functions begining
    alist = avar.split(" ")
    # determines if it is a command
    if alist[0] == ".stat":
      alist = avar.split(".stat ")
      # see's if user wants entire list (.stat) command or specifics (.stat (variable name)) command
      if len(alist)>1 and alist[1] != "":
        if alist[1] == "help":
          pwc("welcome to the advanced information page, this page can be accessed by typing .stat", "blue")
          pwc("here you can access every factor involving your army", "blue") 
          pwc("commands for accessing factors\n\
          .stat troop count\n\
          .stat morale\n\
          .stat suppresion\n\
          .stat organization\n\
          .stat cavalry\n\
          .stat infantry\n\
          .stat artillery\n\
          .stat reconnaissance level\n\
          .stat positioning\n\
          .stat fortification\n\
          .stat command limit\n", "green")
          pwc("commands that work while battel has started","blue")
          pwc(".stat bhs (for battle stats)", "green")
        elif alist[1] == "troop count":
          pwc(Friendly.player.count, fg.Green)
        elif alist[1] == "morale":
          pwc(Friendly.player.morale, "green")
        elif alist[1] == "suppresion":
          pwc(Friendly.player.suppresion, "green")
        elif alist[1] == "organization":
          print(Friendly.player.organization)
        elif alist[1] == "cavalry":
          print(Friendly.player.cav)
        elif alist[1] == "infantry":
          print(Friendly.player.inf)
        elif alist[1] == "artillery":
          print(Friendly.player.arti)          
        elif alist[1] == "reconnaissance level":
          print(Friendly.player.scouting)
        elif alist[1] == "positioning":
          print(Friendly.player.position)
        elif alist[1] == "fortification":
          print(Friendly.player.defense)
        elif alist[1] == "command limit":
          print(Friendly.player.commands)
        elif alist[1] == "Ronys story sucks":
          print("hehe I agree")
          nothingsus()
        elif MC == 1:
          if alist[1] == "bhs":
            pass
      else:
        print(Friendly.player.count)
        print(Friendly.player.morale)
        print(Friendly.player.suppresion)
        print(Friendly.player.organization)
        print(Friendly.player.cav)
        print(Friendly.player.inf)
        print(Friendly.player.arti)
        print(Friendly.player.scouting)
        print(Friendly.player.position)
        print(Friendly.player.defense)
        print(Friendly.player.commands)
    else:
      print("that is not a valid input")
  
  return avar

# =======================================================================================
# checks the input of each input
# =====================================================================================
def input_checks(thingyToPrint, AOO, FRI, TC, MC):
  # checks if it is one of the options (also checks if it is int)
  c1 = False
  while c1 is False:
    print(thingyToPrint)
    # checks if input is a letter
    c1_1 = False
    while c1_1 is False:
      avar = inputprint("", FRI, TC, MC)
      if avar == "Jason sucks":
        print("thank you")
        return random.randint(1, AOO)
      else:
        try:
          avar = int(avar)
          c1_1 = True
        except: pwc.jas("That is not a integer\nPlease input again!", "red")
    # checks if input is one of the options
    if avar<=AOO and avar>-1:
      return avar
    else:
      print("that is not a valid option!\nPlease input again!")

# =============================================================================
def easyprint(title, phases):
  pwc("==========", fg.Yellow, True)
  print(title, end="")
  pwc("==========", fg.Yellow)
  for i in phases:
    print("          ", end="")
    print(str(i[0])+str(i[1]), end="")
    if len(i)==2:
      print("/20")
    else:
      if i[2]==1:
        print("/50")
      if i[2]==2:
        print("")


def nothingsus():
	c1 = False
	while c1 is False:
		c1_1 = False
		while c1_1 is False:
			ainput = input("please inport pasword")
			try:
				ainput = int(ainput)
				c1_1 = True
				break
			except: pass
		c1_2 = False
		while c1_2 is False:
			ainput1 = input("please inport pasword")
			try:
				ainput1 = int(ainput1)
				c1_2 = True
				break
			except: pass
		if ainput * ainput1 == 499770 and ainput1 + ainput == 1639:
			print("hehe you got it")
			c1 = True
			break
		else:
			print("you did not enter the correct pasword")
			break

