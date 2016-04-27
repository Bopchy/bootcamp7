# you can import anything that's addressable 

# shows importing of all the exporter functions
from exporter import super_sum, hello_again, max_min, people 


print super_sum, hello_again, max_min, people 

a = [10, 40, -5, 6, 9, 34, 7]
 
print hello_again ('Joe', 89)
print super_sum (*a)
print max_min (a) 
print hello_again (*people[0])  