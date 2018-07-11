
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
			b=1
			a=i.split(" ")
			remove=[]
			for j in a:
				if (len(j)<3):
					remove.append(j)
			for x in remove:
				a.remove(x)
			if (a[-1][-1]=="?"):   #if the sentence is a question mark then it will be scale?!?!?!?!?!?!
				b=1.039
			elif ( a[-1][-1]=="!"):#if the sentence is a explantation mark then it will be scales less than 3x !!!!!!!!!!
				b=1.097
			a[-1]=a[-1][:-1]
			a = [x.lower() for x in a]
			self.dataset.append((a,int(self.dictionary[i])*b))
		self.print_data("dataset")


	def trainning(self):
		print "Trainning Ellie Version 1.0 to understand what it means to be Human"
		self.transfer_text_to_dict()
		self.print_data()
		self.give_words_value()

	def break_it_down(self,own_text):
		score=0
		b=1
		data_analysis=own_text.split(' ')
		if (data_analysis[-1][-1]=="?"):   #if the sentence is a question mark then it will be scale?!?!?!?!?!?!
			b=1.039
		elif (data_analysis[-1][-1]=="!"):#if the sentence is a explantation mark then it will be scales less than 3x !!!!!!!!!!
			b=1.097
		for i in self.dataset:
			for x in i[0]:
				if x in data_analysis:
					score+=b*i[1]
		if (score>0):
			print "Positive Message: She/He/It might be into you!"
		elif (score<0):
			print "Negative Message: Probably should stay away before she/he/it gets a restraining order"
		else:
			print "Can not determine data base on the dataset available :("
	
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
	own_text = raw_input("Input the text message that has been bothering you for decades:\n") #This will make a great APP for WHAT DID SHE/HE MEAN BY THIS TEXT?!
	data.break_it_down(own_text)
	Sample_Text.close()

