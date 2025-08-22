"""Widgets package for ShopifyQL Query Builder"""

from .inventory_widget import InventoryWidget
from .product_details_widget import ProductDetailsWidget
from .time_widget import TimeWidget

__all__ = [
    'InventoryWidget',
    'ProductDetailsWidget',
    'TimeWidget'
]