```sql
FROM inventory
  SHOW ending_inventory_units, ending_inventory_retail_value
  WHERE product_collections CONTAINS 'MTG Singles - Instock'
  GROUP BY product_title, product_variant_id, product_variant_title WITH TOTALS,
    GROUP_TOTALS, CURRENCY 'CAD'
  DURING today
  ORDER BY ending_inventory_units__product_title_totals DESC,
    ending_inventory_units__product_title_product_variant_id_totals DESC,
    ending_inventory_units DESC, product_title ASC, product_variant_id ASC,
    product_variant_title ASC
  LIMIT 1000
```