from homework2.rewards.i_game_item import IGameItem


class Sapphire(IGameItem):
    def open(self):
        print('Sapphire! ', end="")