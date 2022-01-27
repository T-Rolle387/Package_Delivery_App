
import csv
from package import Package


# The ChainingHashTable class implements a hash table using chaining to store and access package data efficiently.
class ChainingHashTable:
    # Constructor with initial capacity set to 10
    # All buckets are assigned with an empty list below.
    def __init__(self, initial_capacity=10):
        self.hash_table = [] # Initialize the hash table with empty bucket list entries.
        for i in range(initial_capacity):
            self.hash_table.append([])

    # This function inserts/updates items in(to) the the hash table.
    def insert_package(self, key, item):  # Handles both insert and update functions
        # Retrieves the bucket list where this item will go.
        bucket = hash(key) % len(self.hash_table)
        b_list = self.hash_table[bucket]

        # Updates the key if already present in the bucket
        for kv_pair in b_list:
            if kv_pair[0] == key:
                kv_pair[1] = item
                return True

        # If key not present, insert the item at the end of the bucket list.
        key_value = [key, item]
        b_list.append(key_value)
        return True

    # This function is used to search the hash table for a certain item.
    # O(1)
    def search(self, key):
        # get the bucket list where this key(package_id) would be.
        bucket = hash(key) % len(self.hash_table)
        b_list = self.hash_table[bucket]

        # Search for the key in the bucket list
        for kv_pair in b_list:
            # print (key_value)
            if kv_pair[0] == key:
                return kv_pair[1]  # value
        return None

    # This function removes an item from the hash table
    def remove_package(self, key):
        # Get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.hash_table)
        b_list = self.hash_table[bucket]

        # Remove the item from the bucket list if it is present.
        for kv_pair in b_list:
            # print (key_value)
            if kv_pair[0] == key:
                b_list.remove([kv_pair[0], kv_pair[1]])


# This function loads package information from a csv file and adds it to the hash table as package objects
# O(n)
def load_package_data(filename):
    counter = 0
    with open(filename) as packageInfo:
        packageData = csv.reader(packageInfo, delimiter=',')
        for package in packageData:
            id = package[0]  # Package ID number
            address = package[1]  # Delivery address
            city = package[2]  # Delivery city
            state = package[3]  # Delivery state
            zip = package[4]  # Delivery zip code
            deadline = package[5]  # Delivery deadline
            weight = package[6]  # Package weight
            notes = package[7]  # Special notes
            delivery_time = None  # Delivery time
            status = 'At hub'  # Delivery status
            priority = None  # Package priority used for loading packages
            truck_number = None # Package truck number

            # package object
            package = Package(id, address, city, state, zip, deadline, weight, notes, delivery_time, status, priority, truck_number)
            counter += 1
            # print(package)  # This prints package objects created with csv file data... May delete later

            # insert package into hash table
            packageHashTable.insert_package(id, package)

            # insert into list
            all_packages.append(package)

    return counter


# hash table instance
packageHashTable = ChainingHashTable()

# all packages list
all_packages = []

# load packages into hash table
packageCount = load_package_data('package_data.csv')




# Retrieve data from Hash Table
# O(n)
def get_package_data():
    for i in range(1, packageCount):
        print("Key: {} and Package: {}".format(i, packageHashTable.search(str(i))))
