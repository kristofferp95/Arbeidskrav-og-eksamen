from datetime import datetime

class Flight:
    def __init__(self, f_number = "", departureTime = datetime(2010, 1, 1, 1, 1, 1), arrivalTime = datetime(2010, 1, 1, 1, 1, 1)):
        self.f_number = f_number
        self.departureTime = departureTime
        self.arrivalTime = arrivalTime

    def getflightNumber(self):
        return self.f_number

    def getDepartureTime(self):
        return self.departureTime
    
    def setDeparturetime(self, x, x1, x2, x3, x4, x5):
        self.departureTime = datetime(x, x1, x2, x3, x4, x5)
    
    def getArrivaltime(self):
        return self.arrivalTime

    def SetArrivalTime(self, z, z1, z2, z3, z4, z5):
        self.arrivalTime = datetime(z, z1, z2, z3, z4, z5)

    def getFlighttime(self):
        hours = (self.arrivalTime.hour - self.departureTime.hour) * 60
        minutes = self.arrivalTime.minute - self.departureTime.minute

        return int(hours + minutes)

class Itinerary:
    def __init__(self, flights = []):
        self.flights = flights
        self.flights.sort(key=Flight.getDepartureTime)
    
    def getTotalFlightTime(self):
        totaltime = 0
        for i in range(0, len(self.flights)):
            sum = int(Flight.getFlighttime(self.flights[i]))
            totaltime += sum

        return totaltime

    def getTotalTravelTime(self):
        hours = (self.flights[len(self.flights)-1].arrivalTime.hour - self.flights[0].departureTime.hour) * 60
        minutes = (self.flights[len(self.flights)-1].arrivalTime.minute - self.flights[0].departureTime.minute) 
        
        return (hours + minutes)

def main():
    flights = []
    flights.append(Flight("US237", datetime(2014, 4, 5, 9, 35, 0), datetime(2014, 4, 5, 12, 55, 0)))
    flights.append(Flight("US230", datetime(2014, 4, 5, 5, 5, 0), datetime(2014, 4, 5, 6, 15, 0)))
    flights.append(Flight("US235", datetime(2014, 4, 5, 6, 55, 0), datetime(2014, 4, 5, 7, 45, 0)))
    itinerary = Itinerary(flights)
    print(f'The total flighttime is {itinerary.getTotalFlightTime()} minutes')
    print(f'The total traveltime is {itinerary.getTotalTravelTime()} minutes')

main()
    

    
