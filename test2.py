inside = {
    "num": 0,
    "path": [],
}

something = {
	"count": 0,
	"morale":0,
	"supresion":0,
	"organization":0,
	"cav":0,
	"inf":0,
	"arti":0,
	"scouting":0,
	"position":0,
	"defense":0,
	"commands":0,
	"damage": 0,
	"path": []
}

keys = ["count", "morale", "supresion", "organization", "cav", "inf", "arti", "scouting", "position", "defense", "commands", "damage"]

#something["count"]["num"] += 1
#for i in something.values():
#    print(i)

#avar = something.copy()
#for i in avar.keys():
#    avar[i]["num"]+=10
#for i in avar.values():
#    print(i)

one = something.copy()
one["path"] = something["path"].copy()
something["path"].append(100)
print(something)
print(one)
alist = ["banna", "apple"]
list2 = alist.copy()
print(alist)
print(list2)
alist.append("thethings")
print(alist)
print(list2)
list2.append("something here")
print(alist)
print(list2)