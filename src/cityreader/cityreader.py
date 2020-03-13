# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self,name,lat,lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"Name: {self.name}, Lat: {self.lat}, Lon: {self.lon}"



# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
cities = []

def cityreader(cities=[]):
    with open('cities.csv','r') as csv_file:
      csv_reader = csv.reader(csv_file)

      ## GETS THE FIRST LINE
      properties = next(csv_reader)

      ## GRABS THE INDEX OF THE PROPERTIES I NEED
      name_index = properties.index("city")
      lat_index = properties.index("lat")
      lon_index = properties.index("lng")

      ## LOOPS THROUGH THE REST  - SKIPPING THE FIRST_ONE
      for line in csv_reader:
        cities.append(City(line[name_index],float(line[lat_index]),float(line[lon_index])))
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print((c.name,c.lat, c.lon))

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

(lat1,lon1) = input("First coordinate -> ").split()
(lat2,lon2) = input("Second coordinate -> ").split()

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  min_x = min(float(lat1),float(lat2))
  max_x = max(float(lat1),float(lat2))
  min_y = min(float(lon1),float(lon2))
  max_y = max(float(lon1),float(lon2))

  within = []
  for city in cities:
    # Can not use range with floats
    # if city.lat in range(float(lat1),float(lat2)) and city.lon in tange(float(lon1),float(lon2)):
    #   within.append(cities)
    if city.lat > min_x and city.lat < max_x and city.lon > min_y and city.lon < max_y:
      within.append(city)

  return within

cityreader_stretch(lat1,lon1,lat2,lon2,cities)