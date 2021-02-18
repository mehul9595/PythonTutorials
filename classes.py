class Vehicle: 
    name = ""
    model = ""
    year = ""

    def vehicleInfo(self):
        info = "My car name is %s - %s - %d" % (self.name, self.model, self.year)
        return info
    
def main():
    vehicleObject = Vehicle()
    vehicleObject.model = "Tesla"
    vehicleObject.name = "Ferrai"
    vehicleObject.year = 2020
    print(vehicleObject.vehicleInfo())

if __name__ =="__main__":
    main()