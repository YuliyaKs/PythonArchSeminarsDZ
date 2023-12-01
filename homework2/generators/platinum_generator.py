from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.platinum import Platinum


class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Platinum()