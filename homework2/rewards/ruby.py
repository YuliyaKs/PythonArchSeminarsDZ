from homework2.rewards.i_game_item import IGameItem


class Ruby(IGameItem):
    def open(self):
        print('Ruby! ', end="")