interest_car = 1.07
interest_motorcycle = 1.03
interest_truck = 1.11
employee_discounted_price = 0.9
lease_multiplier_car = 1.2
lease_multiplier_motorcycle = 1.0
lease_multiplier_truck = 1.7

from dealership.vehicles import Car, Truck, Motorcycle
from dealership.customers import Customer, Employee


class Contract(object):
    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):    
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
  
    def total_value(self):
        if isinstance(self.vehicle, Car):
            car_price = self.vehicle.sale_price() + (interest_car * self.monthly_payments * self.vehicle.sale_price() / 100)
            if self.customer.is_employee():
                return car_price * employee_discounted_price
            else:
                return car_price

        if isinstance(self.vehicle, Motorcycle):
            motorcycle_price = self.vehicle.sale_price() + (interest_motorcycle * self.monthly_payments * self.vehicle.sale_price() / 100)
            if self.customer.is_employee():
                return motorcycle_price * employee_discounted_price
            else:
                return motorcycle_price
        
        if isinstance(self.vehicle, Truck):
            truck_price = self.vehicle.sale_price() + (interest_truck * self.monthly_payments * self.vehicle.sale_price() / 100)
            if self.customer.is_employee():
                return truck_price * employee_discounted_price
            else:
                return truck_price

    def monthly_value(self):
        return self.total_value() / self.monthly_payments
    
    
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
    
    def total_value(self):
        if isinstance(self.vehicle, Car):
            car_lease_price = self.vehicle.sale_price() + (self.vehicle.sale_price() * lease_multiplier_car / self.length_in_months)
            if self.customer.is_employee():
                return car_lease_price * employee_discounted_price
            else:
                return car_lease_price
       
        if isinstance(self.vehicle, Motorcycle):
            motorcycle_lease_price = self.vehicle.sale_price() + (self.vehicle.sale_price() * lease_multiplier_motorcycle / self.length_in_months)
            if self.customer.is_employee():
                return motorcycle_lease_price * employee_discounted_price
            else:
                return motorcycle_lease_price

        if isinstance(self.vehicle, Truck):
            truck_lease_price = self.vehicle.sale_price() + (self.vehicle.sale_price() * lease_multiplier_truck / self.length_in_months)
            if self.customer.is_employee():
                return truck_lease_price * employee_discounted_price
            else:
                return truck_lease_price
                
    def monthly_value(self):
        return self.total_value() / self.length_in_months
        