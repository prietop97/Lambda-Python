class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Food(Item):
    def __init__(self, name, description, calories):
        super().__init__(name, description)
        self.calories = calories

# class Watermelon(Food):
#     def __init__():
#         super().__init__("Watermelon", "It's a watermelon", 20)

# class Rice(Food):
#     def __init__():
#         super().__init__("Rice","It's rice",15)

# class Steak(Food):
#     def __init__():
#         super().__init__("Steak","It's a welldone steak",40)
