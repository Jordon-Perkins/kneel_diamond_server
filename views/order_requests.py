from copy import deepcopy

from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style

ORDERS = [
        {
            "id": 1,
            "metalId": 3,
            "sizeId": 2,
            "styleId": 3,
            "timestamp": 1614659931693
        }
    ]

def get_all_orders():
    return ORDERS

# Function with a single parameter
def get_single_order(id):
    # Variable to hold the found metal, if it exists
    requested_order = None


    for order in ORDERS:
        if order["id"] == id:
            requested_order = deepcopy(order)

            styleId = requested_order["styleId"]
            style = get_single_style(styleId)
            requested_order["style"] = style

            metalId = requested_order["metalId"]
            metal = get_single_metal(metalId)
            requested_order["metal"] = metal

            sizeId = requested_order["sizeId"]
            size = get_single_size(sizeId)
            requested_order["size"] = size

            del requested_order["styleId"]
            del requested_order["metalId"]
            del requested_order["sizeId"]

    return requested_order


def create_order(order):
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    # Initial -1 value for animal index, in case one isn't found
    order_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            order_index = index

    # If the animal was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break