import pandas as pd
from config import CSV_FILE_PATH, RANGES

def getInventoryItemValue(row: pd.Series) -> float:
    """getInventoryItemValue gets the value per unit of an inventory item

    Args:
        row (pd.Series): The row containing the inventory item information

    Returns:
        float: The value per unit of the inventory item
    """
    inventory_value = row["Ending inventory retail value"]
    inventory_units = row["Ending inventory units"]
    
    if inventory_units == 0:
        return 0
    
    return inventory_value / inventory_units

def writeSummary(df: pd.DataFrame):
    """writeSummary writes the summary of the dataset

    Args:
        df (pd.DataFrame): The dataset
    """
    
    # Create summary statistics
    summary_lines = []
    summary_lines.append("CSV INVENTORY SUMMARY REPORT")
    summary_lines.append("=" * 50)
    summary_lines.append("")
    
    # Basic DataFrame info
    summary_lines.append("📊 BASIC INVENTORY STATISTICS")
    summary_lines.append("-" * 30)
    summary_lines.append(f"Total number of products: {len(df)}")
    summary_lines.append(f"Total ending inventory units: {df['Ending inventory units'].sum():,.0f}")
    summary_lines.append(f"Total ending inventory retail value: ${df['Ending inventory retail value'].sum():,.2f}")
    summary_lines.append("")
    
    # Products with zero inventory
    summary_lines.append("⚠️  ZERO INVENTORY PRODUCTS")
    summary_lines.append("-" * 30)
    zero_inventory = df[df['Ending inventory units'] == 0]
    summary_lines.append(f"Products with zero inventory: {len(zero_inventory)}")
    summary_lines.append("")
    
    # Ranges 
    summary_lines.append("📈 INVENTORY VALUE RANGES")
    summary_lines.append("-" * 30)
    for range in RANGES:
        min = range["min"]
        max = range["max"]
        collection = range.get("collection", ["Unknown"])
        # Remove duplicates from collection names
        unique_collections = list(dict.fromkeys(collection))
        df_range = df[(df["Inventory item value"] >= min) & (df["Inventory item value"] <= max)]
        
        # Calculate all unit-related metrics
        total_units = df_range['Ending inventory units'].sum()
        total_value = df_range['Ending inventory retail value'].sum()
        avg_item_value = df_range['Inventory item value'].mean() if len(df_range) > 0 else 0
        num_products = len(df_range)
        
        summary_lines.append(f"Range {min} - {max} ({', '.join(unique_collections)}):")
        summary_lines.append(f"  • Total Units: {total_units:,}")
        summary_lines.append(f"  • Total Value: ${total_value:,.2f}")
        summary_lines.append(f"  • Number of Products: {num_products}")
        summary_lines.append(f"  • Average Item Value: ${avg_item_value:.2f}")
        summary_lines.append("")
    summary_lines.append("")
    
    # Write to text file
    output_file = "inventory_summary.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary_lines))
    
    print(f"Summary written to {output_file}")


if __name__ == "__main__":
    df = pd.read_csv(CSV_FILE_PATH)
    df["Inventory item value"] = df.apply(getInventoryItemValue, axis=1)
    writeSummary(df)
