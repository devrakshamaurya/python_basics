#fruit ripeness checker
# determine if a fruit is a ripe, overripe, or unripe based on its color.(e.g., Banana: Green -unripe,  Yellow-Ripe, Brown-Overripe)

fruit = "Banana"
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    else:
        print("Overripe")        