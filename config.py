"""
CSV_FILE_PATH: str

Absolute path to the inventory totals CSV file containing summarized inventory data.
To set correctly:
    - Copy the relative/absolute path by right-clicking the file and selecting "Copy Path".
    - Prefix the path with 'r' (MANDATORY).

Example: CSV_FILE_PATH = r"C:\\Users\\username\\Desktop\\inventorETB\\inventory-totals.csv"
"""
CSV_FILE_PATH: str = "" # HERE

"""
RANGES: list[dict]

Configuration for the ranges to print in the TXT file.
Each range is a dictionary with 'min', 'max', and 'collection' keys.

Example:
    RANGES = [
        {
            "min": 0.8,
            "max": 0.8,
            "collection": ["New Arrivals"]
        },
        {
            "min": 0.5,
            "max": 0.7,
            "collection": ["MTG Singles", "Pokemon Singles"]
        }
    ]
"""
RANGES: list = [
    {
        "min": 0.8,
        "max": 0.8,
        "collection": [
            "New Arrivals"
            
        ]
    },
] 
