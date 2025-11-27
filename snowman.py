from game_logic import play_game


if __name__ == "__main__":
    print("Welcome to Snowman Meltdown! ❄️\n")

    while True:

        # Starte eine Spielrunde
        play_game()

        # Replay-Option
        replay = input("Do you want to play again? (y/n): ").lower()
        while replay not in ["y", "n"]:
            replay = input("Please enter 'y' for yes or 'n' for no: ").lower()

        if replay == "n":
            print("\nThanks for playing Snowman Meltdown! 🎉❄️")
            break

        # Trennung zwischen Runden für bessere Lesbarkeit
        print("\n" + "=" * 40 + "\n")
