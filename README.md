# Package_Delivery_App
A solution to a modified Traveling Salesman Problem in which a truck must delivery packages in an optimized manner while still meeting various constraints (package delays, changed addresses, etc.)

I chose to implement a Nearest Neighbor algorithm due to it's simplicity and the scale of the project(A delivery route with 40 regular stops in the same city).

This program was built using Python 3.9.6 in the PyCharm Community Edition 2021.2.3 IDE on a Windows 10 64-bit local machine.


Package description:

•	main – calls the delivery simulation and contains all code relating to the CLI

•	utils – contains all utility functions, time conversions, and Greedy algorithm

•	address_dictionary – contains an address dictionary and related lookup function

•	chaininghashtable – contains a chaining hash table and all related functions to the hash table

•	truck – contains the truck class and method for loading trucks based on package priority

•	package – contains the package class used for instantiating package objects


Screenshots of package delivery status at various times throughout the day with times highlighted in yellow:

![G1_updated](https://user-images.githubusercontent.com/79055002/155603340-a5d241e1-4634-4965-a188-084553f69c00.png)


![G2_updated](https://user-images.githubusercontent.com/79055002/155603373-75d0feef-4705-4002-85bb-84c1773df8bc.png)


![G3_updated](https://user-images.githubusercontent.com/79055002/155603392-99801905-d788-4f72-9079-24c3d35f6b8c.png)

One of the constraints of this project was that the total mileage for all trucks come in under 140 miles. 
Another unique project constraint was that each truck should carry no more than 16 packages: Highlighted in the image below is the load size for each truck along with the total truck mileage.

![H_Screen2](https://user-images.githubusercontent.com/79055002/155603895-a47fb779-ce2e-4a57-9745-1588da2b8acf.png)
