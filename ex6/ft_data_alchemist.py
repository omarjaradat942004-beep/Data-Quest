import random


if __name__ == "__main__":

    names: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan',
        'Emma', 'Gregory', 'john', 'kevin', 'Liam'
    ]

    lst_all_cap: list[str] = [name.capitalize() for name in names]

    lst_only_cap: list[str] = [
        name for name in names if name[0].isupper()
    ]

    dict_all_cap: dict[str, int] = {
        key.capitalize(): random.randint(0, 1000)
        for key in names
    }

    score_average: float = round(
        sum(dict_all_cap.values()) / len(dict_all_cap), 2
    )

    dict_high_sco: dict[str, int] = {
        key.capitalize(): random.randint(
            int(score_average + 1), 10000
        )
        for key in names
    }

    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {lst_all_cap}")
    print(f"New list of capitalized names only: {lst_only_cap}")
    print(f"Score dict: {dict_all_cap}")
    print(f"Score average is {score_average}")
    print(f"High scores: {dict_high_sco}")
