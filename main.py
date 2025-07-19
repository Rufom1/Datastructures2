# Author: Michael Rufo 

from package import Package
from hashtable import HashTable
import csv
from pathlib import Path
from enum import Enum
import os

class DeliveryStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"

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
    

def read_csv(file_path):
    """
    Function to read distance matrix from csv and return a 2D array.
    :param file_path: The path to the CSV file.
    :return: A list of lists containing the data from the CSV file.
    """
    with open(file_path, newline='') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        return [row for row in csvReader]
    

def index_addresses(distance_array):
    """
    Function to index addresses in a list and return a dictionary with address as key and index as value.
    :param addresses: A list of addresses.
    :return: A dictionary with addresses as keys and their indices as values.
    """
    address_index = HashTable(size=len(distance_array))
    for idx, address in enumerate(distance_array):
        address_index.insert(address[0], idx + 1)
    return address_index

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

    packageArray = read_csv(f'{os.getcwd()}/WGUPS Package File.csv')
    distanceArray = read_csv(f'{os.getcwd()}/WGUPS Distance Table.csv')

    addressIndex = index_addresses(distanceArray)

    #wgu_packages_file = load_workbook(f'{parent_dir}/WGUPS Package File.xlsx')
    #package_distances_file = load_workbook(f'{parent_dir}/WGUPS Distance Table.xlsx')

    #delivery_array = [row for row in wgu_packages_file.active.iter_rows(min_row=8, max_row=48, min_col=1, max_col=8, values_only=True)]
    #distance_array = [row for row in package_distances_file.active.iter_rows(min_row=8, max_row=35, min_col=1, max_col=29, values_only=True)]

    packageTable = create_packages(packageArray, addressIndex)

    firstTruck_packages = [1, 15, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    firstTruck = load_first_truck(packageTable, firstTruck_packages)

    secondTruck_packages = [2, 3, 4, 5, 10, 18, 36, 38]
    thirdTruck_packages = [6, 7, 8, 25, 28, 32, 9]

    secondTruck, thirdTruck = sort_remaining_packages(packageTable, secondTruck_packages, thirdTruck_packages)

    for truck in [firstTruck, secondTruck, thirdTruck]:
        # Deliver packages for each truck
        deliver_packages(truck, distanceArray)



def deliver_packages(package, distanceArray):
    # Implementation of the delivery logic goes here
    
    currentNode = 0
    totalDistance = 0

        # Simulate the delivery process for each package
        # For each package on truck: (start at index 0)
            # Set delivery status to "In Transit"
            # Calculate distance from hub to package address * 18 for time delta 
            # Update delivery status to "Delivered"
            # Update the package in the hash table with the new delivery status and time
            # Find nearest neighbor for the next package
        # Continue until all packages are delivered
    package.deliveryStatus = DeliveryStatus.IN_TRANSIT.value
    nextNode = getNearestNeighbor(package.getAddresIdx(), distance_array=distanceArray)
    distance, time = travel_to_next_package(currentNode, nextNode[0], distanceArray)
    totalDistance += distance
    package.deliveryStatus = DeliveryStatus.DELIVERED.value


def travel_to_next_package(currentNode, nextNode, distanceArray):
    '''
    Function to calculate the distance and time to travel to the next package.
    :param currentNode: The current node (package address index).
    :param nextNode: The next node (nearest neighbor package address index).
    :param distanceArray: The array containing distances between nodes.
    :return: The distance and time to travel to the next package.
    '''
    distance = float(distanceArray[currentNode][nextNode])
    time = distance / 18  # Assuming speed is 18 mph
    return distance, time
    
def create_packages(package_array, address_Index):
    '''
    Function to create package objects from the package array and store them in a hash table.
    :param package_array: The array of packages to be processed.
    :return: A hash table containing package objects indexed by their IDs.
    '''
    package_table = HashTable(size=len(package_array))
    
    for i in range(len(package_array)):
        package = Package(
            id=int(package_array[i][0]),
            address=package_array[i][1],
            deadline=package_array[i][5],
            city=package_array[i][2],
            zip=int(package_array[i][3]),
            weight=float(package_array[i][6]),
            deliveryStatus=DeliveryStatus.NOT_STARTED.value,
            notes=package_array[i][7] if len(package_array[i][7]) > 0 else None,
            addressIdx=address_Index.get(package_array[i][1])  # Get index from addressIndex
        )
        package_table.insert(package.id, package)
    
    return package_table

def load_first_truck(package_map, firstTruck):
    first_truck = []
    for idx in firstTruck:
        package = package_map.get(idx)
        package.loadTruckID(1)  # Load truck ID for the package
        first_truck.append(package_map.get(idx))

    return first_truck

def sort_remaining_packages(package_map, secondTruck, thirdTruck):
    '''
    Function to sort remaining packages into trucks based on the nearest neighbor algorithm.
    :param package_Array: The array of packages to be sorted.
    :param secondTruck: The second truck object to load packages into.
    :param thirdTruck: The third truck object to load packages into.
    :return: None
    '''
    second_truck, third_truck = []

    for package in package_map:
        if package.notes is None and package.deadline is None:
            if len(secondTruck.package_dict) < len(thirdTruck):
                package.loadTruckID(2)
                secondTruck.append(package) 
            else:
                package.loadTruckID(3)
                thirdTruck.append(package)

    return second_truck, third_truck

def getNearestNeighbor(currentNode, distance_array):
    '''
    Function to find the nearest neighbor for a given node based on the distance array.
    :param currentNode: The current node for which to find the nearest neighbor.
    :param distance_array: The array containing distances between nodes.
    :return: The ID of the nearest neighbor and its distance.
    '''
    nearest_neighbor_id = None
    nearest_distance = float('inf')
    pivot = 0
    x = currentNode

    for i in range(1, len(distance_array[currentNode])-1):
        if distance_array[x][i] != '0.0' and pivot == 0:
            distance = float(distance_array[x][i])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_neighbor_id = i - 1
        elif distance_array[x][i] == '0.0' and pivot == 0:
            pivot = i
            x += 1
            distance = float(distance_array[x][pivot])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_neighbor_id = i - 1
        elif distance_array[x][i] != '0.0' and pivot != 0:
            x += 1
            distance = float(distance_array[x][pivot])
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_neighbor_id = i


    return nearest_neighbor_id, nearest_distance

if __name__ == "__main__":
    main()
    # Example usage of lookup_package
    # package_table = HashTable()
    # package_table.insert(1, Package(1, "123 Main St", "10:30 AM", "Salt Lake City", "84101", 5, "Delivered"))
    # package = lookup_package(1, package_table)
    # if package:
    #     print(f"Package found: {package}")
    # else:
    #     print("Package not found.")