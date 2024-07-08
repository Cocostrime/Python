Days1={"Monday","Tuesday","Wednesday","Thursday","Sunday"}
Days2={"Friday","Thursday","Sunday","Saturday"}
set1={"Devansh","bob","castle"}
set2={"castle","dude","emyway"}
set3={"fuson","gaurav","castle"}

#union
print(Days1|Days2)
print(Days1.union(Days2))

#difference
print(Days1-Days2)
print(Days1.difference(Days2))
print(Days2.difference(Days1))

#intersection
print(Days1&Days2)
print(Days1.intersection(Days2))

set1.intersection_update(set2,set3)
print(set1)

#symmetric difference
a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b
c=a.symmetric_difference(b)
print(c)


#comparisions
Days3={"Monday","Tuesday","Wednesday","Thursday","Sunday"}
Days4={"Monday","Tuesday"}
Days5={"Monday","Tuesday","Friday"}

#Days3 is subset of Days4
print(Days3>Days4)  #true
#prints false since Days3 is not a subset of Days4
print(Days3<Days4)    #false
#prints false since Days4 and Days5 are not equal
print(Days4==Days5)   #false