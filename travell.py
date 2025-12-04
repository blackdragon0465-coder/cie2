import sys

if len(sys.argv) == 4:
    print("User input given")

    script_name = sys.argv[0]
    distancetravelled = float(sys.argv[1])
    fuelused = float(sys.argv[2])
    mileage = float(sys.argv[3])

else:
    print("User input not given")

    script_name = sys.argv[0]
    distancetravelled = 3.0
    fuelused = 2.0
    mileage = 40.0

print("Distance Travelled km:", distancetravelled)
print("Fuel Used liters:", fuelused)
print("Mileage km/liter:", mileage)
