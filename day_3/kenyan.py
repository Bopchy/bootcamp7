#  this is a subclass, as it inherits from Person


from person import Person  
class Kenyan(Person): 
#  class Kenyan extends Person 
	
	
	def probe(self, corrupt):
		self.corrupt = corrupt 
		# you must probe kenyan objects to get attirbute corrupt    

	
	def is_corrupt (self):
		if self.corrupt: 
			return "Yes"
		return "No"


