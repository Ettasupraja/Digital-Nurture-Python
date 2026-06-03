def display_coordinates(coords):
    if len(coords) != 2:
        return "Invalid Coordinates"

    x, y = coords
    return f"X = {x}, Y = {y}"

print(display_coordinates((10, 20)))