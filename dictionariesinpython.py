chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}
print(chai_types)

print(chai_types.get("Ginger"))

#change dictionary items

chai_types["Green"] = "Fresh"
print(chai_types)

#loop

for chai in chai_types:
    print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

#conditionals

if "Masala" in chai_types:
    print("I have Masala chai")
print(len(chai_types))    

chai_types["Earl Grey"] = "Citrus"
print(chai_types)


#pop

print(chai_types.pop("Ginger"))
print(chai_types)

#.popitem (is used for which value we add at last)

print(chai_types.popitem())
print(chai_types)

#del (for delete)

del chai_types["Green"]
print(chai_types)

tea_shop ={
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}
print(tea_shop)

tea_shop["chai"]
print(tea_shop["chai"])

tea_shop["chai"]["Ginger"]
print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(10)}
print(squared_num)

squared_num.clear()
print(squared_num)


keys = ["Masala", "Ginger", "Lemon"]
print(keys)
default_value ="Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)