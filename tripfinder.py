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
    Stop(1, "Batangas City Grand Terminal", 13.7904833, 121.0611499),
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
    Stop(49, "Provincial Road/Diversion Road Eastbound", 13.771023, 121.051021),
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
    Stop(63, "Traders", 13.758284, 121.057923),
    Stop(64, "SM City Lipa Grand Transport Terminal", 13.9532638, 121.1619836),
    Stop(65, "Lipa Medix Medical Hospital", 13.948288, 121.156712),
    Stop(66, "Big Ben Complex", 13.942680, 121.152736),
    Stop(67, "Robinsons Place Lipa", 13.941499, 121.150845),
    Stop(68, "De La Salle Lipa", 13.941431, 121.148384),
    Stop(69, "Tambo", 13.940958, 121.140409),
    Stop(70, "Lipa Town Center", 13.943585, 121.134399),
    Stop(71, "Fernando Air Base", 13.944026, 121.128144),
    Stop(72, "Mataasnakahoy Junction", 13.939633, 121.123079),
    Stop(73, "Banaybanay Elementary School", 13.935386, 121.118358),
    Stop(74, "Banaybanay Crossing", 13.929005, 121.110960),
    Stop(75, "Banaybanay II", 13.920718, 121.106022),
    Stop(76, "Banaybanay I", 13.901823, 121.104581),
    Stop(77, "San Jose Crossing", 13.887197, 121.104563),
    Stop(78, "San Jose", 13.878619, 121.103907),
    Stop(79, "San Jose Public Market", 13.877789, 121.100168),
    Stop(80, "Calansayan", 13.858692, 121.093871),
    Stop(81, "Batangas-San Jose Boundary", 13.841150, 121.086909),
    Stop(82, "Concepcion", 13.833046, 121.082630),
    Stop(83, "Mahabang Parang", 13.821458, 121.075439),
    Stop(84, "Sorosoro Karsada", 13.804477, 121.076146),
    Stop(85, "Andok's Balagtas", 13.798294, 121.071250),
    Stop(86, "Diversion Northbound", 13.771527, 121.051143),
    Stop(87, "Montenegro/Tree House", 13.777106, 121.053580),
    Stop(88, "Camillus", 13.782088, 121.056445),
    Stop(89, "Banaba South", 13.785338, 121.058608),
    Stop(90, "XentroMall Batangas", 13.788855, 121.060292),
    Stop(91, "Crossing Calamba Terminal", 14.205795, 121.153311),
    Stop(92, "SM City Calamba South Parking", 14.204063, 121.153944),
    Stop(93, "Real", 14.200608, 121.151222),
    Stop(94, "Real Exit", 14.194645, 121.142848),
    Stop(95, "Turbina-Bicol Bus Terminal", 14.188019, 121.136776),
    Stop(96, "Turbina", 14.185551, 121.136564),
    Stop(97, "NU Laguna", 14.178562, 121.137044),
    Stop(98, "Carmelray", 14.171500, 121.137497),
    Stop(99, "Ashton Fields", 14.168996, 121.137652),
    Stop(100, "Petron Makiling", 14.163397, 121.137993),
    Stop(101, "WalterMart Makiling", 14.160453, 121.138110),
    Stop(102, "LPU-Laguna", 14.158927, 121.137829),
    Stop(103, "Makiling", 14.153755, 121.136669),
    Stop(104, "Puting Lupa Junction", 14.149367, 121.135666),
    Stop(105, "FPIP Gate 1", 14.137637, 121.135461),
    Stop(106, "Sta. Anastacia Brgy. Hall", 14.134881, 121.135940),
    Stop(107, "FPIP Gate 2", 14.132762, 121.136514),
    Stop(108, "Sta. Anastacia Elementary School", 14.130421, 121.137209),
    Stop(109, "Sto. Tomas Exit", 14.128337, 121.137770),
    Stop(110, "Ponteverde Sto. Tomas", 14.122558, 121.139552),
    Stop(111, "San Antonio Heights", 14.117710, 121.141428),
    Stop(112, "7-Eleven San Antonio", 14.111290, 121.144381),
    Stop(113, "Santo Tomas Central Terminal", 14.107662, 121.145564),
    Stop(114, "Santo Tomas", 14.105286, 121.143661),
    Stop(115, "San Roque", 14.098970, 121.147304),
    Stop(116, "Tanauan North Central School", 14.089563, 121.148986),
    Stop(117, "Tanauan", 14.084813, 121.149747),
    Stop(118, "FAITH Colleges", 14.078852, 121.150704),
    Stop(119, "WalterMart Tanauan", 14.074399, 121.151402),
    Stop(120, "Darasa", 14.067662, 121.152926),
    Stop(121, "Total Malvar", 14.057752, 121.154325),
    Stop(122, "BSU Malvar", 14.045276, 121.158197),
    Stop(123, "Luta Sur", 14.033844, 121.161280),
    Stop(124, "Uno Fuel Malvar", 14.025444, 121.162047),
    Stop(125, "LIMA", 14.008552, 121.165460),
    Stop(126, "Wilcon Depot Lipa", 13.995808, 121.167983),
    Stop(127, "Inosluban", 13.979340, 121.167855),
    Stop(128, "Jollibee Marawoy", 13.970426, 121.166455),
    Stop(129, "Fiesta Mall Lipa", 13.960481, 121.165667),
    Stop(130, "Lipa City Hall", 13.957309, 121.165675),
    Stop(131, "Lawa Junction", 14.212339, 121.152222),
    Stop(132, "Liana's Calamba", 14.213823, 121.150836),
    Stop(133, "Parian", 14.215127, 121.148285),
    Stop(134, "Calamba Doctors Hospital", 14.217726, 121.142642),
    Stop(135, "Checkpoint Calamba", 14.218526, 121.140632),
    Stop(136, "Caltex San Cristobal", 14.221718, 121.139592),
    Stop(137, "San Cristobal", 14.225722, 121.140062),
    Stop(138, "Jollibee Banlic", 14.228217, 121.138984),
    Stop(139, "WalterMart Cabuyao", 14.232844, 121.135404),
    Stop(140, "San Isidro", 14.237717, 121.133365),
    Stop(141, "CentroMall Cabuyao", 14.242391, 121.131526),
    Stop(142, "Pulo, Cabuyao", 14.246788, 121.129906),
    Stop(143, "Banaybanay, Cabuyao", 14.253710, 121.128574),
    Stop(144, "Nestle Cabuyao", 14.260531, 121.127695),
    Stop(145, "Cabuyao Crossing", 14.268072, 121.126347),
    Stop(146, "Cabuyao City Hall", 14.271028, 121.123210),
    Stop(147, "Wilcon Depot Cabuayo", 14.275191, 121.118691),
    Stop(148, "Dita", 14.282179, 121.111275),
    Stop(149, "Golden City", 14.288814, 121.108620),
    Stop(150, "Balibago (Santa Rosa Crossing)", 14.295351, 121.106113),
    Stop(151, "Macabling", 14.302008, 121.103724),
    Stop(152, "7-Eleven Macabling", 14.305943, 121.102341),
    Stop(153, "Leon Arcillas Blvd", 14.309204, 121.101168),
    Stop(154, "SM City Santa Rosa", 14.313912, 121.099500),
    Stop(155, "New Sinai Hospital", 14.317552, 121.098227),
    Stop(156, "Robinsons Santa Rosa", 14.319369, 121.097552),
    Stop(157, "Caltex Tagapo", 14.321199, 121.096908),
    Stop(158, "Biñan Crossing", 14.327599, 121.091775),
    Stop(159, "Pavilion Mall Biñan", 14.329075, 121.089265),
    Stop(160, "University of Perpetual Help Biñan", 14.331279, 121.085582),
    Stop(161, "Olivarez Plaza Biñan", 14.333127, 121.082378),
    Stop(162, "Areza Biñan", 14.338449, 121.073516),
    Stop(163, "Pacita Complex", 14.347865, 121.065313),
    Stop(164, "Victory Mall Balibago", 14.292270, 121.102645),
    Stop(165, "Balibago Transport Terminal", 14.294045, 121.104538),
    Stop(166, "Balibago Polyclinic", 14.297325, 121.106592),
    Stop(167, "Pooc, Santa Rosa", 14.300638, 121.107429),
    Stop(168, "Don Jose Zavalla Subdivision", 14.303342, 121.109091),
    Stop(169, "Olympia Park Subdivision", 14.306595, 121.110257),
    Stop(170, "Malusak, Santa Rosa", 14.3112177,121.1117894),
    Stop(171, "Santa Rosa City Plaza", 14.313909, 121.112365),
    Stop(172, "Santa Rosa Public Market", 14.313909, 121.112365),
    Stop(173, "Santa Rosa", 14.315897, 121.109848),
    Stop(174, "Puregold Tagapo", 14.317318, 121.106350),
    Stop(175, "7-Eleven Amihan Village", 14.317612, 121.105564),
    Stop(176, "Progressive Village", 14.319270, 121.101639),
    Stop(177, "Balibago Crossing", 14.296820, 121.105571),
]

routes = [
    Route(1, "Batangas City Proper - Balagtas", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 9, 28, 29, 6 , 5, 4, 3, 2, 30, 1]),
    Route(2, "Batangas City Proper - Capitolio", [31, 32, 33, 34, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 35, 24, 25, 37, 27, 9, 28, 34, 33, 32, 36, 31]),
    Route(3, "Batangas City - Bauan", [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 62, 63, 16, 17, 18, 19, 20, 21, 54, 55, 56, 57, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 58, 59, 60, 61, 38]),
    Route(4, "Batangas City - Lipa City", [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 2, 3, 4, 5, 6, 7, 8, 9, 27, 53, 52, 51, 50, 86, 87, 88, 89, 90, 1, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64]),
    Route(5, "Calamba City - Lipa City via Tanauan", [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 64, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91]),
    Route(6, "Calamba City - Pacita Complex", [91, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 91]),
    Route(7, "Santa Rosa Laguna Loop (Clockwise)", [164, 165, 150, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 157, 156, 155, 154, 153, 152, 151, 177, 164]),
    
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
def find_stop_by_name(stops, name):
    for stop in stops:
        if stop.name.lower() == name.lower():
            return stop
    return None

def input_start_and_destination(stops):
    while True:
        start_name = input("Enter the name of the start point: ")
        start_point = find_stop_by_name(stops, start_name)
        if start_point:
            break
        else:
            print("Invalid start point. Please try again.")

    while True:
        destination_name = input("Enter the name of the destination point: ")
        destination_point = find_stop_by_name(stops, destination_name)
        if destination_point:
            break
        else:
            print("Invalid destination point. Please try again.")

    return start_point, destination_point

# Input start and destination points
start_point, destination_point = input_start_and_destination(stops)

# Find and construct the route
trip_route = find_route(stops, routes, start_point, destination_point)
if trip_route:
    print("Starting Point:", start_point.name,"\n")
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
                        print("Stopover:", stop.name, "\n")
                    print("Route {} ({}): {}".format(route_count, j+1, route_obj.route_name))
                    route_count += 1
                    break
else:
    print("No route found")