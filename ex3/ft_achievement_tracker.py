import random


def set_generator(achievement: list[str]) -> set[str]:
    sets: set[str] = set()
    set_size = random.randint(1, len(achievement))
    while (len(sets) < set_size):
        sets.add(random.choice(achievement))
    return (sets)


def gen_player_achievements() -> None:
    achievement: list[str] = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "Unstoppable",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder"
        "Strategist"
    ]

    Alice: set[str] = set_generator(achievement)
    Bob: set[str] = set_generator(achievement)
    Charlie: set[str] = set_generator(achievement)
    Dylan: set[str] = set_generator(achievement)

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}\n")
    print(f"All distinct achievements: {Alice.union(Bob, Charlie, Dylan)}")
    print(f"Common achievements: {Alice.intersection(Bob, Charlie, Dylan)}\n")

    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Bob, Alice, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Bob, Charlie, Alice)}\n")

    print(f"Alice is missing: {set(achievement).difference(Alice)}")
    print(f"Bob is missing: {set(achievement).difference(Bob)}")
    print(f"Charlie is missing: {set(achievement).difference(Charlie)}")
    print(f"Dylan is missing: {set(achievement).difference(Dylan)}")


if (__name__ == "__main__"):
    gen_player_achievements()
