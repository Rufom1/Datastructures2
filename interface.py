
class DeliveryUI:
    def __init__(self, delivery_table):
        self.delivery_table = delivery_table

    def display_deliveries(self):
        for address, packages in self.delivery_table.items():
            print(f"Address: {address}")
            for package in packages:
                print(f"  Package ID: {package.package_id}, Deadline: {package.deadline}, City: {package.city}, Zip Code: {package.zip_code}, Weight: {package.weight}, Status: {package.delivery_status}")

    def lookup_package(self, package_id):
        for address, packages in self.delivery_table.items():
            for package in packages:
                if package.package_id == package_id:
                    return package
        return None
    
    def lookup_deliveryTime(self, package_id):
        package = self.lookup_package(package_id)
        if package:
            return package.delivery_time
        return None
    
    def update_delivery_status(self, package_id, status):
        package = self.lookup_package(package_id)
        if package:
            package.delivery_status = status
            return True
        return False
    
    def display_totalMiles(self):
        total_miles = 0
        for address, packages in self.delivery_table.items():
            for package in packages:
                total_miles += package.distance_from_hub
        print(f"Total miles driven: {total_miles}")

    