def string_length(S):
		s = []
		if type(S) == str:
			s.append(len(S))
			return s
		if type(S) == list:
			for i in S:
				s.append(len(i))
			return s  

print string_length("Godson")
print string_length("Mia")
print string_length(["Adam", "Frankel"])
print string_length(["Michael", "William", "Smith"])
print string_length("C-sharp")
print string_length(["Fairy", "tale"])