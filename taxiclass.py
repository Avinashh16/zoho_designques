class Taxi:

    id = 1
    def __init__(self) -> None:

        self.id = Taxi.id
        self.currentLocation = 'B'
        self.availableFrom = 0
        self.earnings = 0
        self.trips  = []

        Taxi.id +=1

    def getId(self):
        return self.id
    
    def getCurrentLocation(self):
        return self.currentLocation
    
    def updateCurrentLocation(self, currentLocation):
        self.currentLocation = currentLocation
    
    def getAvailableFrom(self):
        return self.availableFrom
    
    def updateAvailableFrom(self,availableFrom):
        self.availableFrom = availableFrom

    def getEarnings(self):
        return self.earnings
    
    def updateEarnings(self,cost):
        self.earnings += cost

    def getTrips(self):
        return self.trips
    
    def addTrip(self,trip):
        self.trips.append(trip)
    
    def getArrivalTime(self,pickupPoint):

        return abs(ord(self.currentLocation) - ord(pickupPoint))
    

    def getDetails(self):
        print("Taxi ID = " ,self.getId())
        print("Current Location = ",self.getCurrentLocation())
        print("Available From = ",self.getAvailableFrom())
        print("Total Earnings",self.getEarnings())
        print("Trips")
        for trip in self.trips:
            trip.getDetails()



class Trip:

    id = 1

    def __init__(self,pickupPoint,dropPoint,taxiId,pickupTime,dropTime) -> None:
        self.id = Trip.id
        self.pickupPoint = pickupPoint
        self.dropPoint = dropPoint
        self.taxiId = taxiId
        self.pickupTime = pickupTime
        self.dropTime = dropTime
        Trip.id += 1


    def getDetails(self):
        print(f" {self.id} , {self.pickupPoint} , {self.dropPoint} ")