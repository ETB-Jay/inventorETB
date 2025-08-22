"""Product Details Widget for ShopifyQL Query Builder"""

from textual.widgets import Input, Select
from textual.containers import VerticalGroup


class ProductDetailsWidget(VerticalGroup):
    """Widget for product detail fields"""
    
    def __init__(self):
        super().__init__()
        
    def compose(self):
        yield Input(placeholder="Product ID", id="product_id", classes="text-input")
        yield Input(placeholder="Product Tags", id="product_tags", classes="text-input")
        yield Input(placeholder="Product Title", id="product_title", classes="text-input")
        yield Input(placeholder="Product Type", id="product_type", classes="text-input")
        yield Input(placeholder="Product Variant ABC Grade", id="product_variant_abc_grade", classes="text-input")
        yield Input(placeholder="Product Vendor", id="product_vendor", classes="text-input")
        yield Input(placeholder="Product Collections", id="product_collections", classes="text-input")