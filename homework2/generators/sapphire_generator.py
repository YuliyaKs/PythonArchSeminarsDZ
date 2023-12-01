from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.sapphire import Sapphire


class SapphireGenerator(ItemFabric):
    def create_item(self):
        return Sapphire()