"""
CSV_FILE_PATH: str

Absolute path to the inventory totals CSV file containing summarized inventory data.
To set correctly:
    - Copy the relative/absolute path by right-clicking the file and selecting "Copy Path".
    - Prefix the path with 'r' (MANDATORY).

Example: CSV_FILE_PATH = r"C:\\Users\\username\\Desktop\\inventorETB\\inventory-totals.csv"
"""
CSV_FILE_PATH: str = r"C:\Users\kalem\OneDrive\Desktop\ETB\inventorETB\inventory-totals.csv"

"""
OUTPUT_PATH: str

Absolute/relative path to the output path. 
"""
OUTPUT_PATH: str = r"data/"

"""
RANGES: list[dict]

Configuration for the ranges to print in the TXT file.
Each range is a dictionary with 'min', 'max', and 'collection' keys.

- 'min' is the minimum value of the range.
- 'max' is the maximum value of the range.
- 'collection' is the collection to print in the TXT file. 
    These should be directly copied from the CSV/Shopify. 
    The collection filter is inclusive. So if the collection name is "MTG Singles -- All Products" and the filter is "MTG Singles", 
    it will print all products in the MTG Singles - All Products collection.
    If you want to print all collections, leave the collection list empty.
- variant_ids is a list of variant IDs to print in the TXT file. These should be directly copied from the CSV/Shopify.

The Shipping, MTG Packs, Comics, Drinks, and Chocolate ranges are hardcoded in since they do not have a collection name. 
If any new/similar products are added. Include them in a similar fashion.

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
RANGES = [
    # ==== MTG Singles ====
    {"name": "MTG Singles - Under and Including $0.50", "max": 0.5, "collection": ["MTG Singles"]},
    {"name": "MTG Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["MTG Singles"]},
    {"name": "MTG Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["MTG Singles"]},
    {"name": "MTG Singles - Over $10.00", "min": 10, "collection": ["MTG Singles"]},
    # ==== Pokemon Singles ====
    {"name": "Pokémon Singles - Under and Including $0.50", "max": 0.5, "collection": ["Pokémon Singles"]},
    {"name": "Pokémon Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["Pokémon Singles"]},
    {"name": "Pokémon Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["Pokémon Singles"]},
    {"name": "Pokémon Singles - Over $10.00", "min": 10, "collection": ["Pokémon Singles"]},
    # ==== YuGiOh Singles ====
    {"name": "Yugioh Singles - Under and Including $0.50", "max": 0.5, "collection": ["Yugioh Singles"]},
    {"name": "Yugioh Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["Yugioh Singles"]},
    {"name": "Yugioh Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["Yugioh Singles"]},
    {"name": "Yugioh Singles - Over $10.00", "min": 10, "collection": ["Yugioh Singles"]},
    # ==== One Piece ====
    {"name": "One Piece Singles - Under and Including $0.50", "max": 0.5, "collection": ["One Piece Singles"]},
    {"name": "One Piece Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["One Piece Singles"]},
    {"name": "One Piece Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["One Piece Singles"]},
    {"name": "One Piece Singles - Over $10.00", "min": 10, "collection": ["One Piece Singles"]},
    # ==== Lorcana Singles ====
    {"name": "Lorcana Singles - Under and Including $0.50", "max": 0.5, "collection": ["Lorcana Singles"]},
    {"name": "Lorcana Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["Lorcana Singles"]},
    {"name": "Lorcana Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["Lorcana Singles"]},
    {"name": "Lorcana Singles - Over $10.00", "min": 10, "collection": ["Lorcana Singles"]},
    # === Sorcery ===
    {"name": "Sorcery Singles - Under and Including $0.50", "max": 0.5, "collection": ["Sorcery Singles"]},
    {"name": "Sorcery Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["Sorcery Singles"]},
    {"name": "Sorcery Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["Sorcery Singles"]},
    {"name": "Sorcery Singles - Over $10.00", "min": 10, "collection": ["Sorcery Singles"]},
    # === Flesh and Blood
    {"name": "Flesh and Blood Singles - Under and Including $0.50", "max": 0.5, "collection": ["Flesh and Blood Singles"]},
    {"name": "Flesh and Blood Singles - $0.51 to $3.00", "min": 0.51, "max": 2.99, "collection": ["Flesh and Blood Singles"]},
    {"name": "Flesh and Blood Singles - $3.01 to $10.00", "min": 3, "max": 9.99, "collection": ["Flesh and Blood Singles"]},
    {"name": "Flesh and Blood Singles - Over $10.00", "min": 10, "collection": ["Flesh and Blood Singles"]},
    # ==== Shipping ====
    {"name": "Shipping Products", "variant_ids": [42277454676139, 45167013494955, 42172855943339, 45250620489899, 44728401166507, 43398104285355, 45341396631723, 43014307053739]},
    # ==== MTG Packs ====
    {"name": "MTG Packs", "variant_ids": [42242026209451, 42038207053995, 44400988782763, 43901919232171]},
    # ==== Comics ====
    {"name": "Comics", "variant_ids": [43449742524587, 43449744359595, 43449747079339, 43449748160683, 43449751863467, 43449754058923, 43449756909739, 43449759760555]},
    # ==== Drinks ====
    {"name": "Drinks", "variant_ids": [36574139908257, 36573745021089, 36573812687009, 36573763043489, 36573626695841]},
    # ==== Chocolate ====
    {"name": "Chocolate", "variant_ids": [45034427777195, 45034422763691, 45034560061611, 45034436034731, 45034435412139, 45034515693739, 45034516873387, 45034517069995, 45034435838123, 45034418503851, 45034432954539]},
]