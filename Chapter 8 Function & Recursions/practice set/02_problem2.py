#Write a python program using function to convert Celsius to Fahrenheit.

#NOTE: METHOD 1 by ME.
cel=float(input("Enter the temp in Celsius: "))

def fah(cel):
    fahrenheit = (9/5 * cel)+ 32
    print(f"{fahrenheit} °F")

fah(cel)



#NOTE: METHOD 2 by harry.
def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)} °C")