import sys

def finding_duplicates(lst1: list[str], lst2: list[str]) -> list[str]:
    index: int = 0
    index2: int = 1
    while (index < len(lst2)):
        index2 = index + 1
        while (index2 < len(lst2)):
            if (lst2[index][:lst[index]] == lst2[index2][:lst[index]]):
                lst2.pop(index2)
                print(f"Redundant item ’{lst2[index][:lst[index]]}’ - discarding")
            index2 += 1
        index += 1
    return (lst2)



if __name__ == "__main__":
    inventory: dict[str, int] = {}

    lst: list[str] = []
    lst2: list[str] = []

    lst_size = len(sys.argv)
    index: int = 1
    index2: int = 0
    comma_pos: int = -1

    while (index < lst_size):
        index2 = 0
        comma_pos = -1
        while (index2 < len(sys.argv[index])):
            if (sys.argv[index][index2] == ':'):
                comma_pos = index2
            index2 += 1
        if (comma_pos == 0 or comma_pos == -1):
            print(f"Error - invalid parameter {sys.argv[index]}")
        else:
            lst += [comma_pos]
            lst2 += [sys.argv[index]]
        index += 1

    index = 0
    index2 = 0
    lst2 = finding_duplicates(lst, lst2)
    while (index < len(lst2) and index2 < len(lst)):
        try:
            inventory[str(lst2[index][:lst[index2]])] = int(lst2[index][lst[index2] + 1:])

        except ValueError:
            print(f"Quantity error for ’{lst2[index][:lst[index2]]}’: invalid literal for int() for base  ’{lst2[index][lst[index2] + 1:]}’")
        index += 1
        index2 += 1

    #round(inventory[lst_items[index]] / sum(inventory.values()), 1)
    lst_items: list[str] = list(inventory.keys())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {lst_items}")
    print(f"Total quantity of the {len(lst_items)} items: {sum(inventory.values())}")
    index = 0
    while (index < len(lst_items)):
        print(f"Item {lst_items[index]} represents {round((inventory[lst_items[index]] / sum(inventory.values()) * 100), 1)}%")
        index += 1



