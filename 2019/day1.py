import sys

def fuel_sum(filename):
    with open(filename,'r') as fh:
        data=[int(line.rstrip('\n')) for line in fh]
    return sum([int(mass/3)-2 for mass in data])

def fuel_for_fuel(filename):
    with open(filename,'r') as fh:
        data=[int(line.rstrip('\n')) for line in fh]

    totalFuelForFuel = 0
    for f in data:
        sumFuelForFuel = 0
        while f > 8:
            f = int(f/3)-2
            sumFuelForFuel += f
            # print(f"{f}:{sumFuelForFuel}")
        totalFuelForFuel += sumFuelForFuel

    return totalFuelForFuel
        
if __name__ == "__main__":
    fuelfile = sys.argv[1]
    fuelCounterUpper = fuel_sum(fuelfile) 
    print(f"The total amount of fuel required for the Fuel Counter-Upper is {fuelCounterUpper}")

    fuelRocketEquationDC = fuel_for_fuel(fuelfile)
    print(f"The total amount of fuel required for the Fuel Rocket Equation Double Checker is {fuelRocketEquationDC}")
    
