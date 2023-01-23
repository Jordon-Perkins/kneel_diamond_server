from copy import deepcopy
import sqlite3
import json
from models import Order

# from .metal_requests import get_single_metal
# from .size_requests import get_single_size
# from .style_requests import get_single_style

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
    # Open a connection to the database
    with sqlite3.connect("./kneel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.style_id,
            o.size_id,
            o.timestamp
        FROM orders o
        """)

        # Initialize an empty list to hold all animal representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            order = Order(row['id'], row['metal_id'], row["size_id"], row["style_id"], row["timestamp"])

            orders.append(order.__dict__)

    return orders

# Function with a single parameter
def get_single_order(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM orders o
        WHERE o.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return {}

        # Create an animal instance from the current row
        order = Order(data['id'], data['metal_id'], data['size_id'],
                            data['style_id'], data['timestamp'])

        return order.__dict__


# def get_single_order(id):
#     # Variable to hold the found metal, if it exists
#     requested_order = None


#     for order in ORDERS:
#         if order["id"] == id:
#             requested_order = deepcopy(order)

#             styleId = requested_order["styleId"]
#             style = get_single_style(styleId)
#             requested_order["style"] = style

#             metalId = requested_order["metalId"]
#             metal = get_single_metal(metalId)
#             requested_order["metal"] = metal

#             sizeId = requested_order["sizeId"]
#             size = get_single_size(sizeId)
#             requested_order["size"] = size

#             del requested_order["styleId"]
#             del requested_order["metalId"]
#             del requested_order["sizeId"]

#     return requested_order


def create_order(new_order):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO orders
            ( size_id, metal_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['size_id'], new_order['metal_id'],
                new_order['style_id'], new_order['timestamp']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_order['id'] = id

        return new_order

# def create_order(order):
#     # Get the id value of the last animal in the list
#     max_id = ORDERS[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the animal dictionary
#     order["id"] = new_id

#     # Add the animal dictionary to the list
#     ORDERS.append(order)

#     # Return the dictionary with `id` property added
#     return order

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