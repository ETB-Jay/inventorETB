"""Time Widget for ShopifyQL Query Builder"""

from textual.widgets import Input, Select
from textual.containers import VerticalGroup


class TimeWidget(VerticalGroup):
    """Widget for time-related fields"""
    
    def __init__(self):
        super().__init__()
        
    def compose(self):
        yield Input(placeholder="Month", id="month", classes="text-input")
        yield Input(placeholder="Day", id="day", classes="text-input")
        yield Input(placeholder="Quarter", id="quarter", classes="text-input")
        yield Input(placeholder="Week", id="week", classes="text-input")
        yield Input(placeholder="Year", id="year", classes="text-input")
