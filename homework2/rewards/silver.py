from homework2.rewards.i_game_item import IGameItem


class Silver(IGameItem):
    def open(self):
        print('Silver! ', end="")