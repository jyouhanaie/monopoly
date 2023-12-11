class Space():
    '''
    This class represents a space on the board
    '''
    def __init__(self, name, position):
        '''
        Constructs all the necessary attributes for the Space object
        
        name is an string representing the name of the property
        position is an int between 1 and 40 that represents this Space's location on the board
        '''
        self.name = name
        self.position = position
        
    def get_position():
        '''
        Gets the position of the Space object
        
        returns the value of self.position, which is an int between 1 and 40
        '''
        return self.position
        
class Property(Space):
    '''
    This class represents a space on the board that is specifically a purchasable, colored property
    '''
    def __init__(self, color, cost, rent_costs, *args, **kwargs):
        '''
        Constructs all the necessary attributes for the Property object
        
        color is a string that defines the color group that the Property is a part of
        cost is an int that equals the purchasing price of the Property
        rent_costs is a list of ints that defines the rent payments for landing on the property 
        depending on the number of houses/hotels on it and if it is part of a monopoly
        *args for any additional unnamed arguments used when creating a Property object
        **kwargs for any additional keyword arguments used when creating a Property object
        '''
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
        '''
        Determines the appropriate rent cost to charge based on the number of houses/hotels
        
        returns the correct int from the list of rent_costs
        '''
        return self.rent_costs[self.house_count + (5 * self.hotel_count)]
        
        
        
class Railroad(Space):
    '''
    This class represents a Railroad on the board
    '''
    def __init__(self, cost, *args, **kwargs):
        '''
        Constructs all the necessary attributes for the Property object
        
        cost is an int that equals the purchasing price of the Property
        *args for any additional unnamed arguments used when creating a Property object
        **kwargs for any additional keyword arguments used when creating a Property object
        '''
        self.cost = cost
        self.house_count = 0
        self.hotel_count = 0
        self.rent_costs = [25, 50, 100, 200]
        self.isRailroad = True
        self.mortgaged = False
        
        super().__init__(*args, **kwargs)
    
    def get_rent_cost(self):
        '''
        Determines the appropriate rent cost to charge based on the number of railroads owned by the player.
        Because all Railroad objects are iterated through in our main loop and the house_count and hotel_count
        of each Property oject is referenced, we must include these variables in our Railroad class. Thus, to minimize
        redundancy, we use house_count as a proxy for counting the number of railroads a player owns to determine rent
        
        returns the correct int from the list of rent_costs
        '''
        return self.rent_costs[self.house_count]
        
class Utility(Space):
    '''
    This class represents a Utility on the board
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructs all the necessary attributes for the Property object
        
        *args for any additional unnamed arguments used when creating a Property object
        **kwargs for any additional keyword arguments used when creating a Property object
        '''
        self.cost = 150
        self.mortgaged = False
        self.isRailroad = True
        self.house_count = 0
        self.hotel_count = 0
        super().__init__(*args, **kwargs)