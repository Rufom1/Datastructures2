

class Package:
    def __init__(self,id=-1, address="", deadline=None, city="", zip=0, weight=0, deliveryStatus="", notes=None, addressIdx=None):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.deliveryStatus = deliveryStatus
        self.truckID = -1
        self.HubDistance = -1
        self.nearestNeighborID = -1
        self.nearestNeighborDistance = -1
        self.duplicateAddress = False
        self.duplicateAddressPointer = 0
        self.notes = notes
        self.addressIdx = addressIdx

    def __str__(self):
        return f"{self.id}"
    
    def lookupPackage(self):
        return {
            "address": self.address,
            "deadline": self.deadline,
            "city": self.city,
            "zip": self.zip,
            "weight": self.weight,
            "deliveryStatus": self.deliveryStatus,
            "truckID": self.truckID,
        }
    
    def loadTruckID(self, truckID):
        self.truckID = truckID

    def getAddresIdx(self):
        return self.addressIdx



if __name__ == "__main__":
    pass