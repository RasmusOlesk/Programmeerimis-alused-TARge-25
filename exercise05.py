def convert_to_fahrenheit(celsius_temperature: float) -> float:
    return celsius_temperature * 1.8 + 32

def convert_to_celsius(fahrenheit_temperature: float) -> float:
    return (fahrenheit_temperature - 32) / 1.8




if __name__ == '__main__':
    unit = input("Määra sisestatava temperatuuri ühik (C/F): ")
    if unit.upper() == "C":
        temperature_celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
        temperature_fahrenheit = convert_to_fahrenheit(temperature_celsius)
        print(f"{temperature_celsius}C on {temperature_fahrenheit}F kraadi. ")
    elif unit.upper() == "F":
        temperature_fahrenheit = float(input("Sisesta temperatuur fahrenheit kraadides: "))
        temperature_celsius = convert_to_celsius(temperature_fahrenheit)
        print(f"{temperature_fahrenheit}F on {temperature_celsius}C kraadi. ")
    else:
        print(f"Sisestatud tundmatu temperatuuri ühiku - {unit}")
        print("programm toetab C - Celsius ja F - Fahrenheit kraade")