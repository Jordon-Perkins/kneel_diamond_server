class Order():
    """Class that defines the properties for a metal object"""

    # Write the __init__ method here

    def __init__(self, id, timestamp, style_id, metal_id, size_id):
        self.id = id
        self.timestamp = timestamp
        self.style_id = style_id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style = None
        self.metal = None
        self.size = None