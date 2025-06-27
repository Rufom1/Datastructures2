
MAX_SPEED = 18 #mph

class Truck:
    def __init__(self, id, capacity=16, driver=None, package_list={}, address_dict={}):
        self.id = id
        self.capacity = capacity
        self.load = 0
        self.max_speed = MAX_SPEED
        self.driver = driver
        self.package_list = package_list
        self.address_list = address_list

    def load_cargo(self, weight):
        if self.load < self.capacity:
            self.load += 1
            return True
        else:
            return False

    def unload_cargo(self, address):
        if self.load >= 0:
            for packageId in self.address_list[address]:
                if packageId in self.package_list:
                    del self.package_list[packageId]
                    self.load -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"Truck {self.id} with current load {self.load}"