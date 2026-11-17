import random


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
    ]


def gen_player_achievements(achievement: list[str]) -> set[str]:
    sets: set[str] = set()
    new_achievement: list[str] = list(set(achievement))
    set_size = random.randint(0, len(new_achievement))
    while (len(sets) < set_size):
        sets.add(random.choice(new_achievement))
    return (sets)


def set_generators(achievement: list[str]) -> None:

    alice: set[str] = gen_player_achievements(achievement)
    bob: set[str] = gen_player_achievements(achievement)
    charlie: set[str] = gen_player_achievements(achievement)
    dylan: set[str] = gen_player_achievements(achievement)

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")

    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}\n")

    print(f"Alice is missing: {set(achievement).difference(alice)}")
    print(f"Bob is missing: {set(achievement).difference(bob)}")
    print(f"Charlie is missing: {set(achievement).difference(charlie)}")
    print(f"Dylan is missing: {set(achievement).difference(dylan)}")


if (__name__ == "__main__"):
    set_generators(achievement)
