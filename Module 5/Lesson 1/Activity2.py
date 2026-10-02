class vehicle:

    #Constructor
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ford = vehicle(240,20)
print(f"Ford has a maximum speed of {ford.max_speed}km/h. It has mileage of {ford.mileage}")