import sys

if (__name__ == "__main__"):
    print("=== Player Score Analytics ===")
    if (len(sys.argv) == 1):
        print("No scores provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        index: int = 1
        scores: list[int] = []
        while (index < len(sys.argv)):
            try:
                int(sys.argv[index])
                scores += [int(sys.argv[index])]
            except ValueError:
                print(f"Invalid parameter: ’{sys.argv[index]}’")
            index += 1
        if (len(scores) == 0):
            print("No scores provided. Usage: python3"
                  "ft_score_analytics.py <score1> <score2> ...")
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
