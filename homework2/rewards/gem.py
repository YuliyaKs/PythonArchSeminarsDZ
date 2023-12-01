from homework2.rewards.i_game_item import IGameItem


class Gem(IGameItem):
    def open(self):
        print('Gem!')