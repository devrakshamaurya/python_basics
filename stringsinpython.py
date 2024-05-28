chai = "Masala Chai"
first_char = chai[0]
print(first_char)

chai = "Masala Chai"
slice_chai = chai[0:5]
print(slice_chai)

#number list

num_list = "0123456789"
num_list[:5]
print(num_list[:5])


num_list = "0123456789"
num_list[:4]
print(num_list[:4])


num_list = "0123456789"
num_list[0:7:2]
print(num_list[0:7:2])

#lower case

chai = 'Masala chai'
print(chai.lower())

#upper case

chai = 'Masala chai'
print(chai.upper())

#stripping

chai = "    Masala Chai   "
print(chai.strip())

#replace
chai = "Masala Chai"
print(chai.replace("Masala", "Ginger"))


#split
chai ="Lemon, Ginger, Mint, Masala"
print(chai.split())

chai ="Lemon, Ginger, Mint, Masala"
print(chai.split(", "))

#find
chai = "Masala Chai"
print(chai.find("Chai"))

chai = "Masala Chai"
print(chai.find("chai"))

#count
chai = "Masala Chai Chai Chai Chai"
print(chai.count("Chai"))

#format
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))

#join methods
chai_variety = ["Lemon", "Masala", "Ginger"]
print(chai_variety)
print("".join(chai_variety))
print("-".join(chai_variety))
print(" ".join(chai_variety))
print(", ".join(chai_variety))

#forloop
chai = "Masala Chai"
print(chai)
for letter in chai:
    print(letter)

#questions
chai = "Masala Chai"
print("Masala" in chai)
print("Masalaaa" in chai)





