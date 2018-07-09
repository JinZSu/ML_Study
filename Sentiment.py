

class Sentiment:
	def __init__(self):
		# self.text = input_text
		self.dictionary={}


	# def break_it_down(self,own_text):
	# 	self.text=own_text
	# 	new_text = []
	# 	words = []
	# 	character = []
	# 	for sentence in self.text:
	# 		for word in sentence:
	# 			if (word == '.' or word == '!' or word == '?'):
	# 				p =''.join(character)
	# 				words.append(p)
	# 				character=[]
	# 				new_text.append([words])
	# 				words = []
	# 			elif (word.isalpha()):
	# 				character.append(word)
	# 			elif (word == ' '):
	# 				p =''.join(character)
	# 				words.append(p)
	# 				character=[]
	# 	self.text = new_text

	def break_it_down(self,own_text):
		print hi


	@property
	def dict(self):
		return self.dictionary 

	@dict.setter
	def dict(self,d1,d2):
		self.dictionary[d1] = d2

	def print_data(self):
		for i in self.dictionary:
			print i , '\n'

	def trainning(self):
		new_text = []
		print self.text.strip("\r\n").split('.,')











if __name__ == "__main__":
	Sample_Text=open("Sample_Text.csv",'r')
	data = Sentiment()
	for i in Sample_Text:
		a = i.strip("\r\n")
		a = a.split(",")
		data.dict[a[0]] = a[1]
	# data.trainning()
	data.print_data()
	# own_text=input("Input the text message that has been bothering you for decates.") #This will make a great APP for WHAT DID SHE/HE MEAN BY THIS TEXT?!


