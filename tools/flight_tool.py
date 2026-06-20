import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVATIONSTACK_API_KEY")

def search_flight(query):
    print(">>> Flight Search Processing...")

    #url = "http://api.aviationstack.com/v1/flights"
    params = {"access_key":API_KEY,"limit":5}

    response = requests.get(url,params=params)

    data = response.json()
    print(data)

    flights = []

    for flight in data["data"][:5]:
        airline = flight.get("airline",{}).get("name","Unknown")
        departure = flight.get("departure",{}).get("airport","Unknown")
        arrival = flight.get("arrival",{}).get("airport","Unknown")
        status = flight.get("flight_status","Unknown")

        flights.append(
            f"""
            Airline : {airline}
            Departure : {departure}
            Arrival : {arrival}
            Status : {status}
            """
        )
        print(flights)
        return "\n".join(flights)