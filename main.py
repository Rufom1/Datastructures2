# Author: Michael Rufo 

from package import Package
from hashtable import HashTable

def lookup_package(package_id, package_table):
    """
    Function to look up a package by its ID in the package list.
    :param package_id: The ID of the package to look up.
    :param package_list: The table of packages where each package is stored with its ID as the key.
    :return: The package if found, otherwise None.
    """

    if package_id in package_table:
        return package_table[package_id].lookupPackage()
    else:
        return None


def main():
    '''
    Main function to deliver packages using a self-adjusting algorithm and a hash table.

    Initialize a hash table to store package data
    Initialize a hash table to store delivery data
    Initialize a set of trucks to deliver packages 
        contaning truck objects with attributes such as truck ID, and packages assigned, distance traveled, package weight
            and methods to update packages, deliver packages, calculate distance, and update status

    read package and delivery data from file 
    for each package in the package data:
        assign a unique ID to the package
        assign a delivery address, deadline, city, zip code, weight, and delivery status
        add the package to the package table

        If the package has a duplicate address, set the duplicateAddress attribute to True
        If the package has a duplicate address, incriment the duplicateAddressPointer 
            and add it to the list of packages with the same address 
        calculate the distance from the hub to the package address      
        assign the nearest neighbor ID and distance to the package

    Intialize a queue to manage loading packaged onto trucks
        containing package objects

    Sort packages into queue based on distance from hub and delivery deadline

    Sort packages into trucks based on the nearest neighbor algorithm
        for each truck:
            while there are packages in the queue:
                if truck is empty:
                    load the first package from the queue onto the truck
                else:
                    check if the truck can carry the package based on its weight and capacity
                    if the truck can carry the package:
                        check if duplicate address exists
                        if duplicate address exists:
                            skip to duplicate address pointer
                            load duplicates onto truck until truck is full or no more duplicates
                            decrement the package iterator back to skipped package
                        else
                            load the package onto the truck
                    else:
                        dequeue the next truck and repeat the process
    '''

    # Example package data structure
    package_table = {
        1: Package(id=1, address="123 Main St", deadline="10:30 AM", city="Salt Lake City", zip=84101, weight=5, deliveryStatus="at the hub"),
        2: Package(id=2, address="456 Elm St", deadline="12:00 PM", city="Salt Lake City", zip=84102, weight=10, deliveryStatus="en route"),
        # Add more packages as needed
    }

    # Example usage of lookup_package function
    package_id = 1
    package_info = lookup_package(package_id, package_table)
    
    if package_info:
        print(f"Package {package_id} found: {package_info}")
    else:
        print(f"Package {package_id} not found.")