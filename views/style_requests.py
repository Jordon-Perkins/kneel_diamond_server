STYLES = [
        { "id": 1, "style": "Classic", "price": 500 },
        { "id": 2, "style": "Modern", "price": 710 },
        { "id": 3, "style": "Vintage", "price": 965 }
    ]

def get_all_styles():
    return STYLES

# Function with a single parameter
def get_single_style(id):
    # Variable to hold the found metal, if it exists
    requested_style = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for style in STYLES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if style["id"] == id:
            requested_style = style

    return requested_style

def create_style(style):
    # Get the id value of the last animal in the list
    max_id = STYLES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    style["id"] = new_id

    # Add the animal dictionary to the list
    STYLES.append(style)

    # Return the dictionary with `id` property added
    return style