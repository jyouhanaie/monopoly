class Space():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_position():
        return self.position
        
class Property(Space):
    def __init__(self, color, cost, rent_costs, *args, **kwargs):
        
        self.color = color
        self.cost = cost
        
        self.rent_costs = rent_costs
        self.house_count = 0
        self.hotel_count = 0
        
        self.isRailroad = False
        
        super().__init__(*args, **kwargs)
        
        self.owner = "unowned"
        self.mortgaged = False

    def get_rent_cost(self):
        return self.rent_costs[self.house_count + (5 * self.hotel_count)]
        
        
        
class Railroad(Space):
    def __init__(self, cost, *args, **kwargs):
        self.cost = cost
        #is this a smart way of doing this? idk
        self.house_count = 0
        self.hotel_count = 0
        self.rent_costs = [25, 50, 100, 200]
        self.isRailroad = True
        self.mortgaged = False
        
        super().__init__(*args, **kwargs)
    def get_rent_cost(self):
        return self.rent_costs[self.house_count]
        
class Utility(Space):
    def __init__(self, *args, **kwargs):
        self.cost = 150
        self.mortgaged = False
        self.isRailroad = True
        self.house_count = 0
        self.hotel_count = 0
        super().__init__(*args, **kwargs)