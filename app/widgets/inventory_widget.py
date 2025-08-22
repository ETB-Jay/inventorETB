"""Inventory Widget for ShopifyQL Query Builder"""

from textual.widgets import Input, Select
from textual.containers import VerticalGroup


class InventoryWidget(VerticalGroup):
    """Widget for inventory-related fields"""
    
    def __init__(self):
        super().__init__()
        
    def compose(self):
        yield Input(placeholder="Inventory Item Cost", id="inventory_item_cost", classes="number-input")
        yield Input(placeholder="Inventory Item ID", id="inventory_item_id", classes="text-input")
        yield Input(placeholder="Shop ID", id="shop_id", classes="text-input")
