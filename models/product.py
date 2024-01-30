from dataclasses import dataclass


@dataclass
class product_create:
    title: str
    price: float
    amount: int
    description: str

    def add_product_to_db(self) -> int:
        pass


@dataclass
class Product(product_create):
    id: int
    
    def add_product_to_db(self) -> int:
        raise TypeError("tried to create existing product")
    

    @classmethod
    def get_list_of_products(cls) -> list["Product"]:
        # logic to get list of products from db
        return [Product(123, "cup of tea", 1.99, 10, "the best cup of tea")]

    @classmethod
    def get_product_by_id(cls, id) -> "Product":
        return Product(123, "cup of tea", 1.99, 10, "the best cup of tea")

   

    def update_product_in_db(self) -> "Product":
        return Product(123, "cup of tea", 1.99, 10, "the best cup of tea")

    def delete_product_from_db(self) -> bool:
        # delete from product where id = ?, [self.id]
        return True
