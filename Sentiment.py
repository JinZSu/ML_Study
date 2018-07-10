

class Sentiment:
	def __init__(self,input_text):
		self.text = input_text
		self.dictionary={}
		self.dataset = []
		self.trainning()

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

	def print_data(self,dataset="dictionary"):
		print 21*"#"
		if (dataset=="dictionary"):
			for i in self.dictionary:
				print self.dictionary[i], '\t',i
		elif (dataset=="text"):
			print self.text
		elif (dataset=="dataset"):
			for i in self.dataset:
				print i
		print 21*"#"

	def transfer_text_to_dict(self):
		for i in self.text:
			a = i.strip("\r\n")
			a = a.split(",")
			self.dictionary[a[0]] = a[1]
		print "Giving meaning to the text"

	def give_words_value(self,number=3):
		for i in self.dictionary:
			a=i.split(" ")
			remove=[]
			for j in a:
				if (len(j)<3):
					remove.append(j)
			for x in remove:
				a.remove(x)
			self.dataset.append((a,self.dictionary[i]))
		self.print_data("dataset")


	def trainning(self):
		print "Trainning Ellie Version 1.0 to understand what it means to be Human"
		self.transfer_text_to_dict()
		self.print_data()
		self.give_words_value()

	def break_it_down(self,own_text):
		print "What is the text that you wish for me to interpret?"


	@property
	def dict(self):
		return self.dictionary

	@dict.setter
	def dict(self,d1,d2):
		self.dictionary[d1] = d2

#####################

if __name__ == "__main__":
	Sample_Text=open("Sample_Text.csv",'r')
	data = Sentiment(Sample_Text)
	# own_text=input("Input the text message that has been bothering you for decates.") #This will make a great APP for WHAT DID SHE/HE MEAN BY THIS TEXT?!


