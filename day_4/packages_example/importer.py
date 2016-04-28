# lns 3 and 4 shows importing modules from packages 
# that is, package.module import ..... 
from A.classes import Animal, Poacher, Tourist 
from A.functions import word_count, sum_of_digits

# another way to import 
import A.functions as func 
import A.classes as classes
# as helps to have a cleaner namespace ~~ see more uses  
# i.e now you can call A.functions as func when you want to use it, see ln 13 

print Animal, word_count 
print classes.Animal, func.word_count
