from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.alexandrite import Alexandrite


class AlexandriteGenerator(ItemFabric):
    def create_item(self):
        return Alexandrite()