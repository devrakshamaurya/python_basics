tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
print(tea_varities[0])
print(tea_varities[-1])
print(tea_varities[:2])

tea_varities[3] = "Herbal"
print(tea_varities)

tea_varities[1:2] = ["Lemon"]
print(tea_varities)

tea_varities[1:3] = ["Green", "Masala"]
print(tea_varities)

#by using loop

for tea in tea_varities:
    print(tea)

for tea in tea_varities:
    print(tea, end="-")

if "Oolong" in tea_varities:
    print("I have Oolong tea")   


#.append method(adding value)

tea_varities.append("Oolong")    
print(tea_varities)
if "Oolong" in tea_varities:
    print("I have Oolong tea")

#.pop (to remove last value)

tea_varities.pop()
print(tea_varities)

#.remove (to remove particular value)

tea_varities.remove("Black")
print(tea_varities)

#.insert (to insert value)

tea_varities.insert(1, "Black")
print(tea_varities)


#related to loops
#list comprehension

squared_num = [x**2 for x in range (10)]
print(squared_num)

cube_num =[y**3 for y in range (5) ]
print(cube_num)

    


