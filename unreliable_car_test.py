from unreliable_car import UnreliableCar

def main():
    """reliability set to 50% and doing 100 1km drives. odometer shows roughly 50km driven"""
    fiesta = UnreliableCar("Ford Fiesta", 100, 50)
    for x in range(0, 100):
        print(fiesta.drive(1))
    print(fiesta)

main()

