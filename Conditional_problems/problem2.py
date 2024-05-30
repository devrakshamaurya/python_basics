#movie ticket pricing
#movie tickets are priced based on age: $12 for adults(18 and above), $8 for children.
#everyone gets a $2 discount on wednesday

age = 6
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket is for you is $", price)
