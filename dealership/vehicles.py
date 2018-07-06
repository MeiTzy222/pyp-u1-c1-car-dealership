sale_multiplier_car = 1.2
sale_multiplier_motorcycle = 1.1
sale_multiplier_truck = 1.6
purchase_multiplier_car = 0.004
purchase_multiplier_motorcycle = 0.009
purchase_multiplier_truck = 0.02


class Vehicle(object):
    def __init__(self, maker, model, year, base_price, miles):
        self.maker = maker
        self.model = model
        self.year = year
        self.base_price = base_price
        self.miles = miles


class Car(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Car, self).__init__(maker, model, year, base_price, miles)

    def sale_price(self):
        return self.base_price * sale_multiplier_car
        
    def purchase_price(self):
        return self.sale_price() - purchase_multiplier_car * self.miles

    
class Motorcycle(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Motorcycle, self).__init__(maker, model, year, base_price, miles)

    def sale_price(self):
        return self.base_price * sale_multiplier_motorcycle

    def purchase_price(self):
        return self.sale_price() - purchase_multiplier_motorcycle * self.miles


class Truck(Vehicle):
    def __init__(self, maker, model, year, base_price, miles):
        super(Truck, self).__init__(maker, model, year, base_price, miles)

    def sale_price(self):
        return self.base_price * sale_multiplier_truck
        
    def purchase_price(self):
        return self.sale_price() - purchase_multiplier_truck * self.miles
