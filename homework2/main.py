from homework2.generators.gem_generator import GemGenerator
from homework2.generators.gold_generator import GoldGenerator
from homework2.generators.alexandrite_generator import AlexandriteGenerator
from homework2.generators.platinum_generator import PlatinumGenerator
from homework2.generators.ruby_generator import RubyGenerator
from homework2.generators.sapphire_generator import SapphireGenerator
from homework2.generators.silver_generator import SilverGenerator
from homework2.generators.titanium_generator import TitaniumGenerator
from random import randint

# Создаем список с генераторами наград
rewards = [
    GemGenerator(),
    GoldGenerator(),
    AlexandriteGenerator(),
    PlatinumGenerator(),
    RubyGenerator(),
    SapphireGenerator(),
    SilverGenerator(),
    TitaniumGenerator()
]

# Генерируем награды в соотношении:
# Алмазы в количестве 1, Золото в количестве 3
# Собственные награды в количестве 10
for i in range(20):
    index = randint(0, 7)
    if index == 0:
        rewards[index].create_item().open()
    elif index == 1:
        for j in range(3):
            rewards[index].create_item().open()
        print()
    else:
        for k in range(10):
            rewards[index].create_item().open()
        print()





