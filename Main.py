from monty_hall_game import MontyHall


if __name__ == "__main__":
    game = MontyHall()
    win_count = 0

    for i in range(1000):
        if game.play_game():
            win_count += 1

    print(f"\nWin rate when switching doors: {win_count / 1000}")

    win_count = 0

    for i in range(1000):
        if game.play_game(switch=False):
            win_count += 1

    print(f"\nWin rate when not switching doors: {win_count / 1000}")

