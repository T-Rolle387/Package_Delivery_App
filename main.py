

import datetime
from chaininghashtable import all_packages, packageCount, packageHashTable
from truck import priority_load, truck3, truck1, truck2
from utils import string_to_datetime, optimize_truck, truck_deliver_packages, delivery_sim

# Declare truck start times
truck1.start_time = '08:00:00'
truck2.start_time = '09:06:00'
truck3.start_time = '10:00:00'  # Truck 3 must leave after truck 1 returns because there are only two drivers

# Turn start times into datetime timedelta objects for later comparison
truck1_start = string_to_datetime(truck1.start_time)
truck2_start = string_to_datetime(truck2.start_time)
truck3_start = string_to_datetime(truck3.start_time)

# Run package delivery simulation
delivery_sim()
print("The interface below is designed to interact with the user in the user's current time. ")
print("To view the status of all packages at any given time please select option 3, type in the time you would like to view, and press enter.")

now = datetime.datetime.now()  # Get current time as datetime object
current_t = now.strftime('%H:%M:%S')  # Convert to string
current_time = string_to_datetime(current_t)  # Convert string to timedelta object for comparison


# This method returns all package information in current time
# O(n)
def choice_one():
    for i in range(1, packageCount):  # Get package information from the hash table
        p = packageHashTable.search(str(i))  # package object
        address_change = string_to_datetime('10:20:00')  # Time of address change
        if '9' in p.id:  # Address correction
            if current_time < address_change:  # Compare current time to time of address change and change if needed
                p.address = '300 State St'
        if p.delivery_time is not None:  # Get delivery time
            if p.delivery_time <= current_time:
                print('ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: {} Truck number: {}'.format(p.id,
                                                                                                              p.address,
                                                                                                              p.city,
                                                                                                              p.zip,
                                                                                                              p.deadline,
                                                                                                              p.weight,
                                                                                                              p.status,
                                                                                                              p.delivery_time,
                                                                                                              p.truck_number))
            elif p.delivery_time > current_time:  # Compare delivery time to current time and update status accordingly
                if p in truck2.route and current_time < truck2_start:
                    p.status = 'At hub'
                if p in truck3.route and current_time < truck3_start:
                    p.status = 'At hub'
                else:
                    p.status = 'En route'
                print('ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: Scheduled for '
                      'delivery by end of day. Truck number: {}'.format(p.id, p.address, p.city, p.zip, p.deadline, p.weight,
                                                       p.status, p.truck_number))


# This method returns package information for a single package
# O(1)
def choice_two():
    try:
        entered_id = input("""Please enter a package number in front of the arrows below to retrieve package information.\n
                               >>>>>""")
        p = packageHashTable.search(entered_id)
        address_change = string_to_datetime('10:20:00')
        if '9' in entered_id:
            if current_time < address_change:
                p.address = '300 State St'
        if p.delivery_time is not None:
            if p.delivery_time <= current_time:
                print(
                'ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: {} Truck number: {}'.format(p.id, p.address,
                                                                                                        p.city, p.zip,
                                                                                                        p.deadline,
                                                                                                        p.weight,
                                                                                                        p.status,
                                                                                                        p.delivery_time,
                                                                                                        p.truck_number))
            elif p.delivery_time > current_time:
                if p in truck2.route and current_time < truck2_start:
                    p.status = 'At hub'
                if p in truck3.route and current_time < truck3_start:
                    p.status = 'At hub'
                else:
                    p.status = 'En route'
                print('ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: Scheduled for '
                  'delivery by end of day. Truck number {}'.format(p.id, p.address, p.city, p.zip, p.deadline, p.weight, p.status, p.truck_number))
    except ValueError:
        print('Invalid Entry. Please choose one of the options above by typing in the option number in front of the arrows and press enter.')


# This method returns package information for all packages at a specific time
# O(n)
def choice_three():
    try:
        time_entry = input("""Please enter your time selection in front of the arrows below in the following format and press enter:
                                    HH:MM:SS as Hours:Minutes:Seconds in military time
                                    Ex) 10:00 AM would be 10:00:00 and 2:00 PM would be 14:00:00
                                    Please enter any time during normal business hours from 08:00:00 onwards.\n 
                                    >>>>> """)
        time_entered = string_to_datetime(time_entry)  # Converts time entered to datetime object

        for i in range(1, packageCount):
            p = packageHashTable.search(str(i))  # package object
            address_change = string_to_datetime('10:20:00')
            if '9' in p.id:
                if time_entered < address_change:
                    p.address = '300 State St'
                elif time_entered >= address_change:
                    p.address = '410 S State St'
            if p.delivery_time is not None:
                if p.delivery_time <= time_entered:
                    print('ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: {} Truck number: {}'.format(p.id,
                                                                                                              p.address,
                                                                                                              p.city,
                                                                                                              p.zip,
                                                                                                              p.deadline,
                                                                                                              p.weight,
                                                                                                              p.status,
                                                                                                              p.delivery_time,
                                                                                                              p.truck_number))
                elif p.delivery_time > time_entered:
                    if p in truck2.route and time_entered < truck2_start:
                        p.status = 'At hub'
                    if p in truck3.route and time_entered < truck3_start:
                        p.status = 'At hub'
                    else:
                        p.status = 'En route'
                    print('ID: {} Address: {} {} {} Deadline: {} Weight: {} Status: {} Time delivered: Pending Truck Number: {}'.format(p.id,
                                                                                                                   p.address,
                                                                                                                   p.city,
                                                                                                                   p.zip,
                                                                                                                   p.deadline,
                                                                                                                   p.weight,
                                                                                                                   p.status,
                                                                                                                   p.truck_number))
    except ValueError:
        print('Invalid Entry. Please choose one of the options above by typing in the option number in front of the arrows below and press enter.')


# This method contains the main menu screen prompt
# O(1)
def prompt_screen():
    try:
        u_entry = input("""Please select one of the following options by typing the option number in front of the arrows below and press enter:
                           1. Get all package information
                           2. Get information on a specific package
                           3. Select new time to check package delivery status for all packages
                           4. Exit program\n \n>>>>> """)
    except ValueError:
        print('Invalid Entry. Please choose one of the options above by typing in the option number and press enter.')
    return u_entry


# The main class contains the code for the user interface and results reporting defined by the rubric requirements.
class Main:
    print('---------------------------------------- Welcome to WGUPS ----------------------------------------\n')
    user_entry = prompt_screen()
    while '4' not in user_entry:
        if user_entry == '1':
            choice_one()
            print('\n\n')
            user_return = input("""Would you like to return to the main menu?
                Please select one of the following by typing in the selection number in front of the arrows below and press enter:
                1. Return to Main Menu
                2. Exit program\n
                >>>>>""")
            if '1' in user_return:
                user_entry = prompt_screen()
            if '2' in user_return:
                user_entry = '4'
            continue

        if user_entry == '2':
            choice_two()
            print('\n\n')
            try:
                user_return = input("""Would you like to return to the main menu?
                            Please select one of the following by typing in the option number in front of the arrows below and press enter:
                            1. Return to Main Menu
                            2. Look up another package
                            3. Exit program\n
                            >>>>>""")
                while '2' in user_return:
                    choice_two()
                    user_return = input("""Would you like to return to the main menu?
                                            Please select one of the following by typing in the option number in front of the arrows below and press enter:
                                            1. Return to Main Menu
                                            2. Look up another package
                                            3. Exit program\n
                                            >>>>>""")
                if '1' in user_return:
                    user_entry = prompt_screen()
                    continue
                if '3' in user_return:
                    user_entry = '4'
            except ValueError:
                print('Invalid Entry. Please choose one of the options above by typing in the option number and press enter.')

        if user_entry == '3':
            choice_three()
            print('\n\n')
            try:
                user_entry = prompt_screen()
            except ValueError:
                print('Invalid Entry. Please choose one of the options above by typing in the option number and press enter.')
            continue

    if user_entry == '4':  # Exit program
        print('Thank you for using WGUPS!')
        exit()
