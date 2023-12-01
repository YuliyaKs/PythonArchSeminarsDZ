from homework2.rewards.i_game_item import IGameItem


class Platinum(IGameItem):
    def open(self):
        print('Platinum! ', end="")