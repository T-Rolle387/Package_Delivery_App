
import datetime
import math

from address_dictionary import lookup_index
from chaininghashtable import packageCount, packageHashTable, all_packages


# The Truck Class is used to generate truck objects that contain a list of packages, an optimized route list,
# and pertinent times.
class Truck:
    def __init__(self):
        # Constructor: Initializes truck package list, route, relevant delivery times, and mileage.
        self.package_list = []  # Unsorted package list
        self.route = []  # Optimized packing list for delivery
        self.start_time = None
        self.end_time = None
        self.truck_number = None

    # get package list
    def get_package_list(self):
        return self.package_list

    # get optimized route list
    def get_route(self):
        return self.route

    # get start time
    def get_start_time(self):
        return self.start_time

    # get end time
    def get_end_time(self):
        return self.end_time

    # get truck number
    def get_truck_number(self):
        return self.truck_number


# Instantiate truck objects
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
# Define truck number
truck1.truck_number = '1'
truck2.truck_number = '2'
truck3.truck_number = '3'


# This function accesses all packages in the hash table and assigns them a priority level based on special notes given.
# The priority levels are defined below:
""" priority1 - package with a deadline
    priority2 - package can only be on truck2
    priority3 - package can only be grouped with certain packages
    priority4 - package delayed but has a deadline"""
# O(n)
def priority():
    for i in range(1, packageCount):
        package = packageHashTable.search(str(i))
        notes = package.notes
        deadline = package.deadline
        if 'EOD' not in deadline:
            if 'Delayed' in notes:
                package.priority = 'priority4'
            else:
                package.priority = 'priority1'
        elif 'Can only be' in notes:
            package.priority = 'priority2'
        elif 'Must be' in notes:
            package.priority = 'priority3'
        elif 'Delayed' in notes:
            package.priority = 'priority4'




# This function loops through all packages, accesses their priority level (by calling the priority() method) and
#  assigns them to a truck based on based on that priority level.
# O(n²)
def priority_load(arr, t1, t2, t3):
    package_list1 = t1.package_list
    package_list2 = t2.package_list
    package_list3 = t3.package_list
    truck_num1 = t1.truck_number
    truck_num2 = t2.truck_number
    truck_num3 = t3.truck_number
    priority()  # Assigns a priority level to all packages
    for p in arr:
        while len(arr) > 24:
            if p.priority == 'priority1' or p.priority == 'priority3':
                if p not in package_list1:
                    package_list1.append(p)
                    p.truck_number = truck_num1
                    arr.remove(p)
                    p = arr[0]
            elif p.priority == 'priority2' or p.priority == 'priority4':
                if p not in package_list2:
                    package_list2.append(p)
                    p.truck_number = truck_num2
                    arr.remove(p)
                    p = arr[0]
            elif p.priority is None:
                if p.priority not in package_list3 and len(package_list3) < 16:
                    package_list3.append(p)
                    p.truck_number = truck_num3
                    arr.remove(p)
                    p = arr[0]
                else:
                    package_list1.append(p)
                    p.truck_number = truck_num1
                    arr.remove(p)
                    p = arr[0]
        while len(arr) > 8:
            if p.priority == 'priority1' or p.priority == 'priority3':
                if p not in package_list1:
                    package_list1.append(p)
                    p.truck_number = truck_num1
                    arr.remove(p)
                    p = arr[0]
            elif p.priority == 'priority2' or p.priority == 'priority4':
                if p not in package_list2:
                    package_list2.append(p)
                    p.truck_number = truck_num2
                    arr.remove(p)
                    p = arr[0]
            elif p.priority is None:
                if p not in package_list3 and len(package_list3) < 16:
                    package_list3.append(p)
                    p.truck_number = truck_num3
                    arr.remove(p)
                    p = arr[0]
                else:
                    package_list1.append(p)
                    p.truck_number = truck_num1
                    arr.remove(p)
                    p = arr[0]
        while len(arr) > 1:
            if p.priority == 'priority1' or p.priority == 'priority3':
                if p not in package_list1:
                    package_list1.append(p)
                    p.truck_number = truck_num1
                    arr.remove(p)
                    p = arr[0]
            elif p.priority == 'priority2' or p.priority == 'priority4':
                if p not in package_list2:
                    package_list2.append(p)
                    p.truck_number = truck_num2
                    arr.remove(p)
                    p = arr[0]
            elif p.priority is None:
                if p not in package_list3 and len(package_list3) < 16:
                    package_list3.append(p)
                    p.truck_number = truck_num3
                    arr.remove(p)
                    p = arr[0]
                else:
                    package_list2.append(p)
                    p.truck_number = truck_num2
                    arr.remove(p)
                    p = arr[0]
        while len(arr) == 1:
            package_list1.append(p)
            p.truck_number = truck_num1
            arr.remove(p)

        return package_list1, package_list2, package_list3

