from homework2.rewards.i_game_item import IGameItem


class Alexandrite(IGameItem):
    def open(self):
        print('Alexandrite! ', end="")