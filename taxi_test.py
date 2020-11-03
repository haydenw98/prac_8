from taxi import Taxi

def main():
    taxi_p = Taxi("Prius 1", 100)
    taxi_p.drive(40)
    print(taxi_p)
    print("The fare is $" + str(taxi_p.get_fare()))
    taxi_p.start_fare()
    taxi_p.drive(100)
    print(taxi_p)
    print("The fare is $" + str(taxi_p.get_fare()))


main()