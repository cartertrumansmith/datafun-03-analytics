'''
Carter Smith, 44608
'''

#import dependencies
import math
import statistics

#define variables
company_name: str = "Midwest Airlines"
count_active_routes: int = 4
standard_fare_usd: float = 59.99
has_free_checked_baggage: bool = True
destinations: list = ["Kansas City", "Omaha", "Chicago","St. Louis"]
fleet: list = ["Boeing 737","Airbus A320"]
passenger_count_on_flights: list = [193,112,94,125,161,71,83,108,179,164,176,100,82,57,133,154,161]

#define formatted strings
active_flights_string: str = f"Active Routes: {count_active_routes}"
has_free_checked_baggage_string: str = f"Free Checked Bags: {has_free_checked_baggage}"
standard_fare_usd_string: str = f"One Way Standard Fare: ${standard_fare_usd}"

#calculate descriptive statistics
minimum_passengers = min(passenger_count_on_flights)
maximum_passengers = max(passenger_count_on_flights)
total_passengers = sum(passenger_count_on_flights)
flight_count = len(passenger_count_on_flights)
average_passengers = statistics.mean(passenger_count_on_flights)
mode_passengers = statistics.mode(passenger_count_on_flights)
median_passengers = statistics.median(passenger_count_on_flights)
stdev_passengers = statistics.stdev(passenger_count_on_flights)

passenger_stats: str = f"""
Flight Statistics:
    Least Passengers: {minimum_passengers}
    Most Passengers: {maximum_passengers}
    Total Passengers: {total_passengers}
    Flight Count: {flight_count}
    Average Passengers: {average_passengers}
    Mode of Passengers: {mode_passengers}
    Median Passengers: {median_passengers}
    Standard Deviation: {stdev_passengers}
"""

#define byline string
byline: str = f"""
{company_name}
    {active_flights_string}
    {has_free_checked_baggage_string}
    {standard_fare_usd_string}
    {passenger_stats}
"""

#define main function
def main():
    print(byline)

#conditional script execution
if __name__ == '__main__':
    main()
