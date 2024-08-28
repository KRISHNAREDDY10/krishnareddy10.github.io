
class Product:
    def __init__(self,product_id,product_name,selling_price,inventory):
        self.product_id = product_id
        self.product_name = product_name
        self.selling_price = selling_price
        self.inventory = inventory
    
    def update_inventory(self,quantity):
        self.inventory += quantity

    def __str__(self):
        return  (f"Product\n"
                f"product_id={self.product_id}\n"
                f"product_name={self.product_name}\n"
                f"selling_price={self.selling_price}\n"
                f"inventory={self.inventory}")