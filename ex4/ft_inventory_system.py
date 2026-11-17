import sys


def finding_duplicates(lst: list[int], lst2: list[str]) -> list[str]:
    index: int = 0

    while index < len(lst2):
        index2: int = index + 1

        while index2 < len(lst2):
            if lst2[index][:lst[index]] == lst2[index2][:lst[index2]]:
                print(f"Redundant item '{lst2[index][:lst[index]]}'"
                      " - discarding")
                del lst2[index2]
                del lst[index2]
            else:
                index2 += 1

        index += 1

    return lst2


def find_max(inventory: dict[str, int], lst_items: list[str]) -> str:
    if (not lst_items):
        return ("")
    index: int = 1
    maxi_str: str = lst_items[0]
    maxi: int = inventory[lst_items[0]]
    while (index < len(lst_items)):
        if (maxi < inventory[lst_items[index]]):
            maxi = inventory[lst_items[index]]
            maxi_str = lst_items[index]
        index += 1
    return (maxi_str)


def find_min(inventory: dict[str, int], lst_items: list[str]) -> str:
    if (not lst_items):
        return ("")
    index: int = 1
    mini_str: str = lst_items[0]
    mini: int = inventory[lst_items[0]]
    while (index < len(lst_items)):
        if (mini > inventory[lst_items[index]]):
            mini = inventory[lst_items[index]]
            mini_str = lst_items[index]
        index += 1
    return (mini_str)


if __name__ == "__main__":
    inventory: dict[str, int] = {}

    lst: list[int] = []
    lst2: list[str] = []

    lst_size = len(sys.argv)

    if (lst_size == 1):
        print("Please Enter Arguments")
    else:
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
                inventory[str(lst2[index][:lst[index2]])] = (
                    int(lst2[index][lst[index2] + 1:])
                )

            except ValueError as e:
                print(f"Quantity error for '{lst2[index][:lst[index2]]}': {e}")

            index += 1
            index2 += 1

        lst_items: list[str] = list(inventory.keys())
        print(f"Got inventory: {inventory}")
        print(f"Item list: {lst_items}")
        print(f"Total quantity of the {len(lst_items)}"
              f" items: {sum(inventory.values())}")

        index = 0
        while (index < len(lst_items)):
            total: int = sum(inventory.values())
            percentage: float
            if (total == 0):
                percentage = 0
            else:
                percentage = round(
                    inventory[lst_items[index]] / total * 100, 1
                )
            print(f"Item {lst_items[index]} represents {percentage}%")
            index += 1

        maximum: str = find_max(inventory, lst_items)
        minimum: str = find_min(inventory, lst_items)
        if (maximum != ""):
            print(f"Item most abundant: {maximum}"
                  f" with quantity {inventory[maximum]}")
        if (minimum != ""):
            print(f"Item least abundant: {minimum}"
                  f" with quantity {inventory[minimum]}")

        inventory.update({"magic_item": 1})
