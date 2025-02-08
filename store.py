from typing import List
from products import Product

class Store:
    def __init__(self, products: List[Product]):
        self.products = products
    
    def add_product(self, product: Product):
        self.products.append(product)
    
    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
    
    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)
    
    def get_all_products(self) -> List[Product]:
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list: List[tuple]) -> float:
        total_cost = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise ValueError("Product not found in store.")
            total_cost += product.buy(quantity)
        return total_cost
