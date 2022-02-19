# Package_Delivery_App
A solution to a modified Traveling Salesman Problem in which a truck must delivery packages in an optimized manner while still meeting various constraints (package delays, changed addresses, etc.)

I chose to implement a Nearest Neighbor Greedy algorithm due to it's simplicity and the scale of the project(A delivery route with 40 regular stops in the same city).

This program was built using Python 3.9.6 in the PyCharm Community Edition 2021.2.3 IDE on a Windows 10 64-bit local machine.

Package description:
•	main – calls the delivery simulation and contains all code relating to the CLI
•	utils – contains all utility functions, time conversions, and Greedy algorithm
•	address_dictionary – contains an address dictionary and related lookup function
•	chaininghashtable – contains a chaining hash table and all related functions to the hash table
•	truck – contains the truck class and method for loading trucks based on package priority
•	package – contains the package class used for instantiating package objects



