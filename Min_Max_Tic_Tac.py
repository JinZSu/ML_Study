import sys

sys.setrecursionlimit(2000)


class grid:
	def __init__(self):
	    self.data = [[0,0,0],[0,0,0],[0,0,0]]
	    self.avaliable = []
	    self.human=True

	def check_win(self,value1):
		ver1=0
		ver2=0
		ver3=0
		dag=0
		for i in range(3):
			if (self.data [i][i] == value1):
				dag +=1
			if (self.data [0][i] == value1):
				ver1+=1
			if (self.data [1][i] == value1):
				ver2+=1
			if (self.data [2][i] == value1):
				ver3+=1
		if (self.data [0][2] == value1 and self.data [1][1] == value1 and self.data [2][0] == value1):
			return True
		if (self.data [0] == [value1,value1,value1]):
			return True
		if (self.data [1] == [value1,value1,value1]):
			return True
		if (self.data [2] == [value1,value1,value1]):
			return True
		if (ver3 ==3 or ver2 ==3 or ver1 ==3 or dag ==3):
			return True
		return False

	def check_avaliable(self):
		for column in range(len(self.data)):
			for row in range(len(self.data)):
				if (self.data [row] [column] !="X" or self.data [row] [column] !="o"):
					if [row,column] not in self.avaliable:
						self.avaliable.append([row,column])

	def move(self,X,Y,player="X"):
		self.check_avaliable()
		if isinstance(self.data [X] [Y],int):
			self.data [X] [Y] = player
			self.avaliable.remove([X,Y])


	def print_grid(self):
		print("*"*12)
		for column in self.data:
			for row in column:
				print(row , " " ,end = "")
			print('\n')
		print("*"*12)

	def finish(self):
		if self.check_win("X") or self.check_win("o") or self.tie():
			return True
		return False

	def tie(self):        #Check if there is a tie
		total_length=0
		for column in self.data:
			for row in column:
				if (row =="X" or row =="o"):
					total_length+=1
		if (total_length == 9):
			print("There are no winners")
			return True
		return False

	def getenemy(self,player="X"):
		if player == "X":
			return "o"
		else:
			return 'X'

	def auto(self,player, depth=0):
		if self.finish() :
			if self.check_win("X") :
				return -10 + depth, None
			elif self.tie():
				return 0, None
			elif self.check_win("o") :
				return 10 - depth, None
		for movecord in self.avaliable:
			X,Y=movecord[0], movecord[1]
			save = self.data [X][Y]
			self.move(X,Y, player)
			opposite = self.getenemy(player)
			self.print_grid()
			val, _= self.auto(opposite, depth+1)
			print(val)
			self.move(X,Y, save)
			self.move(X,Y, save)
		return val, movecord


	def Terminator(self):
		best,move2 = self.auto("o",5)
		X,Y = move2[0],move2[1]
		print(best,X,Y)
		self.move(X,Y,"o")
		print("I'll Be Back")


if __name__ == "__main__":
	Grid_Now = grid()
	human=True
	print("Will you fight the Terminator? input: True or False")
	Grid_Now.human=input()
	while not Grid_Now.finish():
		Grid_Now.print_grid()
		print("Cordinates for X")
		print("X axis")
		cordxy=int(input())
		print("Y axis")
		cordxx=int(input())	
		Grid_Now.move(cordxy,cordxx)
		Grid_Now.print_grid()
		if Grid_Now.human:
			print("Cordinates for o")
			print("X axis")
			cordxx=int(input())
			print("Y axis")
			cordxy=int(input())	
			Grid_Now.move(cordxy,cordxx,"o")
			Grid_Now.print_grid()
		else:
			Grid_Now.Terminator()
		Grid_Now.print_grid()
