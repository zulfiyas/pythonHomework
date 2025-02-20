def convert_cel_to_far(celsius):
    return celsius * 9/5 + 32

def convert_far_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {round(celsius, 2)} degrees C\n")
    
    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {round(fahrenheit, 2)} degrees F")
    
if __name__ == "__main__":
    main()