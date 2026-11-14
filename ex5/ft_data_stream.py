import typing
import random


def gen_event() -> typing.Generator[tuple[str, str]]:
    Actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    Players = ["bob", "alice", "dylan", "charlie"]
    Player_choice = random.choice(Players)
    Actions_choice = random.choice(Actions)

    yield (Player_choice, Actions_choice)


def consume_event(
    lst_tuple: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    for i in range(10):
        removed = lst_tuple.pop(random.randrange(len(lst_tuple)))
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
