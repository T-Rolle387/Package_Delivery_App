
import csv
import math
import datetime
from address_dictionary import lookup_index

from chaininghashtable import all_packages, load_package_data, packageHashTable, packageCount, get_package_data
from truck import truck1, truck2, truck3, priority_load


# Open distance data csv file and read into 2d matrix
# O(n)
def distance_array():
    with open('distance_data.csv', encoding='utf-8-sig') as distance_in:
        distance_data = []
        csvfile = csv.reader(distance_in)
        for row in csvfile:
            distance_data.append(row)
        return distance_data


# Open address data csv file and read into 2d matrix
# O(n)
def address_array():
    with open('address_data.csv', encoding='utf-8-sig') as address_in:
        address_data = []
        csvfile = csv.reader(address_in)
        for row in csvfile:
            address_data.append(row)
        return address_data


# Define 2D distance matrix
distance_matrix = distance_array()
# Define 2D address matrix
address_matrix = address_array()


# This function calculates the current distance from row (i)/column(j) values
# O(1)
def curr_distance(i, j):
    if j > i:
        z = i
        i = j
        j = z
    distance = distance_matrix[i][j]
    if distance == '':
        distance_matrix[j][i]
    return float(distance)


# This function takes the total distance traveled as a parameter, performs calculations based on truck speed, and
# returns a datetime timedelta  object.
# O(1)
def time(distance):
    t = math.ceil(distance / 18 * 60)
    hr = math.floor(t / 60)
    min = t % 60
    string = str(hr) + ':' + str(min) + ':00'
    dt_obj = string_to_datetime(string)
    return dt_obj


# This function converts a string to a datetime timedelta object
# O(1)
def string_to_datetime(string):
    (hrs, min, sec) = string.split(':')
    time_obj = datetime.timedelta(hours=int(hrs), minutes=int(min), seconds=int(sec))
    return time_obj


# Greedy Algorithm - Nearest Neighbor
# This function is designed to accept a truck object that contains two lists,
# one priority-based pre-sorted list, and one empty list. It uses a greedy algorithm that makes an optimal decision
# based on the proximity of the available packages and chooses the closest package to the current one starting from
# the hub. It then appends that package to the empty list, returning a package list sorted by both priority and
# minimum mileage when complete.
# Please see supporting documentation submitted with the assignment for further detail.
# O(n²)
def optimize_truck(self):
    route = self.route  # optimized package list
    unsorted = self.package_list  # priority-sorted package list
    nn = 0  # Initialize the nearest neighbor
    while len(unsorted) > 0:  # Loops through the priority-sorted package list until it is empty
        minimum_mileage = 50.0  # Initialize minimum mileage value
        for p in unsorted:  # Loop through all "unvisited" packages
            i = lookup_index(p.address)  # Lookup up possible next location's index in the address dictionary
            if len(route) == 0: # If route is empty look for nearest neighbor to the hub
                if curr_distance(0, i) < minimum_mileage: # Compare current distance of possible choice to the minimum value
                    minimum_mileage = curr_distance(0, i) # Update minimum value if the current distance compared is less
                    nn = p # Declare the nearest neighbor
            else:
                current_address = route[-1].address  # Reference address
                current_index = lookup_index(current_address)   # Reference index
                if curr_distance(current_index, i) < minimum_mileage: # Calculate the distance from reference index to possible choice and compare to the minimum value
                    minimum_mileage = curr_distance(current_index, i) # Update minimum value if the current distance compared is less
                    nn = p # Declare the nearest neighbor
        route.append(nn) # Append the nearest neighbor to the sorted list
        packageHashTable.search(str(nn.id)).status = 'En route' # Update the package status in the hash table
        unsorted.remove(nn) # Remove the nearest neighbor from the unsorted list

    return route # Return list sorted by the algorithm


# This function is designed to be called after the truck packages are sorted into an optimized list for
# delivery. This method calculates the total mileage traveled starting from and heading back to the hub after the packages
# are delivered. It keeps track of the time and timestamps each package in the hash table when the package is delivered.
# O(n)
def truck_deliver_packages(self):
    total_mileage = 0.0  # Initialize total mileage variable
    route = self.route
    prev_index = 0
    start_time = string_to_datetime(self.start_time)
    for p in route:
        p_id = p.get_id()
        p_address = p.get_address()
        current_index = lookup_index(p_address)
        total_mileage += curr_distance(prev_index, current_index)
        prev_index = current_index
        t = time(total_mileage)
        arrival_time = start_time + t
        deliver_package(p_id, arrival_time, p)
    total_mileage += curr_distance(prev_index, 0)
    self.end_time = str(t + string_to_datetime(self.start_time))
    return total_mileage, self.end_time


# This function updates a packages status to delivered and timestamps it.
# O(1)
def deliver_package(id, time, p):
    p.status = 'Delivered'
    packageHashTable.search(id).status = 'Delivered'
    packageHashTable.search(id).delivery_time = time



# This function runs a package delivery simulation
# O(n³)
def delivery_sim():
    # Declare truck start times
    truck1.start_time = '08:00:00'
    truck2.start_time = '09:06:00'
    truck3.start_time = '10:00:00'
    # Run package delivery simulation
    all_packages.pop(0)  # Remove the package header
    priority_load(all_packages, truck1, truck2, truck3)  # Load all trucks based on priority
    print('Packages on truck 1: {}'.format(len(optimize_truck(truck1))))
    print('Packages on truck 2: {}'.format(len(optimize_truck(truck2))))
    print('Packages on truck 3: {}'.format(len(optimize_truck(truck3))))
    print('Assigned truck number is viewable with package details below.')
    t1_mileage, t1_end = truck_deliver_packages(truck1)  # Deliver the packages on truck 1
    t2_mileage, t2_end = truck_deliver_packages(truck2)  # Deliver the packages on truck 2
    t3_mileage, t3_end = truck_deliver_packages(truck3)  # Deliver the packages on truck 3
    all_truck_mileage = t1_mileage + t2_mileage + t3_mileage

    print('All packages on the first truck are delivered by {} with a total of {} miles traveled.'.format(t1_end, round(
        t1_mileage, 2)))
    print('All packages on the second truck are delivered by {} with a total of {} miles traveled.'.format(t2_end,
                                                                                                           round(
                                                                                                               t2_mileage,
                                                                                                               2)))
    print('All packages on the third truck do not leave the hub until {} and are delivered by {} with a total of {} '
          'miles traveled.'.format(truck3.start_time, t3_end, round(t3_mileage, 2)))
    print('The total mileage of all three trucks is {} upon completion of the delivery of all packages.'.format(
        all_truck_mileage))
