#find the first non-repeated character 
# given a string, find the first non-repeated character

input_str = "teeter"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break