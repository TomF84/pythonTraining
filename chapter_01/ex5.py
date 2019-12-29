name = 'Tom C. Fahner' 
age = 35
height = 188 # cm
height_in = round(height / 2.54)
weight = 82.5 # kg
weight_lbs = round(weight * 2.20462262)
eyes = 'Blue/grey'
teeth = 'White'
hair = 'Blond'

print(f"Let's talk about {name}.")
print(f"He's {height} cm, {height_in} in tall.")
print(f"He's {weight} kg, {weight_lbs} lbs heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
