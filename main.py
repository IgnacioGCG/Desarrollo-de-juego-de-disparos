from Game import Game


if __name__ == "__main__":
    game = Game()
    game.start()
    game.update()
    game.end_game()
    print(game)
    game.reset_game()
    