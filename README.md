# 🗄️ | inventorETB
**inventorETB** is a Shopify inventory compiler that compiles the current value of the inventory using different metrics. 

# 🚀 | Usage

### Make sure you have the following installed:
- [VS Code](https://code.visualstudio.com/Download)
- [Python](https://www.python.org/downloads/)

### Setup

1. Clone the repository. Make sure to replace `your-username` with your Github username or copy the directory from the Github repository page.

```bash
git clone https://github.com/your-username/inventorETB.git
cd inventorETB
```

<img width="1278" height="477" alt="image" src="https://github.com/user-attachments/assets/acef6061-6b53-49ee-85ee-925a0ecb71a4" />


2. Create and activate a virtual environment (venv) using the terminal. The terminal can be opened using the header or ``Ctrl + Shift + ` ``.
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv/Scripts/activate      # Windows
```

3. Install dependencies. Check that your current path is the same as where requirements.txt and all of the other files are located.
```bash
pip install -r requirements.txt
```

### Exporting Data from Shopify

4. Copy the following ShopifyQL query into the ShopifyQL Editor. The same code can be found under the `inventory-totals` in **Reports**
```sql
FROM inventory
  SHOW ending_inventory_units, ending_inventory_retail_value
  GROUP BY product_title, product_variant_id, product_variant_title WITH TOTALS,
    GROUP_TOTALS, CURRENCY 'CAD'
  DURING today
  ORDER BY ending_inventory_units__product_title_totals DESC,
    ending_inventory_units__product_title_product_variant_id_totals DESC,
    ending_inventory_units DESC, product_title ASC, product_variant_id ASC,
    product_variant_title ASC
  LIMIT 1000
```

5. Download the results as a CSV file.
<img width="1640" height="445" alt="image" src="https://github.com/user-attachments/assets/ce1ec009-d1ac-48eb-bf8c-aea283b9b614" />

### Running inventorETB

6. Place the downloaded CSV in the project’s folder (or wherever specified in `config.py`).

7. Configurate `config.py` to match the information that you need. 

8. Run the processing script. This could take a while depending on the size of the data:
```bash
python processQL.py
```

# 🛠️ | Project Structure
```
inventorETB/
│── processQL.py       # Main processing script
│── config.py          # Configurations for processQL.py
│── requirements.txt   # Project Dependencies
│── README.md          # Documentation
```


# 🤝 | Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add or change.

# 📄 | License
This project is licensed under the MIT License – see the LICENSE file for details.
