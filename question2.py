# Question 2(i)

# Define a function named calculate_bmi that takes a
# person's weight (in kilograms) and height (in 
# meters) as parameters and returns their BMI. (BMI = weight/height) 
# Calculate and sen their BMI category: 
# Below 18.5: "Underweight" 
# 18.5 to 24.9: "Normal weight" 
# 25 to 29.9: "Overweight" 
# 30 or above: "Obese" 
def calculate_bmi ():
    #BMI = (weight/height)
   # weight = ('In kilograms')
   # height = ('In meters')
    
    weight = float(input('Enter the weight in kiolgrams: '))
    height = float(input('Enter the height in meters: '))
    BMI= (weight/height)
    
    if BMI < 18.5:
        print('You are  Underweight')
        
    elif BMI >= 18.5 and BMI<= 24.9:
        print ('You have a Normal Weight')
        
    else:
        print ('You are Obese')
    
calculate_bmi ()
    





# Question 2(ii)
# Use a function to calculate the volume of a cylinder V = π r2 h. 
# Choose a function name in line with what you want to 
# achieve. Radius r and height h should be in parameters.
# Make sure you use the real pie value (import math)

def volume_of_a_cylinder():
    import math
    pie = math.pi
    r= ('radius')
    h = ('height')
    h = float(input('Enter the height :'))
    r = float(input('Enter the radius :'))
    V = (pie*r**2*h)
    
    print(f'The vloume of the cylinder with radius{r} and height {h} is :{V}')
volume_of_a_cylinder()
    