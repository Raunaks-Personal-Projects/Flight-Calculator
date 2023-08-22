# Import Variables
from geopy.geocoders import Nominatim # Pulls Locations
from geopy.exc import GeocoderTimedOut, GeocoderServiceError # Error Handling
from geopy.distance import geodesic # Distance Calculations

# The following function pulls the coordinates (latitude and longitude) for a city.
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_calculator") # Initializes Variable Geolocator
    try:
        location = geolocator.geocode(city_name)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except (GeocoderTimedOut, GeocoderServiceError):
        return None

# This next function calculates the distance between two sets of coordinates
def calculate_distance(city1_coords, city2_coords):
    return geodesic(city1_coords, city2_coords).miles

# Finally, this function calculates the flight's time given a speed defined by the user.
def calculate_time(speed, distance):
    totalMinutes = (distance/speed*60)
    hours = int(totalMinutes // 60)
    minutes = int(totalMinutes % 60)
    return (f"Given your distance and speed, your journey would take about {hours} hours and {minutes} minutes. Note that there are many variables that can affect this result, such as on-ground traffic and delays, as well as turbulence/non-straight paths in the air.")


# Now that we have defined our functions, we can start the main section of the program. 
# This next bit takes the user's input and inputs them into our functions.

    
# Get the coordinates for the cities 

while True:
    city1 = input("Enter the first city: ")
    city1_coords = get_coordinates(city1)
    if city1_coords: #This command checks if the coordinate exists and handles errors. 
        break
    else:
        print(f"Sorry, {city1} could not be verified. Please try again!")

while True:
    city2= input ("Enter the second city: ")   
    city2_coords = get_coordinates(city2)
    if city2_coords:
        break
    else:
        print(f"Sorry, {city2} could not be verified. Please try again!")

#Check for the Plane's speed, and make exceptions for errors.
while True:
    try:
        speed = float(input ("Enter the plane's speed as a number (mph): "))
        break
    except (ValueError):
        print("Sorry, that wasn't a valid input. Try again!")


# Return the distance between the cities
if city1_coords and city2_coords:
    distance = calculate_distance(city1_coords,city2_coords)
    time = calculate_time(speed, distance)
    print(f"The distance between {city1} and {city2} is {distance:.2f} miles. ")
    print(time)
else:
    print(f"Sorry, something went wrong. Here are the inputs you provided: {city1}, {city2}, {speed}. Try again!")


#Ideas for Improvement
#1. Infinite Loop with an Exit Command
#2. GUI
