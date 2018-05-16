Grid_Now = [[0,0,0],[0,0,0],[0,0,0]]


def win(Grid):
	ver1=0
	ver2=0
	ver3=0
	dag=0
	filled=0
	for i in range(3):
		if (Grid [i][i] == "X"):
			dag +=1
		if (Grid [0][i] == "X"):
			ver1+=1
		if (Grid [1][i] == "X"):
			ver2+=1
		if (Grid [2][i] == "X"):
			ver3+=1
	if (Grid [0][2] == "X" and Grid [1][1] == "X" and Grid [2][0] == "X"):
		return True
	if (Grid [0] == ["X","X","X"]):
		return True
	if (Grid [1] == ["X","X","X"]):
		return True
	if (Grid [2] == ["X","X","X"]):
		return True

	return False


def print_Grid(Grid):
	print("*"*12)
	for column in Grid:
		for row in column:
			print(row , " " ,end = "")
		print('\n')
	print("*"*12)

def tie(Grid):
	total_length=0
	for column in Grid:
		for row in column:
			if (row =="X" or row =="o"):
				total_length+=1
	if (total_length == 9):
		print("There are no winners")
		return True

def cal_math(Grid):
	

def Terminator(Grid):
	GridX=copy.copy(Grid)

	print("I'll be Back")

if __name__ == "__main__":
	Grid_Now = [[0,0,0],[0,0,0],[0,0,0]]
	human=True
	print("Will you fight the Terminator? input: True or False")
	human=input()
	while not win(Grid_Now) or not tie(Grid):
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
		else:
			Terminator(Grid_Now)
	print_Grid(Grid_Now)
