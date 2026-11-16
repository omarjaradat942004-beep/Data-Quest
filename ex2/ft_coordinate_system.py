import math


def get_player_pos() -> tuple[int | float, ...]:
    try:
        Tuple: tuple[int | float, ...] = ()
        Input: str = input("Enter new coordinates as"
                           "floats in format ’x,y,z’: ")
        size: int = 0
        for i in Input:
            size += 1
        index: int = 0
        while (index < size):
            if (Input[index] == ','):
                break
            index += 1
        first_comma: int = index
        index += 1
        while (index < size):
            if (Input[index] == ','):
                break
            index += 1
        second_comma: int = index
        Tuple += (float(Input[:first_comma]),)
        Tuple += (float(Input[first_comma + 1: second_comma]),)
        Tuple += (float(Input[second_comma + 1:]),)
        return (Tuple)
    except ValueError as e:
        if (first_comma != size and second_comma != size
                and first_comma != second_comma):
            if (len(Tuple) == 0):
                print(f"Error on parameter ’{Input[:first_comma]}’: {e}")
            elif (len(Tuple) == 1):
                print(f"Error on parameter ’"
                      f"{Input[first_comma + 1:second_comma]}’: {e}")
            elif (len(Tuple) == 2):
                third_comma: int = 0
                for i in Input[second_comma + 1:]:
                    if (i == ","):
                        third_comma += 1
                if (third_comma):
                    print("Invalid syntax")
                else:
                    print(f"Error on parameter ’"
                          f"{Input[second_comma + 1:]}’: {e}")
        else:
            print("Invalid syntax")
        return (get_player_pos())


def get_player_pos_helper_function() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    Tuple: tuple[int | float, ...] = get_player_pos()
    print(f"Got a first tuple: {Tuple}")
    print(f"It includes: X={Tuple[0]}, Y={Tuple[1]}, Z={Tuple[2]},")
    Distance: float = math.sqrt(Tuple[0] ** 2 + Tuple[1] ** 2 + Tuple[2] ** 2)
    print(f"Distance to center: {round(Distance, 4)}\n")
    print("Get a second set of coordinates")
    Tuple2: tuple[int | float, ...] = get_player_pos()
    coordinates: float = math.sqrt((Tuple2[0] - Tuple[0])**2 +
                                   (Tuple2[1] - Tuple[1])**2 +
                                   (Tuple2[2] - Tuple[2])**2)
    print(f"Distance between the 2 sets of"
          f"coordinates: {round(coordinates, 4)}")


if (__name__ == "__main__"):
    get_player_pos_helper_function()
