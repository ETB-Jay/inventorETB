# ShopifyQL Query Builder

A comprehensive terminal-based GUI for building ShopifyQL queries with an intuitive interface.

## Features

### Query Building Capabilities
- **Date Range Filtering**: Set start and end dates for time-based queries
- **Value & Quantity Ranges**: Filter by product prices and quantities with validation
- **Product Filters**: Filter by product type, vendor, and tags
- **Order Filters**: Filter by order status and financial status
- **Customer Filters**: Filter by customer email and location

### Advanced Features
- **Real-time Validation**: Input validation with helpful error messages
- **Sample Queries**: Built-in examples to get you started
- **Query Generation**: Automatically builds proper ShopifyQL syntax
- **Cross-platform**: Runs on Windows, macOS, and Linux
- **Keyboard Shortcuts**: 
  - `Ctrl+C`: Copy generated query
  - `Ctrl+R`: Clear all form fields
  - `D`: Toggle dark/light mode

## Installation

1. Install Python 3.7+ if not already installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Launch in New Window (Recommended)
```bash
python launcher.py
```

### Launch in Current Terminal
```bash
python app.py
```

### Launch with Command Line Option
```bash
python app.py --new-window
```

## File Structure

- `app.py` - Main application with UI logic
- `widgets.py` - Custom UI components and form widgets
- `query_builder.py` - ShopifyQL query generation logic
- `styles.py` - CSS styling definitions
- `launcher.py` - Cross-platform window launcher
- `requirements.txt` - Python dependencies

## Sample Queries

The app includes several sample queries to help you get started:

- **Products by Type**: Filter products by their type
- **High Value Orders**: Find orders above a certain value
- **Recent Customers**: Get customers from a specific date range
- **Tagged Products**: Find products with specific tags

## ShopifyQL Entity Types

The query builder automatically determines the appropriate entity type based on your filters:

- **Products**: When using product-specific filters (type, vendor, tags)
- **Orders**: When using order-specific filters (status, financial status)
- **Customers**: When using customer-specific filters (email, country)

## Tips

1. **Date Format**: Use YYYY-MM-DD format for dates (e.g., 2024-01-15)
2. **Tags**: Separate multiple tags with commas
3. **Validation**: The app validates number ranges to ensure min ≤ max
4. **Copy Queries**: Use Ctrl+C to copy generated queries to clipboard
5. **Clear Form**: Use Ctrl+R or the Clear All button to reset all fields

## Keyboard Shortcuts

- `D`: Toggle between dark and light themes
- `Ctrl+C`: Copy the generated query to clipboard
- `Ctrl+R`: Clear all form fields
- `Escape`: Exit the application

## Requirements

- Python 3.7+
- textual>=0.41.0
- pyperclip>=1.8.2 (optional, for clipboard functionality)