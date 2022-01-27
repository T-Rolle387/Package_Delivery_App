
# The Package Class is used to generate package objects.
# Package objects store pertinent package data/attributes
from address_dictionary import lookup_index


class Package:
    # Package constructor
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, delivery_time, status, priority, truck_number):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_time = delivery_time
        self.status = status
        self.priority = priority
        self.truck_number = truck_number

    def __str__(self):  # Overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.address, self.city, self.state, self.zip, self.deadline
            , self.weight, self.notes, self.delivery_time, self.status, self.priority, self.truck_number)

    # get package id
    def get_id(self):
        return self.id

    # get package address
    def get_address(self):
        return self.address

    # get package city
    def get_city(self):
        return self.city

    # get package state
    def get_state(self):
        return self.state

    # get package zip
    def get_zip(self):
        return self.zip

    # get package deadline
    def get_deadline(self):
        return self.deadline

    # get package notes
    def get_notes(self):
        return self.notes

    # get package delivery time
    def get_delivery_time(self):
        return self.delivery_time

    # get package status
    def get_status(self):
        return self.status

    # get package priority
    def get_priority(self):
        return self.priority

    # get truck number
    def get_truck_number(self):
        return self.truck_number
