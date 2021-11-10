import time, random, asyncio, log
import Jasons_functions as jas
import artificial_inteligence as ai
# from replit import audio
# import time

# audio.play_file("Main_theme.mp3")
# time.sleep(10)

co = jas.fg
bg = jas.bc()

Tension = 0
Turn_count = 0
Subturn_count = 0
Army_points = 0
Army_size = 1
Army_terrain = 0
jas.pwc("type '.stat help' for information", co.Cyan)
#Shaan did this 
print("Shaan is a cool dude")
print("Shann is a cool dude!!!!")
print("however,\nRony is not a cool dude.")
# =============================================================================
global Friendly
Friendly = ai.AI()
Tension = 0
global Maneuver_check
Maneuver_check = 0
Skirmish_check = 0
Battle_check = 0
Rout_check = 0
Rand_num = 0
Command_num = 0

time.sleep(0.2)
print("Welcome to commander simulator!")
# ===============================================================================
Army_size = jas.input_checks(co.Cyan + "\nplease input battle size\n" +
                             co.LightGreen + "[1] Small battle (500v500)\n[2] Medium battle (1000v1000)\n[3] Large battle (2000v2000)\n[4] Gigantic battle (10000v10000)" + co.LightRed,
                             4, Friendly.player, Turn_count, Maneuver_check)

if Army_size == 1:
    Army_points = 500
    Friendly.size = 500
elif Army_size == 2:
    Army_points = 1000
    Friendly.size = 1000
elif Army_size == 3:
    Army_points = 2000
    Friendly.size = 2000
elif Army_size == 4:
    Army_points = 10000
    Friendly.size = 10000
time.sleep(0.2)

Army_terrain = jas.input_checks(co.Cyan + "\n\nplease input terrain\n"
                                + co.LightGreen + "[1]flat plains\n[2]river crossing\n[3]thick forest\n[4]rugged hills\n[5]sodden swamp" + co.LightRed,
                                5, Friendly, Turn_count, Maneuver_check)
time.sleep(0.2)
Friendly.originalset(Army_points)
Friendly.player.inf = jas.input_checks(
    co.Cyan + "\n\nplease set up your army" + co.Yellow + "\n\ninput infantry count (1 army size per infantry)\nremaining army points: " + str(
        Army_points) + co.LightRed, Army_points, Friendly, Turn_count, Maneuver_check)
Army_points -= Friendly.player.inf
time.sleep(0.2)


jas.pwc("\n\ninput army size for cavalry (2 army size for 1 cavalry)", co.Cyan)
print("remaining army points: " + str(Army_points))
print("Infantry: " + str(Friendly.player.inf) + "\nCavalry: " + str(Friendly.player.cav) + "\nArtillery: " + str(
    Friendly.player.arti))

Friendly.player.cav = int(jas.input_checks("", Army_points, Friendly, Turn_count, Maneuver_check))
Army_points -= Friendly.player.cav
Friendly.player.cav /= 2
Friendly.player.cav = round(Friendly.player.cav, 1)
time.sleep(0.2)

jas.pwc("\n\ninput army size for artillery (15 army size for 1 artillery)", co.Cyan)
print("remaining army points: " + str(Army_points))
print("Infantry: " + str(Friendly.player.inf) + "\nCavalry: " + str(Friendly.player.cav) + "\nArtillery: " + str(
    Friendly.player.arti))

Friendly.player.arti = int(jas.input_checks("", Army_points, Friendly, Turn_count, Maneuver_check))
Army_points -= Friendly.player.arti
Friendly.player.arti /= 10
Friendly.player.arti = round(Friendly.player.arti, 1)

print("Infantry: " + str(Friendly.player.inf) + "\nCavalry: " + str(Friendly.player.cav) + "\nArtillery: " + str(
    Friendly.player.arti))
time.sleep(0.2)

jas.pwc("\n\nremaining army points will be turned into infantry", co.Magenta)
Friendly.player.inf += Army_points
Army_points = 0
time.sleep(0.2)

jas.pwc("Infantry: " + str(Friendly.player.inf) + "\nCavalry: " + str(Friendly.player.cav) + "\nArtillery: " + str(
    Friendly.player.arti),
        co.LightRed)
time.sleep(0.2)
Friendly.setvars()
sp = "        "
nl = "\n"
Turn_count = 1
Maneuver_check = 1
while Maneuver_check == 1:
    jas.easyprint("BATTLE HAS STARTED",
                  [["MANUEVER PHRASE, TURN ", Turn_count, 2], ["MORALE: ", Friendly.player.morale],
                   ["ORGANIZATION: ", Friendly.player.organization], ["POSITION: ", Friendly.player.position],
                   ["RECONNAISSANCE: ", Friendly.player.scouting], ["FORTIFICATION: ", Friendly.player.defense]])
    Turn_count += 1
    Tension += random.randint(1, 3)
    if Tension > 30:
        Maneuver_check = 0
        Skirmish_check = 1
        break
    if Army_terrain == 1:
        print(
            co.Cyan + "Flat Terrain Maneuvers\n" + co.LightGreen + "[1] establish fortifications (++defense)\n[2] establish war room (++command)\n[3] set up camp (++morale,-organization)\n[4] scout enemy positions (+scouting,+tension)\n[5] march to good terrain (+position,+tension)\n[6] forced march to good terrain (++position,-morale,++tension)\n[7] perform a rousing speach (+morale) ")
        Command_num = int(jas.inputprint("", Friendly, Turn_count, Maneuver_check))
        # =============================================================================
        if Command_num == 1:
            Rand_num = random.randint(1, 3)
            Friendly.player.defense += Rand_num
            if Rand_num == 1:
                jas.pwc("your soldiers were able to establish rudimentary defenses", co.Red)
            if Rand_num == 2:
                jas.pwc("your soldiers were able to create an adequete set of defenses", co.Yellow)
            if Rand_num == 3:
                jas.pwc("your soldiers were able to construct a formidable series of fortifications", co.Green)
            pass
        # =============================================================================
        elif Command_num == 2:
            Rand_num = random.randint(1, 5)
            Friendly.player.commands += Rand_num - 2
            if Rand_num == 1:
                jas.pwc("your staff bicker and argue over the finest details", co.Red)
            if Rand_num == 2:
                jas.pwc("your staff are divided on the course of action", co.Red)
            if Rand_num == 3:
                jas.pwc("your staff begrudgingly agrees to a vague plan of action", co.Yellow)
            if Rand_num == 4:
                jas.pwc("your staff arrive at a conclusion for a course of action", co.Green)
            if Rand_num == 5:
                jas.pwc("your staff are in complete agreement and leave with determined vigor", co.Green)
            pass
        # =============================================================================
        elif Command_num == 3:
            print("not done")
            Rand_num = random.randint(1, 3)
            Friendly.player.morale += Rand_num * 2
            Friendly.player.organization += Rand_num - 5
            if Rand_num == 1:
                jas.pwc("Your soldiers are rowdy and drunken, your camp becomes a chaotic mess", co.Red)
            if Rand_num == 2:
                jas.pwc("Your soldiers set up camp in an adequate manner, though a few rowdy incidents occur",
                        co.Yellow)
            if Rand_num == 3:
                jas.pwc(
                    "Your soldiers set up camp in a timely manner, the mood is cheerful, but discipline is still in place",
                    co.Green)
            pass
        # =============================================================================
        elif Command_num == 4:
            Rand_num = random.randint(1, 4)
            Tension += 2
            Friendly.setvars()
            Friendly.player.scouting += Rand_num
            if Friendly.player.scouting >20:
              Friendly.player.scouting = 20
            if Rand_num == 1:
                jas.pwc("Your scouting party is spotted by enemy troops!, a firefight has broken out!", co.Red)
                # if scouting goes wrong, the skirmish phase can pre-emptively begin
                Skirmish_check = 1
                Maneuver_check = 0
            if Rand_num == 2:
                jas.pwc(
                    "Your scouting party was forced to turn back before they reached enemy lines, but were able to detect forward enemy positions",
                    co.Yellow)
            if Rand_num == 3:
                jas.pwc(
                    "Your scouting party successfully reached enemy lines, but were forced back prematurely to avoid detection",
                    co.Yellow)
            if Rand_num == 4:
                jas.pwc(
                    "Your scouting party infiltrated enemy lines flawlessly, giving you a full view of enemy positions",
                    co.Green)
            pass
        # =============================================================================
        elif Command_num == 5:
            Rand_num = random.randint(2, 3)
            Friendly.player.position += Rand_num
            Tension += 5
            if Rand_num == 2:
                jas.pwc(
                    "Your army is bogged down by weather and logistics, as such your advance was slowed considerably",
                    co.Red)
            if Rand_num == 3:
                jas.pwc("Your army marched in orderly fashion, reaching their advantageous positions in short order",
                        co.Green)
            pass
        # =============================================================================
        elif Command_num == 6:
            Rand_num = random.randint(1, 4)
            # yo rony why didn't the terminal run???
            Tension += 8
            Friendly.player.position += Rand_num * 2
            Friendly.player.morale += Rand_num - 5
            if Rand_num == 1:
                jas.pwc("Your army is outraged by the forced march, and talks of mutiny circle", co.Red)
            if Rand_num == 2:
                jas.pwc("Your army begrudingly marches forward, though without significant discontent", co.Yellow)
            if Rand_num == 3:
                jas.pwc("Your army obliges with the march, though they are visibly demoralized", co.Yellow)
            if Rand_num == 4:
                jas.pwc("Your army marches forward, with only the  slightest hint of discontentment", co.Green)

            pass
        # =============================================================================
        elif Command_num == 7:
            Rand_num = random.randint(1, 3)
            Friendly.player.morale += Rand_num + 1
            if Rand_num == 1:
                jas.pwc("You perform a speech to your troops, it had a mediocre impact on the troops", co.Red)
            if Rand_num == 2:
                jas.pwc("You perform a speech to your troops, reinvigorating your army", co.Yellow)
            if Rand_num == 3:
                jas.pwc("You perform a brilliant speech to your troops, your army becomes estatic and determined",
                        co.Green)
        pass

Tension = 0

while Skirmish_check == 1:
    jas.easyprint("\nCONFLICT HAS ESCALATED",
    [["SKRIMISH PHASE: TURN ", Turn_count, 2], ["MORALE: ", Friendly.player.morale],
    ["ORGANISATION: ", Friendly.player.organization], ["POSITION: ", Friendly.player.position],
    ["RECONNAISSANCE: ", Friendly.player.scouting],
    ["FORTIFICATION: ", Friendly.player.defense],
    ["SUPPRESSION: ", Friendly.player.suppresion, 1]])
    jas.easyprint("\nENEMY RECON: TURN ", [[Turn_count, 2]])
    jas.recon("MORALE",Friendly.player.scouting,Friendly.morale) 
    jas.recon("ORGANIZATION",Friendly.player.scouting,Friendly.organization)
    jas.recon("POSITION",Friendly.player.scouting,Friendly.position)
    jas.recon("RECONNAISSANCE", Friendly.player.scouting,Friendly.scouting)
    jas.recon("FORTIFICATION",Friendly.player.scouting,Friendly.defense)
    jas.recon("SUPPRESSION", Friendly.player.scouting,Friendly.suppresion)

    jas.easyprint("ARMY STATISTICS",
    [["INFANTRY: ", Friendly.player.inf, 2], ["INFANTRY LOSSES: ", Friendly.player.inf_losses, 2],
    ["CAVALRY: ", Friendly.player.cav, 2], ["CAVALRY LOSSES: ", Friendly.player.cav_losses, 2],
    ["ARTILLERY: ", Friendly.player.arti, 2], ["ARTILLERY LOSSES: ", Friendly.player.arti_losses, 2],
    ["TOTAL TROOP COUNT: ", Friendly.player.inf + Friendly.player.cav + Friendly.player.arti, 2],
    ["TOTAL LOSSES: ",
    Friendly.player.inf_losses + Friendly.player.cav_losses + Friendly.player.arti_losses, 2]])

    jas.easyprint("ENEMY ARMY STATISTICS",
    [["INFANTRY: ", Friendly.inf, 2], ["INFANTRY LOSSES: ", Friendly.inf_losses, 2],
    ["CAVALRY: ", Friendly.cav, 2], ["CAVALRY LOSSES: ", Friendly.cav_losses, 2],
    ["ARTILLERY: ", Friendly.arti, 2], ["ARTILLERY LOSSES: ", Friendly.arti_losses, 2],
    ["TOTAL TROOP COUNT: ", Friendly.inf + Friendly.cav + Friendly.arti, 2],
    ["TOTAL LOSSES: ", Friendly.inf_losses + Friendly.cav_losses + Friendly.arti_losses, 2]])

    Turn_count += 1
    Tension += random.randint(1, 3)
    if Tension > 30:
        print(Tension)
        Maneuver_check = 0
        Skirmish_check = 0
        Battle_check = 1
        break
    if Army_terrain == 1:
        jas.pwc("Flat Terrain Maneuvers\n", "blue")
        print(
            "[1] form rank (++organization)\n[2] form council with army staff (+command)\n[3] perform pre-emptive artillery barrage (++enemysuppresion,-enemy organization,ENGAGE IN RANGED ATTACK,++++tension)\n[4] harass enemy positions (+scouting,+enemy suppresion,++tensionF,ENGAGE IN SKIRMISH ATTACK)\n[5] send in a cavalry raid (-enemy organisation,-enemy morale,-enemy position,+tension,ENGAGE IN SKIRMISH ATTACK)\n[6] fortify forward positions (+position,+fortification,)\n[7] perform a rousing speach (++morale)",
            "pink")
        Command_num = int(jas.inputprint("", Friendly, Turn_count, Maneuver_check))
        if Command_num == 1:
            Rand_num = random.randint(2, 3)
            Friendly.player.organization += Rand_num * 2
            if Rand_num == 2:
                jas.pwc("Your troops walk into formation, steeling themselves for the battle to come ", co.Red)
            if Rand_num == 3:
                jas.pwc("Your troops march into formation, ready for the battle to come", co.Green)
        elif Command_num == 2:
            Rand_num = random.randint(1, 5)
            Friendly.player.command = Rand_num - 2
            if Rand_num == 1:
                jas.pwc("Your staff devolve into panicked sheep, the stress of battle addling their minds", co.Red)
            if Rand_num == 2:
                jas.pwc("Your staff remains indecisive and factionalized", co.Red)
            if Rand_num == 3:
                jas.pwc("Your staff arrive at a general plan, amidst much chaos and confusion", co.Yellow)
            if Rand_num == 4:
                jas.pwc("Your staff sets a course of action, though bickering remains commonplace", co.Yellow)
                #       if Rand_num == 5:
                jas.pwc("Despite the chaos of battle, your staff remains focused and resolute", co.Green)
        elif Command_num == 3:
            Subturn_count = 1
        # while Subturn_count != 0:
        jas.easyprint("RANGED ATTACK",
        [["ARTILLERY BOMBARDMENT: SUBTURN ", Subturn_count, 2], ["MORALE: ", Friendly.player.inf_losses],
        ["ORGANISATION: ", Friendly.player.organization], ["POSITION: ", Friendly.player.defense],
        ["SUPPRESSION: ", Friendly.player.suppresion, 1]])
        jas.easyprint("BATTLE STATISTICS",
        [["INFANTRY: ", Friendly.player.inf, 2], ["INFANTRY LOSSES: ", Friendly.player.inf_losses, 2],
        ["CAVALRY: ", Friendly.player.cav, 2], ["CAVALRY LOSSES: ", Friendly.player.cav_losses, 2],
        ["ARTILLERY: ", Friendly.player.arti, 2], ["ARTILLERY LOSSES: ", Friendly.player.arti_losses, 2],
        ["TOTAL TROOP COUNT: ", Friendly.player.inf + Friendly.player.cav + Friendly.player.arti, 2],
        ["TOTAL LOSSES: ",
        Friendly.player.inf_losses + Friendly.player.cav_losses + Friendly.player.arti_losses, 2]])
        Subturn_count += 1
        jas.pwc("Bombardment options", co.Cyan)
        print(
            "[1] target center (++central breakthrough,+suppresion,+morale damage)\n[2] target flank (++flanking,+suppresion,+morale damage)\n[3] suppresive fire (+++suppresion,-enemy organization)\n[4] concentrated fire (++morale damage,--enemy organization)")
        Command_num = int(jas.input_checks("", 4, Friendly, Turn_count, Maneuver_check))
        if Subturn_count == 3:
            Subturn_count = 0
        if Command_num == 1:
            Rand_num = random.randint(3, 5)
            Friendly.player.damage = Friendly.player.arti * (Rand_num) * (1 - (Friendly.player.suppresion) / 100) * (
                    1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
            Friendly.inf_losses = Friendly.player.damage
            Friendly.center -= (Friendly.inf_losses / Friendly.size) * 40
            Friendly.inf -= Friendly.player.damage
            Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
            Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 40
            Subturn_count += 1
        elif Command_num == 2:
            Rand_num = random.randint(3, 4)
            Friendly.player.damage = Friendly.player.arti * (Rand_num) * (1 - (Friendly.player.suppresion) / 100) * (
                    1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
            Friendly.inf_losses = Friendly.player.damage
            Friendly.flank -= (Friendly.inf_losses / Friendly.size) * 40
            Friendly.inf -= Friendly.player.damage
            Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
            Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 40
            Subturn_count += 1
        elif Command_num == 3:
            Rand_num = random.randint(2, 3)
            Friendly.player.damage = Friendly.player.arti * (Rand_num) * (1 - (Friendly.player.suppresion) / 100) * (
                    1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
            Friendly.inf_losses = Friendly.player.damage
            Friendly.inf -= Friendly.player.damage
            Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 20
            Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 100
            Subturn_count += 1
        elif Command_num == 4:
            Rand_num = random.randint(5, 7)
            Friendly.player.damage = Friendly.player.arti * (Rand_num) * (1 - (Friendly.player.suppresion) / 100) * (
                    1 - (Friendly.defense) / 50) * (1 - (Friendly.organization) / 100)
            Friendly.inf_losses = Friendly.player.damage
            Friendly.inf -= Friendly.player.damage
            Friendly.morale -= (Friendly.inf_losses / Friendly.size) * 40
            Friendly.suppresion += (Friendly.player.damage / Friendly.size) / 40
            Subturn_count += 1
        elif Command_num == 5:
            Subturn_count = 0
    elif Command_num == 4:
        Subturn_count = 1
        while Subturn_count != 0:
            Subturn_count += 1
            jas.easyprint("SKIRMISH ATTACK",[["COMBINED ARMS HARRASMENT", Subturn_count], ["MORALE: ", Friendly.player.inf_losses],["ORGANISATION: ", Friendly.player.organization], ["POSITION", Friendly.player.defense],["SUPPRESSION: ", Friendly.player.suppresion, 1]])
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
                Rand_num = random.randint(5, 10)/100
                Friendly.player.damage = (Friendly.player.inf + Friendly.player.cav) / 8 * (Rand_num) * (
                        1 - (Friendly.player.suppresion) / 200) * (1 - (Friendly.defense) / 100) * (
                                                 1 - (Friendly.organization) / 50)
                Friendly.inf_losses = Friendly.player.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
                Friendly.inf -= Friendly.inf_losses
                Friendly.cav_losses = Friendly.player.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
                Friendly.cav -= Friendly.cav_losses
                Friendly.morale -= ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 50
                Friendly.suppresion += (Friendly.player.damage / Friendly.size) * 50
            if Command_num == 2:
                Rand_num = random.randint(2, 5)/100
                Friendly.player.damage = (Friendly.player.inf + Friendly.player.cav) / 8 * (Rand_num) * (
                        1 - (Friendly.player.suppresion) / 500) * (1 - (Friendly.defense) / 500) * (
                1 - (Friendly.organization) / 500)
                Friendly.inf_losses = Friendly.player.damage * (Friendly.inf / (Friendly.cav + Friendly.inf))
                Friendly.inf -= Friendly.inf_losses
                Friendly.cav_losses = Friendly.player.damage * (Friendly.cav / (Friendly.cav + Friendly.inf))
                Friendly.cav -= Friendly.cav_losses
                Friendly.morale -= 3 + ((Friendly.inf_losses + Friendly.cav_losses) / Friendly.size) * 50
                Friendly.suppresion += 1 + (Friendly.player.damage / Friendly.size) * 50
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
while Battle_check == 1:
    jas.easyprint("\nTHE BATTLE HAS NOW TRULY BEGUN\nMAY GOD BE ON OUR SIDE",
                  [["BATTLE PHASE: TURN ", Turn_count, 2], ["MORALE: ", Friendly.player.morale],
                   ["ORGANISATION: ", Friendly.player.organization], ["POSITION: ", Friendly.player.position],
                   ["RECONNAISSANCE: ", Friendly.player.scouting],
                   ["FORTIFICATION: ", Friendly.player.defense],
                   ["SUPPRESSION: ", Friendly.player.suppresion, 1]])
    jas.easyprint("\nENEMY RECON: TURN ", [[Turn_count, 2], ["MORALE: ", Friendly.player.morale - (
                random.randint(0.2, 1.0) * (20 - Friendly.player.scouting) + "-" + Friendly.player.morale + (
                    random.randint(0.2, 1.0) * (20 - Friendly.player.scouting)))],
                  ["ORGANISATION: ", Friendly.player.organization],
                  ["POSITION: ", Friendly.player.position],
                  ["RECONNAISSANCE: ", Friendly.player.scouting],
                  ["FORTIFICATION: ", Friendly.player.defense],
                  ["SUPPRESSION: ", Friendly.player.suppresion, 1]])
    jas.easyprint("ARMY STATISTICS",
                  [["INFANTRY: ", Friendly.player.inf, 2], ["INFANTRY LOSSES: ", Friendly.player.inf_losses, 2],
                   ["CAVALRY: ", Friendly.player.cav, 2], ["CAVALRY LOSSES: ", Friendly.player.cav_losses, 2],
                   ["ARTILLERY: ", Friendly.player.arti, 2], ["ARTILLERY LOSSES: ", Friendly.player.arti_losses, 2],
                   ["TOTAL TROOP COUNT: ", Friendly.player.inf + Friendly.player.cav + Friendly.player.arti, 2],
                   ["TOTAL LOSSES: ",
                    Friendly.player.inf_losses + Friendly.player.cav_losses + Friendly.player.arti_losses, 2]])
    jas.easyprint("ENEMY ARMY STATISTICS",
                  [["INFANTRY: ", Friendly.inf, 2], ["INFANTRY LOSSES: ", Friendly.inf_losses, 2],
                   ["CAVALRY: ", Friendly.cav, 2], ["CAVALRY LOSSES: ", Friendly.cav_losses, 2],
                   ["ARTILLERY: ", Friendly.arti, 2], ["ARTILLERY LOSSES: ", Friendly.arti_losses, 2],
                   ["TOTAL TROOP COUNT: ", Friendly.inf + Friendly.cav + Friendly.arti, 2],
                   ["TOTAL LOSSES: ", Friendly.inf_losses + Friendly.cav_losses + Friendly.arti_losses, 2]])

    Turn_count += 1