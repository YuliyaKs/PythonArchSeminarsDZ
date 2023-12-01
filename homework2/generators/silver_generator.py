from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.silver import Silver


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()