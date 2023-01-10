class Order():
    """Class that defines the properties for a metal object"""

    # Write the __init__ method here

    def __init__(self, id, metalId, sizeId, styleId, timestamp):
        self.id = id
        self.metalId = metalId
        self.sizeId = sizeId
        self.styleId = styleId
        self.timestamp = timestamp