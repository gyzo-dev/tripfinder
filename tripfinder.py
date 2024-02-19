from math import radians, sin, cos, sqrt, atan2

class Stop:
    def __init__(self, stop_id, name, latitude, longitude):
        self.stop_id = stop_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class Route:
    def __init__(self, route_id, route_name, route_order):
        self.route_id = route_id
        self.route_name = route_name
        self.route_order = route_order

stops = [
    Stop(1, "Grand Terminal", 13.7904833, 121.0611499),
    Stop(2, "Balagtas", 13.7963729, 121.0705508),
    Stop(3, "SM Hypermarket", 13.791746, 121.0701396),
    Stop(4, "BSU Alangilan", 13.7860755, 121.0689882),
    Stop(5, "De Joya Subdivision", 13.780159, 121.067798),
    Stop(6, "SSS Batangas", 13.775601, 121.066424),
    Stop(7, "Don Ramos/STI Batangas", 13.770448, 121.065199),
    Stop(8, "Regional Hospital", 13.767757, 121.063368),
    Stop(9, "Hilltop", 13.764847, 121.060116),
    Stop(10, "Hilltop/Lyceum", 13.763936, 121.064392),
    Stop(11, "P. Herrerra/Ferry Rd.", 13.762088, 121.063940),
    Stop(12, "Noble", 13.760009, 121.063037),
    Stop(13, "Lt. Col. Danilo S. Atienza/Evangelista", 13.758197, 121.060687),
    Stop(14, "Rizal Ave./Lt. Col. Danilo S. Atienza", 13.756454, 121.060654),
    Stop(15, "Rizal Ave./P. Burgos", 13.756414, 121.058703),
    Stop(16, "Citimart Batangas", 13.756329, 121.057703),
    Stop(17, "P. Zamora", 13.756060, 121.057255),
    Stop(18, "M.H. Del Pilar", 13.753379, 121.056031),
    Stop(19, "Bago", 13.750450, 121.056225),
    Stop(20, "Cuta", 13.750108, 121.053577),
    Stop(21, "Coliseum/BSU Main Gate 2", 13.753512, 121.052358),
    Stop(22, "BSU Main Gate 1", 13.755439, 121.053052),
    Stop(23, "Luma (Evangelista)", 13.757413, 121.055526),
    Stop(24, "Baymall", 13.758580, 121.056870),
    Stop(25, "Jollibee D. Silang", 13.759336, 121.058102),
    Stop(26, "Miss Philippines", 13.760778, 121.057642),
    Stop(27, "Lawas", 13.762982, 121.057707),
    Stop(28, "Lyceum/Compark", 13.764767, 121.064654),
    Stop(29, "Don Ramos Northbound", 13.770472, 121.065536),
    Stop(30, "Balagtas Rotonda", 13.797745, 121.071150),
    Stop(31, "SM Batangas Front", 13.755887, 121.070682),
    Stop(32, "Total Gulod", 13.761238, 121.073687),
    Stop(33, "Gov. Antonio Carpio Rd.", 13.768476, 121.070958),
    Stop(34, "Don Ramos", 13.769630, 121.065737),
    Stop(35, "Lumang Palengke (D. Silang)", 13.757084, 121.055968),
    Stop(36, "SM Batangas Side Unloading", 13.756571, 121.068995),
    Stop(37, "Mabini", 13.761741, 121.057393),
    Stop(38, "Petron Bauan", 13.790629, 121.009616),
    Stop(39, "Shell San Pascual", 13.789260, 121.016481),
    Stop(40, "WalterMart San Pascual", 13.788327, 121.020084),
    Stop(41, "San Pascual Public Market", 13.787714, 121.021262),
    Stop(42, "San Pascual National High School", 13.785335, 121.025394),
    Stop(43, "San Pascual Baylon Parish Church", 13.783174, 121.029011),
    Stop(44, "Caltex San Pascual", 13.782337, 121.030908),
    Stop(45, "Santa Rita Karsada Brgy. Hall", 13.779296, 121.038843),
    Stop(46, "Batangas Provincial Sports Complex", 13.775633, 121.044761),
    Stop(47, "AMA Computer Colleges Bolbok", 13.774044, 121.047022),
    Stop(48, "Bolbok Brgy. Hall", 13.772487, 121.049198),
    Stop(49, "Provincial Road/Diversion Road Westbound", 13.771023, 121.051021),
    Stop(50, "Petron Calicanto", 13.768442, 121.053359),
    Stop(51, "Calicanto", 13.766863, 121.054282),
    Stop(52, "Caedo", 13.765113, 121.055458),
    Stop(53, "WalterMart Batangas/Lawas", 13.763691, 121.056644),
    Stop(54, "DJPMM Access Road", 13.755597, 121.051903),
    Stop(55, "PPA Batangas", 13.765286, 121.050621),
    Stop(56, "Acacia", 13.767878, 121.048427),
    Stop(57, "Diversion Road South", 13.770964, 121.050676),
    Stop(58, "Bauan Public Market", 13.791876, 121.010137),
    Stop(59, "Filipinas Funeral Home Bauan", 13.793416, 121.008616),
    Stop(60, "BPI Bauan", 13.791439, 121.007340),
    Stop(61, "Bauan Plaza", 13.790175, 121.007750),
    Stop(62, "Nuciti Central", 13.759965, 121.057548),
    Stop(63, "Traders", 13.758284, 121.057923)
]

routes = [
    Route(1, "Batangas City Proper - Balagtas", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 9, 28, 29, 6 , 5, 4, 3, 2, 30, 1]),
    Route(2, "Batangas City Proper - Capitolio", [31, 32, 33, 34, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 35, 24, 25, 37, 27, 9, 28, 34, 33, 32, 36, 31]),
    Route(3, "Batangas City - Bauan", [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 62, 63, 16, 17, 18, 19, 20, 21, 54, 55, 56, 57, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 58, 59, 60, 61, 38])
]

def haversine_distance(coord1, coord2):
    # Convert latitude and longitude from decimal degrees to radians
    lat1, lon1 = radians(coord1.latitude), radians(coord1.longitude)
    lat2, lon2 = radians(coord2.latitude), radians(coord2.longitude)
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    radius_of_earth = 6371  # Radius of Earth in kilometers
    distance = radius_of_earth * c
    return distance

def find_nearest_stop(stops, current_location):
    nearest_stop = None
    min_distance = float('inf')
    for stop in stops:
        distance = haversine_distance(current_location, stop)
        if distance < min_distance:
            min_distance = distance
            nearest_stop = stop
    return nearest_stop

def dijkstra(graph, start, end):
    # Initialize distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Initialize previous nodes dictionary
    previous = {node: None for node in graph}

    unvisited = set(graph)

    while unvisited:
        # Get the node with the minimum distance
        current = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current)

        # If the end node is reached, construct the path and return
        if current == end:
            path = []
            while current is not None:
                path.insert(0, current)
                current = previous[current]
            return path

        for neighbor in graph[current]:
            # Calculate the distance from the start node to the neighbor
            dist = distances[current] + haversine_distance(current, neighbor)
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                previous[neighbor] = current

    return None  # No path exists

def find_route(stops, routes, start_point, destination_point):
    # Find the nearest stops to the start and destination points
    nearest_start = find_nearest_stop(stops, start_point)
    nearest_destination = find_nearest_stop(stops, destination_point)

    # Initialize distances and previous nodes dictionaries
    distances = {stop: float('inf') for stop in stops}
    previous_stop = {stop: None for stop in stops}
    route_names = {stop: [] for stop in stops}

    # Initialize starting stop and destination stop
    current_stop = nearest_start
    end_stop = nearest_destination

    # Initialize priority queue for stops to visit
    unvisited = set(stops)

    # Initialize distances for start and destination stops
    distances[nearest_start] = 0

    while unvisited:
        # Find the stop with the smallest distance
        current_stop = min(unvisited, key=lambda stop: distances[stop])

        # Remove current stop from unvisited
        unvisited.remove(current_stop)

        # Stop searching if destination is reached
        if current_stop == end_stop:
            break

        # Explore neighboring stops
        for route in routes:
            if current_stop.stop_id in route.route_order:
                route_names[current_stop].append(route.route_name)

                # Find index of current stop in route order
                current_index = route.route_order.index(current_stop.stop_id)

                # Explore stops before current stop
                for i in range(current_index - 1, -1, -1):
                    neighbor_stop_id = route.route_order[i]
                    neighbor_stop = next((stop for stop in stops if stop.stop_id == neighbor_stop_id), None)
                    if neighbor_stop:
                        # Calculate distance to neighbor stop
                        dist_to_neighbor = haversine_distance(current_stop, neighbor_stop)
                        alt_distance = distances[current_stop] + dist_to_neighbor

                        # Update distance if shorter path is found
                        if alt_distance < distances[neighbor_stop]:
                            distances[neighbor_stop] = alt_distance
                            previous_stop[neighbor_stop] = current_stop
                            route_names[neighbor_stop] = route_names[current_stop][:]  # Copy route names

                # Explore stops after current stop
                for i in range(current_index + 1, len(route.route_order)):
                    neighbor_stop_id = route.route_order[i]
                    neighbor_stop = next((stop for stop in stops if stop.stop_id == neighbor_stop_id), None)
                    if neighbor_stop:
                        # Calculate distance to neighbor stop
                        dist_to_neighbor = haversine_distance(current_stop, neighbor_stop)
                        alt_distance = distances[current_stop] + dist_to_neighbor

                        # Update distance if shorter path is found
                        if alt_distance < distances[neighbor_stop]:
                            distances[neighbor_stop] = alt_distance
                            previous_stop[neighbor_stop] = current_stop
                            route_names[neighbor_stop] = route_names[current_stop][:]  # Copy route names

    # Reconstruct the route from start to destination
    route = []
    current_stop = end_stop
    while current_stop is not None:
        route.insert(0, (current_stop, route_names[current_stop]))
        current_stop = previous_stop[current_stop]

    # Return the route
    return route

# Define the starting and destination points
start_point = Stop(35, "Lumang Palengke (D. Silang)", 13.757084, 121.055968)
destination_point = Stop(58, "Bauan Public Market", 13.791876, 121.010137)

# Find and construct the route
trip_route = find_route(stops, routes, start_point, destination_point)
if trip_route:
    print("Starting Point:", start_point.name)
    route_count = 1
    for i, (stop, _) in enumerate(trip_route):
        if i == len(trip_route) - 1:
            print("Destination:", stop.name)
        else:
            current_stop_id = stop.stop_id
            next_stop_id = trip_route[i + 1][0].stop_id
            for j, route_obj in enumerate(routes):
                if current_stop_id in route_obj.route_order and next_stop_id in route_obj.route_order:
                    if i > 0:  # Print stopover before the next route
                        print("Stopover:", stop.name)
                    print("Route {} ({}): {}".format(route_count, j+1, route_obj.route_name))
                    route_count += 1
                    break
else:
    print("No route found")