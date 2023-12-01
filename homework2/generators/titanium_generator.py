from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.titanium import Titanium


class TitaniumGenerator(ItemFabric):
    def create_item(self):
        return Titanium()