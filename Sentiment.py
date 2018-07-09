
class Sentiment:
	def __init__(self,input_text):
		self.text = input_text

	def break_it_down(self):
		new_text = []
		for word in self.text:
			print word
	
	def print_data(self):
		print self.text











if __name__ == "__main__":
	own_text_bool=input("Input your own text? True or False")
	if own_text_bool:
		own_text=input("Input the text message that has been bothering you for decates.") #This will make a great APP for WHAT DID SHE/HE MEAN BY THIS TEXT?!
		data=Sentiment(own_text)
	else:
		Sample_Text=open("Sample_Text",r)
		data=Sentiment(Sample_Text)
		data.break_it_down()
