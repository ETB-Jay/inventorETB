import pandas as pd
from tqdm import tqdm
from config import CSV_FILE_PATH, RANGES, OUTPUT_PATH


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


def applyFilters(df: pd.DataFrame, range_config: dict) -> pd.DataFrame:
    """applyFilters applies all filters to the dataframe based on range configuration

    Args:
        df (pd.DataFrame): The dataframe to filter
        range_config (dict): The range configuration containing min, max, collection, and variant_ids

    Returns:
        pd.DataFrame: The filtered dataframe
    """
    filtered_df = df.copy()

    # 1. Filter out zero inventory items
    filtered_df = filtered_df[filtered_df["Ending inventory units"] > 0]

    # 2. Filter by min/max values
    min_val = range_config.get("min")
    max_val = range_config.get("max")

    if min_val is not None:
        filtered_df = filtered_df[filtered_df["Inventory item value"] >= min_val]
    if max_val is not None:
        filtered_df = filtered_df[filtered_df["Inventory item value"] <= max_val]

    # 3. Filter by collection names
    collections = range_config.get("collection", [])
    if collections:
        # Check if any of the product's collections contain the filter collection strings
        filtered_df = filtered_df[
            filtered_df["Product collection"].apply(
                lambda x: any(
                    any(filter_col in str(prod_col) for prod_col in x)
                    for filter_col in collections
                )
            )
        ]
    # If collections is empty or not specified, include all collections (no filtering)

    # 4. Filter by variant IDs (if specified)
    variant_ids = range_config.get("variant_ids", [])
    if variant_ids:
        # Check if the variant ID starts with any of the strings in variant_ids
        filtered_df = filtered_df[
            filtered_df["Product variant ID"]
            .astype(str)
            .apply(lambda x: any(x.startswith(str(vid)) for vid in variant_ids))
        ]

    return filtered_df


def groupDuplicateProducts(df: pd.DataFrame) -> pd.DataFrame:
    """groupDuplicateProducts groups duplicate products together and combines their collections into a list

    Args:
        df (pd.DataFrame): The original dataset with duplicate products

    Returns:
        pd.DataFrame: The dataset with grouped products and list of collections
    """
    # Group by product title, variant ID, and variant title
    grouped = (
        df.groupby(["Product title", "Product variant ID", "Product variant title"])
        .agg(
            {
                "Ending inventory units": "first",
                "Ending inventory retail value": "first",
                "Product collection": lambda x: list(x.unique()),
            }
        )
        .reset_index()
    )

    # Calculate inventory item value for the grouped data
    grouped["Inventory item value"] = grouped.apply(getInventoryItemValue, axis=1)

    return grouped


def processInventoryData(df: pd.DataFrame) -> None:
    """processInventoryData processes the inventory data and generates both summary and filtered CSV files

    Args:
        df (pd.DataFrame): The dataset
    """
    # 5. Group duplicate products first
    df_grouped = groupDuplicateProducts(df)
    df_grouped.dropna(inplace=True)

    # Drop items with zero inventory units
    print("Dropping items with zero inventory units...")
    initial_count = len(df_grouped)
    df_grouped = df_grouped[df_grouped["Ending inventory units"] > 0]
    print(f"Dropped {initial_count - len(df_grouped)} items with zero inventory units")
    print(f"Remaining items: {len(df_grouped)}")

    # Create summary statistics
    summary_lines = []
    summary_lines.append("CSV INVENTORY SUMMARY REPORT")
    summary_lines.append("=" * 50)
    summary_lines.append("")

    # Basic DataFrame info
    summary_lines.append("📊 | BASIC INVENTORY STATISTICS")
    summary_lines.append("-" * 30)
    summary_lines.append(f"Total number of unique products: {len(df_grouped)}")
    summary_lines.append(f"Original number of entries: {len(df)}")
    summary_lines.append(
        f"Total ending inventory units: {df_grouped['Ending inventory units'].sum():,.0f}"
    )
    summary_lines.append(
        f"Total ending inventory retail value: ${df_grouped['Ending inventory retail value'].sum():,.2f}"
    )
    summary_lines.append("")

    # Products with zero inventory (should be 0 after filtering)
    summary_lines.append("⚠️ | ZERO INVENTORY PRODUCTS")
    summary_lines.append("-" * 30)
    zero_inventory = df_grouped[df_grouped["Ending inventory units"] == 0]
    summary_lines.append(
        f"Products with zero inventory: {len(zero_inventory)} (filtered out)"
    )
    summary_lines.append("")

    # Process each range in a single loop
    summary_lines.append("📈 | INVENTORY VALUE RANGES")
    summary_lines.append("-" * 30)

    for i, range_config in enumerate(tqdm(RANGES)):
        print(f"Processing range {i + 1} of {len(RANGES)}")
        min_val = range_config.get("min", None)
        max_val = range_config.get("max", None)
        collections = range_config.get("collection", [])
        variant_ids = range_config.get("variant_ids", [])

        # Apply all filters efficiently
        df_filtered = applyFilters(df_grouped, range_config)

        # Calculate statistics for summary
        total_units = df_filtered["Ending inventory units"].sum()
        total_value = df_filtered["Ending inventory retail value"].sum()
        avg_item_value = (
            df_filtered["Inventory item value"].mean() if len(df_filtered) > 0 else 0
        )
        num_products = len(df_filtered)

        # Add to summary
        name = range_config.get("name", "Unnamed Range")
        collection_str = ", ".join(collections) if collections else "All Collections"
        variant_str = f" | Variant IDs: {len(variant_ids)}" if variant_ids else ""
        summary_lines.append(f"📦 {name}")
        summary_lines.append(
            f"  Range: {min_val} - {max_val} | Collections: {collection_str}{variant_str}"
        )
        summary_lines.append(f"  • Total Units: {total_units:,}")
        summary_lines.append(f"  • Total Value: ${total_value:,.2f}")
        summary_lines.append(f"  • Number of Products: {num_products}")
        summary_lines.append(f"  • Average Item Value: ${avg_item_value:.2f}")
        summary_lines.append("")

        # Save filtered CSV for this range
        collection_str = (
            "_".join([str(c).replace(" ", "-") for c in collections])
            if collections
            else "collectionAll"
        )
        min_str = f"min{min_val}" if min_val is not None else "minNone"
        max_str = f"max{max_val}" if max_val is not None else "maxNone"
        output_file = (
            f"{OUTPUT_PATH}/filtered_{min_str}_{max_str}_{collection_str}_{name}.csv"
        )
        df_filtered.to_csv(output_file, index=False)
        print(f"Filtered inventory saved to {output_file}")

    # Save the grouped data as well
    grouped_output_file = f"{OUTPUT_PATH}/grouped_inventory.csv"
    df_grouped.to_csv(grouped_output_file, index=False)
    print(f"Grouped inventory saved to {grouped_output_file}")

    # Write summary to text file
    output_file = f"{OUTPUT_PATH}/inventory_summary.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(f"Summary written to {output_file}")


if __name__ == "__main__":
    df = pd.read_csv(CSV_FILE_PATH)
    processInventoryData(df)
