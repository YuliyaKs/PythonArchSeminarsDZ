from homework2.rewards.i_game_item import IGameItem


class Titanium(IGameItem):
    def open(self):
        print('Titanium! ', end="")