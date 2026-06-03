def display_coordinates():
    coordinates = (10, 20)

    if len(coordinates) != 2:
        print("Invalid Coordinates")
        return

    print(f"X = {coordinates[0]}, Y = {coordinates[1]}")

display_coordinates()