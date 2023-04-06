#SOKOLOV BE KKCO-04-21
#python3 
 
from os import system
from pickle import FALSE, TRUE
from sys import exit


class Map():

	map1 = [
		["#", "#", "#", "#","#", "#", "#", "#","#","#","#","#"], 
		["#", " ", "#", " "," ", " ", " ", " "," "," "," ","#"],
		["#", "H", "#", " ","#", " ", " ", "#","#","#"," ","#"],
		["#", " ", " ", " ","#", " ", " ", "#"," ","#"," ","#"],
		["#", "D", "#", " "," ", "D", "?", "#"," ","#","W","#"],
		["#", "#", "#", "#","#", "#", "#", "#"," ","#","#","#"]]


	map2 = [
		["#", "#", "#", "#","#", "#", "#", "#","#","#","#","#"], 
		["#", "W", "#", " ","#", " ", " ", "D","W","W"," ","#"],
		["#", " ", "#", " "," ", "H", " ", " ","D"," ","D","#"],
		["#", " ", "#", " "," ", " ", " ", " "," ","D"," ","#"],
		["#", "W", "D", "D","D", "D", " ", " ","D"," ","W","#"],
		["#", "#", "#", "#","#", "#", " ", "#"," ","#","#","#"],
		["#", " ", " ", " "," ", " ", " ", " "," "," "," ","#"],
		["#", " ", " ", "S","I", "C", "R", "E","T"," "," ","#"],
		["#", " ", " ", " "," ", " ", " ", " "," "," "," ","#"],
		["#", " ", " ", "R","O", "O", "M", " "," ","W"," ","#"],
		["#", " ", " ", " "," ", " ", " ", " "," "," "," ","#"],
		["#", "8", "=", "D"," ", "(", "◕", "‿","◕",")"," ","#"],
		["#", "#", "#", "#","#", "#", "#", "#","#","#","#","#"]] 
	def printMap(Self,map):	
		map[Self.x][Self.y]="H"
		
		system("clear")
		for row in  map:
			print("")
			for elem in row:
				print(elem, end=' ')


class controltrol(Map):
	takeSecret=FALSE
	
	#типо ищим где начальная позиция H в map
	def werPos(Self,map):

		x=-1
		y=0


		for row in  map:
			#print("")
			x+=1
			#print("x= "+str(x))
			for elem in row:
				
				#print(elem)
				#print(" y= "+str(y))
				if elem=="H":
					#print("x= "+str(x)+" y= "+str(y-1))
					Self.x=x
					Self.y=y
				y+=1
			y=0

    

	def control(Self, map ):
		
		print("\n\nH - 		ИГОРК")
		print("D - 		ОПАСНОСТЬ")
		print("W - 		ПОБЕДА")

		print("\n вы находитесь в комнате, куда пойдёте? (верх(w),лево(a),низ(s),право(d))")
		choice=input(">")

		if choice=="право" or choice=="d" :
			map[Self.x][Self.y]=" "

			if map[Self.x][Self.y+1]=="W":
				Self.win()
			if map[Self.x][Self.y+1]=="D":
				Self.dead("орк отправил вас в небо")	
			if map[Self.x][Self.y+1]=="?":
				Self.takeSecret=True
			if map[Self.x][Self.y+1]!="#":
				Self.y+=1	
			 

		if choice=="лево" or choice=="a":
			map[Self.x][Self.y]=" "

			if map[Self.x][Self.y-1]=="W":
				Self.win()
			if map[Self.x][Self.y-1]=="D":
				Self.dead("орк отправил вас в небо")	
			if map[Self.x][Self.y-1]=="?":
				Self.takeSecret=True	
			if map[Self.x][Self.y-1]!="#":
				Self.y-=1	


		if choice=="низ" or choice=="s":
			map[Self.x][Self.y]=" "

					
			if map[Self.x+1][Self.y]=="W":
				Self.win()
			if map[Self.x+1][Self.y]=="D":
				Self.dead("орк отправил вас в небо")	
			if map[Self.x+1][Self.y]=="?":
				Self.takeSecret=True	
			if map[Self.x+1][Self.y]!="#":
				Self.x+=1	


		if choice=="верх" or choice=="w":
			map[Self.x][Self.y]=" "
			if map[Self.x-1][Self.y]=="W":
				Self.win()
			if map[Self.x-1][Self.y]=="D":
				Self.dead("орк отправил вас в небо")	
			if map[Self.x-1][Self.y]=="?":
				Self.takeSecret=True
			if map[Self.x-1][Self.y]!="#":
				Self.x-=1
		

class Mision(controltrol):
	nowLvl =0
 
	def misionOne(Self):
		print("норд:    эй ты не спишь, ты нарушитель границ, да?")
		print("норд:    надо же тебе было попасть в имперскую засаду. они и нас поймали и ворюгу этого..")
		print("вор:  проклятые братья бури.в скайриме было тихо пока вас сюда не занесло. имеперии не до чего дела не было.")
		print("имперский солдат:    А НУ, ВСЕ ЗАТКНУЛИСЬ")
		print("!повозка остановидась!")
		print("!вор попытался сбежать. но его попвтка была тщетной) *выстрел в колено*!")
		print("имперский солдат:    тебя в списке на казнь нет, кто ты ?")
		nameHero=input("> ")

		print("имперский солдат:    тебя в списке нет. но мы всё равно отрубим теье голову")

		print("!вашу казнь прервал дракон!")

		print("вы пойдёте за имперцец или за братьем бури")

		while True:
			choice=input("> ").lower()

			if choice =="имперец":
				print("вы пошли за имперцем он дал вам оружие")
				Self.misionTwo("имперец")
				exit(0)
			if choice=="бури":
				print("вы пощли за братьем бури он дал вам оружие и ведро")
				Self.misionTwo("бури")
				exit(0)
			else:
				print("введите коректные данные")


	def misionTwo(Self,who):
		Self.nowLvl=1
		Self.who=who
		Self.werPos(Self.map1)

		while True:

			Self.printMap(Self.map1)
			Self.control(Self.map1)

	
	def sicretRoom(Self):
		Self.nowLvl=2
		Self.werPos(Self.map2)
		while True:
			Self.printMap(Self.map2)
			Self.control(Self.map2)

class Game(Mision):

	def presend(Self):
		print("Wedlec Game....\nPRESENT.....\n\n")

		print("""
 _______________________________________
/              SKYRIM                   \ 
\     Golden Ultima Pro Max Platinum    /
 ---------------------------------------
      \                    / \  //\ 
       \    |\___/|      /   \//  \ \ 
            /0  0  \__  /    //  | \ \    
           /     /  \/_/    //   |  \  \  
           @_^_@'/   \/_   //    |   \   \  
           //_^_/     \/_ //     |    \    \  
        ( //) |        \///      |     \     \ 
      ( / /) _|_ /   )  //       |      \     _\ 
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \ 
 (( /// ))      `.   {            }                   /      \  \ 
  (( / ))     .----~-.\        \-'                 .~         \  `. \^-. 
             ///.----..>        \             _ -~             `.  ^-`  ^-_ 
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~ ") 
""")
	def start(Self):
		system("clear")
		Self.presend()
		Self.misionOne()
		#Self.misionTwo("бури")
		

	def dead(Self,why):
		print("GAME OVER")
		print(f"ТЫ не драконорождённый, убит: {why}")
		exit(0)

	def win(Self):
		
		if Self.takeSecret==True and Self.nowLvl==1:
			Self.sicretRoom()
		
		print("YOU ARE WIN")
		
		if Self.who =="имперец":
			print("слава ИМПЕРИИ")
		else:	
			print("слава братьям бури")
		print("вы герой skyrim, о вашем подвиге ходят легенды.....")
		if Self.takeSecret==FALSE:
			print("Help: вы могли попасть в секретную комнату взяв '?' ")
		exit(0)


skyrim= Game()
skyrim.start()