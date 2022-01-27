

# This is a dictionary used to map the address(key) to the numeric value used in obtaining distance_data.
# O(1)
address_dict = {
    '4001 South 700 East': 0,
    '1060 Dalton Ave S': 1,
    '1330 2100 S': 2,
    '1488 4800 S': 3,
    '177 W Price Ave': 4,
    '195 W Oakland Ave': 5,
    '2010 W 500 S': 6,
    '2300 Parkway Blvd': 7,
    '233 Canyon Rd': 8,
    '2530 S 500 E': 9,
    '2600 Taylorsville Blvd': 10,
    '2835 Main St': 11,
    '300 State St': 12,
    '3060 Lester St': 13,
    '3148 S 1100 W': 14,
    '3365 S 900 W': 15,
    '3575 W Valley Central Station bus Loop': 16,
    '3595 Main St': 17,
    '380 W 2880 S': 18,
    '410 S State St': 19,
    '4300 S 1300 E': 20,
    '4580 S 2300 E': 21,
    '5025 State St': 22,
    '5100 South 2700 West': 23,
    '5383 South 900 East #104': 24,
    '600 E 900 South': 25,
    '6351 South 900 East': 26

}


# This function looks up an addresses index given the string address as the parameter passed.
# This is useful to link the package data to the distance data using the string address as the common key.
# O(1)
def lookup_index(address):
    index = address_dict[address]
    return index
