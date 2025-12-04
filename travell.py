import sys
if (sys.argv) == 4:
    print("User input given")
    script_name = sys.argv[0]
    didtance_travelled = float(sys.argv[1])
    fuel_used = float(sys.argv[2])
    mileage = float(sys.argv[3])

else:
    print("User input not given")
    script_name = sys.argv[0]
    distance_travelled = 3.0
    fuel_used = 2.0
    mileage = 40.0

    print("Didtance Traveeled km:", distance_travelled)
    print("Fuel Used liters:", fuel_used)
    print("Mileage km/liter:", mileage)