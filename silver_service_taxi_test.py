from silver_service_taxi import SilverServiceTaxi


def main():
    """price per km time 10(fanciness) = 12.30 per km, times the distance drove which is also 10"""
    sstaxi = SilverServiceTaxi("Silver Service Taxi", 100, 10)
    sstaxi.drive(10)
    print(sstaxi)
    print(sstaxi.get_fare())

main()