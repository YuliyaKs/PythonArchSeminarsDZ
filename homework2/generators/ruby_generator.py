from homework2.generators.item_fabric import ItemFabric
from homework2.rewards.ruby import Ruby


class RubyGenerator(ItemFabric):
    def create_item(self):
        return Ruby()