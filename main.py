from Game import Game


if __name__ == "__main__":
    game = Game()
    game.start()

    while game.is_running:
        game.update()
        # Add a condition to break the loop and end the game
        user_input = input("Type 'exit' to end the game: ")
        if user_input.lower() == 'exit':
            game.end_game()
        break