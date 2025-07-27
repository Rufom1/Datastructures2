
from enum import Enum


class DeliveryStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"

class Package:
    def __init__(self,id=-1, address="", deadline=None, city="", zip=0, weight=0, deliveryStatus=DeliveryStatus.NOT_STARTED.value, notes=None, addressIdx=None):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.deliveryStatus = deliveryStatus
        self.truckID = -1
        self.deliveryTime = None
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
    
    def deliverPackage(self, deliveryTime):
        self.deliveryTime = deliveryTime
        self.deliveryStatus = DeliveryStatus.DELIVERED.value



if __name__ == "__main__":
    pass