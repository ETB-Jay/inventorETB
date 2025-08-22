"""Date Range Widget for date selection"""

from textual.widgets import Input, Static
from textual.containers import VerticalGroup


class DateRangeWidget(VerticalGroup):
    """Widget for date range selection"""
    
    def compose(self):
        yield Static("Start Date", classes="field-label")
        yield Input(placeholder="YYYY-MM-DD", id="start_date", classes="text-input")
        yield Static("End Date", classes="field-label")
        yield Input(placeholder="YYYY-MM-DD", id="end_date", classes="text-input")