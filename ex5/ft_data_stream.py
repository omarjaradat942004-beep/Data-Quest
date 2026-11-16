import typing
import random


def gen_event() -> typing.Generator[tuple[str, str]]:
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    players = ["bob", "alice", "dylan", "charlie"]
    player_choice = random.choice(players)
    actions_choice = random.choice(actions)

    yield (player_choice, actions_choice)


def consume_event(
    lst_tuple: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    for i in range(10):
        index = random.randrange(len(lst_tuple))
        removed = lst_tuple[index]
        del lst_tuple[index]
        yield removed


if (__name__ == "__main__"):
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        gen = gen_event()
        nexts = next(gen)
        print(f"Event {i}: Player {nexts[0]} did action {nexts[1]}")
    lst_tuple: list[tuple[str, str]] = []
    for i in range(10):
        gen = gen_event()
        nexts = next(gen)
        lst_tuple += [nexts]
    ten_generator = consume_event(lst_tuple)
    for x in ten_generator:
        print(f"Got event from list {x}")
        print(f"Remains in list: {lst_tuple}")
