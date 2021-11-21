import artificial_inteligence as AI
import time

ai = AI.AI()
ai.player.arti = 100
ai.player.inf = 100
ai.player.cav = 200
ai.originalset(500)
a = time.time()
b = [[0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
b = ai.settoclass(b)
c = ai.predict(None, 7, 3, True,b, player=True)
print("Ronys computer is an idiot")
print(time.time()-a)
print(c.num)
print(c.i)