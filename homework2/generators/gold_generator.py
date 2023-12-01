from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.gold import Gold


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()