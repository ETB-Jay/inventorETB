"""Main ShopifyQL Application Class"""

import pyperclip
from textual.app import App
from textual.widgets import Footer, Header, Button, TextArea, Static
from textual.containers import VerticalScroll, HorizontalGroup, VerticalGroup

# CSS files will be loaded directly by Textual
from widgets import (
    InventoryWidget,
    ProductDetailsWidget,
)
from query_builder import ShopifyQLQueryBuilder


class ShopifyQLApp(App):
    """A Textual App To Write ShopifyQL Scripts"""

    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("ctrl+c", "copy_query", "Copy query"),
        ("ctrl+r", "clear_form", "Clear form"),
        ("ctrl+s", "save_form", "Save form")
    ]
    CSS_PATH = [
        "styles/base.tcss",
        "styles/layout.tcss", 
        "styles/forms.tcss",
        "styles/controls.tcss",
        "styles/output.tcss"
    ]

    def __init__(self):
        super().__init__()
        self.query_builder = ShopifyQLQueryBuilder()

    def compose(self):
        yield Header()
        yield VerticalScroll(
            VerticalGroup(
                # Single grid row with three equal columns
                HorizontalGroup(
                    VerticalGroup(
                        Static("Inventory", classes="section-header"),
                        InventoryWidget(),
                        classes="form-section left-column"
                    ),
                    VerticalGroup(
                        Static("Product Details", classes="section-header"),
                        ProductDetailsWidget(),
                        classes="form-section right-column"
                    ),
                    id="main-grid-row"
                ),
                
                HorizontalGroup(
                    Button("Generate Query", id="generate-btn"),
                    Button("Clear All", id="clear-btn"),
                    Button("Samples", id="samples-btn"),
                    id="controls",
                ),
                
                TextArea(
                    "Generated ShopifyQL query will appear here...",
                    id="query-output",
                    read_only=True
                ),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses"""
        if event.button.id == "generate-btn":
            self.generate_query()
        elif event.button.id == "clear-btn":
            self.clear_form()
        elif event.button.id == "samples-btn":
            self.show_samples()

    def generate_query(self) -> None:
        """Generate ShopifyQL query from form inputs"""
        form_data = self.collect_form_data()
        query = self.query_builder.build_query(form_data)
        
        output_widget = self.query_one("#query-output")
        output_widget.text = query

    def collect_form_data(self) -> dict:
        """Collect all form data from inputs"""
        data = {}
        
        input_ids = [
            "inventory_item_cost", "inventory_item_id", "shop_id",
            "product_id", "product_tags", "product_title", "product_type", 
            "product_variant_abc_grade", "product_vendor", "product_collections",
            "month", "day", "quarter", "week", "year"
        ]
        
        for input_id in input_ids:
            try:
                widget = self.query_one(f"#{input_id}")
                value = getattr(widget, "value", "")
                if value and value.strip():
                    data[input_id] = value.strip()
            except:
                continue
        
        select_ids = []
        for select_id in select_ids:
            try:
                widget = self.query_one(f"#{select_id}")
                value = getattr(widget, "value", "")
                if value:
                    data[select_id] = value
            except:
                continue
        
        return data

    def clear_form(self) -> None:
        """Clear all form inputs"""
        input_selectors = [
            "#inventory_item_cost", "#inventory_item_id", "#shop_id",
            "#product_id", "#product_tags", "#product_title", "#product_type", 
            "#product_variant_abc_grade", "#product_vendor", "#product_collections",
            "#month", "#day", "#quarter", "#week", "#year"
        ]
        
        for selector in input_selectors:
            try:
                widget = self.query_one(selector)
                widget.value = ""
            except:
                continue
        
        select_selectors = []
        for selector in select_selectors:
            try:
                widget = self.query_one(selector)
                widget.value = ""
            except:
                continue
        
        output_widget = self.query_one("#query-output")
        output_widget.text = "Generated ShopifyQL query will appear here..."

    def show_samples(self) -> None:
        """Show sample queries in output"""
        samples = self.query_builder.get_sample_queries()
        sample_text = "Sample ShopifyQL Queries:\n\n"
        
        for name, query in samples.items():
            sample_text += f"# {name}\n{query}\n\n"
        
        output_widget = self.query_one("#query-output")
        output_widget.text = sample_text

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_copy_query(self) -> None:
        """Copy the generated query to clipboard"""
        output_widget = self.query_one("#query-output")
        query_text = output_widget.text
        
        if query_text and query_text != "Generated ShopifyQL query will appear here...":
            try:
                pyperclip.copy(query_text)
                self.notify("Query copied to clipboard!")
            except ImportError:
                self.notify("Install pyperclip to enable copy functionality")

    def action_clear_form(self) -> None:
        """Clear form via keyboard shortcut"""
        self.clear_form()
        

if __name__ == "__main__":
    app = ShopifyQLApp()
    app.run()