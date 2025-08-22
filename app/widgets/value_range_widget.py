"""Value Range Widget for min/max input ranges"""

from textual.widgets import Input, Static
from textual.containers import VerticalGroup, HorizontalGroup


class ValueRangeWidget(VerticalGroup):
    """Widget for min/max value input ranges"""
    
    def __init__(self, label: str, min_id: str, max_id: str):
        super().__init__()
        self.label = label
        self.min_id = min_id
        self.max_id = max_id
    
    def compose(self):
        yield Static(f"{self.label} Range", classes="field-label")
        yield HorizontalGroup(
            Input(placeholder="Min", id=self.min_id, classes="number-input"),
            Input(placeholder="Max", id=self.max_id, classes="number-input"),
        )