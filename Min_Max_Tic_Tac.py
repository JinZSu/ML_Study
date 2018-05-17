import sys

sys.setrecursionlimit(2000)

#Min_Max Algo for Tic Tac Toe

def win(Grid,value1):    #Checking the Condition of the Tic Tac Toe
	ver1=0
	ver2=0
	ver3=0
	dag=0
	for i in range(3):
		if (Grid [i][i] == value1):
			dag +=1
		if (Grid [0][i] == value1):
			ver1+=1
		if (Grid [1][i] == value1):
			ver2+=1
		if (Grid [2][i] == value1):
			ver3+=1
	if (Grid [0][2] == value1 and Grid [1][1] == value1 and Grid [2][0] == value1):
		return True
	if (Grid [0] == [value1,value1,value1]):
		return True
	if (Grid [1] == [value1,value1,value1]):
		return True
	if (Grid [2] == [value1,value1,value1]):
		return True
	if (ver3 ==3 or ver2 ==3 or ver1 ==3 or dag ==3):
		return True

	return False


def print_Grid(Grid):  #Print the grid
	print("*"*12)
	for column in Grid:
		for row in column:
			print(row , " " ,end = "")
		print('\n')
	print("*"*12)

def tie(Grid):        #Check if there is a tie
	total_length=0
	for column in Grid:
		for row in column:
			if (row =="X" or row =="o"):
				total_length+=1
	if (total_length == 9):
		print("There are no winners")
		return True

def cal_math(Grid):
	Grid_X=Grid
	print("*"*12)
	print(Grid_X)
	print("*"*12)
	for column in Grid_X:
		for row in column:
			if (row !="X" or row !="o"):
				row = "o"
				if win(Grid_X,"X"):
					return -10
				elif win(Grid_X,"o"):
					return 10
				elif tie(Grid_X):
					return 0



def Terminator(Grid):
	for column in Grid:
		for row in column:
			if (row !="X" or row !="o"):
				row = cal_math(Grid)
	rangex,rangey,score = 0,0,0
	for i in range(3):
		for j in range(3):
			if (isinstance(Grid[i][j], int)):
				if (Grid[i][j] >= score):
					score = Grid[i][j]
					rangex,rangey = i ,j

	Grid[rangex][rangey] = "o"
	print("I'll be Back")

if __name__ == "__main__":
	Grid_Now = [[0,0,0],[0,0,0],[0,0,0]]
	human=True
	print("Will you fight the Terminator? input: True or False")
	human=input()
	while not win(Grid_Now,"X") and not win(Grid_Now,"o") and not tie(Grid_Now):
		print_Grid(Grid_Now)
		print("Cordinates for X")
		print("X axis")
		cordxx=int(input())
		print("Y axis")
		cordxy=int(input())	
		Grid_Now[cordxy-1][cordxx-1] = "X"	
		print_Grid(Grid_Now)
		if human:
			print("Cordinates for o")
			print("X axis")
			cordxx=int(input())
			print("Y axis")
			cordxy=int(input())	
			Grid_Now[cordxy-1][cordxx-1] = "o"
		elif not win(Grid_Now,"X") and not win(Grid_Now,"o") and not tie(Grid_Now):
			Terminator(Grid_Now)
	print_Grid(Grid_Now)
