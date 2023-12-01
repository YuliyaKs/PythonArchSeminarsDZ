from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.gem import Gem


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()