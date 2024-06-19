from ethiopia_map import ethiopia_map
from SimpleProblemSolvingAgent import SimpleProblemSolvingAgent
# This file calculates the distances between all the cities in the ethiopia_map graph  to their neighbors using the haversine formula and coordinates in the ethiopia_map.locations dictionary.
# It outputs to CalculatedDistances.txt
# The haversine formula calculates the distance between two points on the surface of a sphere.
# The formula is:
# a = sin²(Δlat/2) + cos(lat1).cos(lat2).sin²(Δlong/2)
def haversine(lat1, lon1, lat2, lon2):
    import math

    # convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # haversine formula
    a = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2

    # radius of the earth in kilometers
    radius = 6371

    # calculate the distance
    distance = 2 * radius * math.asin(math.sqrt(a))

    return distance
# Main function - This function is the entry point of the program.
def main():
    # graph of the cities in ethiopia
    graph = ethiopia_map

    # open the output file for writing
    with open("CalculatedDistances.txt", "w") as file:
       
        # loop through each city in the graph
        for city in graph.nodes():
            neighbors = graph.neighbors(city)

            # loop through each neighbor of the city
            for neighbor in neighbors:

                # get the coordinates of the city and its neighbor
                lat1, lon1 = graph.locations[city]
                lat2, lon2 = graph.locations[neighbor]

                # calculate the distance between the city and its neighbor
                distance = haversine(lat1, lon1, lat2, lon2)

                # write the distance to the file
                file.write(f"{city} to {neighbor}: {distance:.2f} km\n")

if __name__ == "__main__":

    main()