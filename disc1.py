# Question 1(i)
# Temperature Classifier: Using a function, 
# write a Python script that takes a temperature as input and classifies it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

#answer
def temperature ():
    temperature = float(input('Enter the temperature: '))
    
    if temperature < 0:
        print(f"It is Freezing")
        
    elif temperature >= 0 and temperature <= 10:
        print(f"It is cold")
        
    elif temperature >=11 and temperature <= 20:
        print(f"It is Moderate")
        
    elif temperature >= 21 and temperature <= 30:
        print (f"It is Warm")
        
    else:
        print(f"It is Hot")
    
temperature()
    
    
    
    
    
    # Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. 
# What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and 
# provide the answer in 1 decimal place

def volume_of_a_sphere():
    import math
    pie = math.pi
    radius = float(input("Enter the radius of the sphere: "))
    formula = radius*(4/3)*pie*radius**2
    print(f"The volume of a sphere with radius {radius} is {formula:.1f}: ")
    
volume_of_a_sphere()