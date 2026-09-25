# Water Level Indicator and Controller

level = int(input("Enter water level (0-100%): "))

if level < 25:
    print("Water Level: LOW")
    print("Pump: ON")

elif level < 50:
    print("Water Level: MEDIUM")
    print("Pump: ON")

elif level < 80:
    print("Water Level: HIGH")
    print("Pump: OFF")

else:
    print("Water Level: FULL")
    print("Pump: OFF")
