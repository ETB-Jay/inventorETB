"""CSS Styles for ShopifyQL Query Builder"""

import os
from pathlib import Path

def load_css_file(filename: str) -> str:
    """Load CSS content from a file"""
    css_dir = Path(__file__).parent
    css_file = css_dir / filename
    if css_file.exists():
        return css_file.read_text(encoding='utf-8')
    return ""

# Load all CSS files
CSS_FILES = [
    'base.tcss',
    'layout.tcss', 
    'forms.tcss',
    'controls.tcss',
    'output.tcss'
]

# Combine all CSS files
MAIN_CSS = "\n".join(load_css_file(css_file) for css_file in CSS_FILES)