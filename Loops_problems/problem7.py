#list uniqueness checker
#check if all elements in a list are unique. if a duplicate is found. exit the loop and print the duplicate


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items :
    if item in unique_item:
        print("duplicate: ", item)
        break
    unique_item.add(item)
    