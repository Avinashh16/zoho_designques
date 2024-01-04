from zoho.zoho_designques.taxiclass import Taxi,Trip

def getAvailableTaxies(pickupTime,pickupPoint):

    availableTaxies = []

    for taxi in taxies:
        if (taxi.getAvailableFrom() + taxi.getArrivalTime(pickupPoint)) <= pickupTime:
            availableTaxies.append(taxi)
    
    return availableTaxies

def getNearestTaxi(availableTaxies,pickupPoint):
    nearest = None
    for taxi in availableTaxies:
        if nearest == None:
            nearest = taxi
            nearestDistance = taxi.getArrivalTime(pickupPoint)
        else:
            if taxi.getArrivalTime(pickupPoint) < nearestDistance:
                nearest = taxi
                nearestDistance = taxi.getArrivalTime(pickupPoint)
            if taxi.getArrivalTime(pickupPoint) == nearestDistance:
                if taxi.getEarnings() < nearest.getEarnings():
                    nearest = taxi
                    nearestDistance = taxi.getArrivalTime(pickupPoint)
            
    return nearest

def getTravelTime(pickupPoint,dropPoint):
    return abs(ord(pickupPoint)-ord(dropPoint))

def getTravelcost(traveltime):
    cost = (((traveltime * 15 ) - 5 ) * 10 ) + 100
    return cost

def bookTaxi(pickupPoint,dropPoint,pickupTime):

    availableTaxies = getAvailableTaxies(pickupTime,pickupPoint)
    if len(availableTaxies) == 0:
        print("No Available Taxies")
        return
    nearestTaxi = getNearestTaxi(availableTaxies,pickupPoint)
    print("Booking...")

    

    traveltime = getTravelTime(pickupPoint,dropPoint)
    travelcost = getTravelcost(traveltime)
    dropTime = pickupTime + traveltime

    nearestTaxi.updateCurrentLocation(dropPoint)
    nearestTaxi.updateAvailableFrom(dropTime)
    nearestTaxi.updateEarnings(travelcost)

    trip = Trip(pickupPoint,dropPoint,nearestTaxi.getId(),pickupTime,dropTime)

    nearestTaxi.addTrip(trip)

    print(f"Taxi - {nearestTaxi.getId()} is booked")
    print()

    return

def getPickupPoint():
    print("Enter Pickup Point")
    pickupPoint = input()
    if pickupPoint in 'ABCDEF':
        return pickupPoint
    print("Invalid PickupPoint")
    return getPickupPoint()

def getDropPoint(pickupPoint):
    print("Enter Drop Point")
    dropPoint = input()
    if dropPoint not in ['A','B','C','D','E','F'] or dropPoint == pickupPoint:
        print("Invalid PickupPoint")
        dropPoint = getDropPoint(pickupPoint)
    return dropPoint
    

def getpickupTime():
    print("Enter Pickup Time")
    pickupTime = input()
    try:
        pickupTime = int(pickupTime)
    except:
        print("Invalid PickupTime")
        pickupTime = getpickupTime()
    return int(pickupTime)


def booking():
    pickupPoint = getPickupPoint()
    dropPoint = getDropPoint(pickupPoint)
    pickupTime = getpickupTime()

    bookTaxi(pickupPoint,dropPoint,pickupTime)
    return

def details(taxies):
    for taxi in taxies:
        taxi.getDetails()
        print("**********")


if __name__ == "__main__":
    n = 4
    taxies = []
    for i in range(n):
        taxi = Taxi()
        taxies.append(taxi)


    while (True):
        
        print("Type 1 for Booking")
        print("Type 2 for taxi Details")
        print("Type 0 to Exit")
        module = input()

        if module == "1":
            booking()

        elif module == "2":
            details(taxies)

        elif module == "0":
            break
        
        continue


