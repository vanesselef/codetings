'''
float --> string
Takes a temperature in celcius and returns the state of water
'''

def water_temperature(cel):

    if cel > 100:
        return "gassed up"
    elif cel <= 0:
        return "ice ice baby"
    else:
        return "liquid"
    


degrees = int(input("Enter a temperature in Celsius: "))
print(water_temperature(degrees))
