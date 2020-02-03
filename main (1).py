'''
float --> float
Ask user for angle in degreees and return sine, cosine, and tangent of that angle
'''
import math

#ask for user input
ang1 = float(input("Please enter an angle in degrees: "))

#convert degrees to radians
ang = ang1 * ((math.pi)/180)

#compute the functions
sin  = math.sin(ang)
cos = math.cos(ang) 
tan = math.tan(ang)  

print("sin is", sin, "cos is" , cos, "tan is", tan)
