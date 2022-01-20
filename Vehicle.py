class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None

    def set_vehicle_type(self, vehicle_type):
        if vehicle_type == "FourWheeler" or vehicle_type == "TwoWheeler":
            self.__vehicle_type = vehicle_type
        else:
            return "Invalid"

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        vehicle_type_calculation = self.get_vehicle_type()
        if vehicle_type_calculation == "TwoWheeler":
            self.__premium_amount = (2 * self.get_vehicle_cost()) / 100
            return self.__premium_amount
        elif vehicle_type_calculation == "FourWheeler":
            self.__premium_amount = (6 * self.get_vehicle_cost()) / 100
            return self.__premium_amount
        else:
            return "Invalid Vehicle Type"

    def display_vehicle_details(self):
        print(
            self.__vehicle_type,
            self.__vehicle_cost,
            self.__premium_amount)


vehicle1 = Vehicle()
vehicle1.set_vehicle_type(input())
vehicle1.set_vehicle_cost(int(input()))
print(vehicle1.calculate_premium())
vehicle1.display_vehicle_details()
