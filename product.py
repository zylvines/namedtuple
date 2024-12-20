# from typing import NamedTuple
#
# class Product(NamedTuple):
#     name: str
#     price: int
#     kg: str
#
#     def get_name(self):
#         return self.name
#
#     def get_price(self):
#         return self.price
#
#     def get_kg(self):
#         return self.kg
#
#     @staticmethod
#     def discount_price(price: float, discount: float) -> float:
#         return price * (1 - discount / 100)
#
# product = Product(name="compyuter", price=17.000, kg="700gr")
# discounted_price = Product.discount_price(product.price, 20)
#
# print(f"Product {product} Discounted Price: {discounted_price}")
