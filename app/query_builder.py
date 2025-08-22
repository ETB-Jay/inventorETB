"""ShopifyQL Query Builder Logic"""

from typing import Dict, Any, List


class ShopifyQLQueryBuilder:
    """Builds ShopifyQL queries from form inputs"""
    
    def __init__(self):
        self.query_parts = []
    
    def build_query(self, form_data: Dict[str, Any]) -> str:
        """Build a complete ShopifyQL query from form data"""
        self.query_parts = []
        
        # Determine the main entity type
        entity_type = self._determine_entity_type(form_data)
        
        # Start query
        query = f"SHOW {entity_type}"
        
        # Add WHERE conditions
        conditions = self._build_conditions(form_data)
        if conditions:
            query += f" WHERE {' AND '.join(conditions)}"
        
        # Add date range if specified
        date_condition = self._build_date_condition(form_data)
        if date_condition:
            if conditions:
                query += f" AND {date_condition}"
            else:
                query += f" WHERE {date_condition}"
        
        # Add ordering
        query += " ORDER BY created_at DESC"
        
        # Add limit
        query += " LIMIT 100"
        
        return query
    
    def _determine_entity_type(self, form_data: Dict[str, Any]) -> str:
        """Determine the primary entity type based on filled fields"""
        if any(key in form_data for key in ['order_status', 'financial_status']):
            return "orders"
        elif any(key in form_data for key in ['customer_email', 'customer_country']):
            return "customers"
        else:
            return "products"
    
    def _build_conditions(self, form_data: Dict[str, Any]) -> List[str]:
        """Build WHERE conditions from form data"""
        conditions = []
        
        # Product conditions
        if form_data.get('product_type'):
            conditions.append(f"product_type = '{form_data['product_type']}'")
        
        if form_data.get('vendor'):
            conditions.append(f"vendor = '{form_data['vendor']}'")
        
        if form_data.get('tags'):
            tags = [tag.strip() for tag in form_data['tags'].split(',')]
            tag_conditions = [f"tags CONTAINS '{tag}'" for tag in tags if tag]
            if tag_conditions:
                conditions.append(f"({' OR '.join(tag_conditions)})")
        
        # Value range conditions
        if form_data.get('min_value') or form_data.get('max_value'):
            value_conditions = []
            if form_data.get('min_value'):
                value_conditions.append(f"total_price >= {form_data['min_value']}")
            if form_data.get('max_value'):
                value_conditions.append(f"total_price <= {form_data['max_value']}")
            conditions.extend(value_conditions)
        
        # Quantity range conditions
        if form_data.get('min_quantity') or form_data.get('max_quantity'):
            qty_conditions = []
            if form_data.get('min_quantity'):
                qty_conditions.append(f"quantity >= {form_data['min_quantity']}")
            if form_data.get('max_quantity'):
                qty_conditions.append(f"quantity <= {form_data['max_quantity']}")
            conditions.extend(qty_conditions)
        
        # Order conditions
        if form_data.get('order_status'):
            conditions.append(f"order_status = '{form_data['order_status']}'")
        
        if form_data.get('financial_status'):
            conditions.append(f"financial_status = '{form_data['financial_status']}'")
        
        # Customer conditions
        if form_data.get('customer_email'):
            conditions.append(f"customer_email = '{form_data['customer_email']}'")
        
        if form_data.get('customer_country'):
            conditions.append(f"customer_country = '{form_data['customer_country']}'")
        
        return conditions
    
    def _build_date_condition(self, form_data: Dict[str, Any]) -> str:
        """Build date range condition"""
        start_date = form_data.get('start_date')
        end_date = form_data.get('end_date')
        
        if start_date and end_date:
            return f"created_at BETWEEN '{start_date}' AND '{end_date}'"
        elif start_date:
            return f"created_at >= '{start_date}'"
        elif end_date:
            return f"created_at <= '{end_date}'"
        
        return ""
    
    def validate_date_format(self, date_str: str) -> bool:
        """Validate date format (YYYY-MM-DD)"""
        try:
            from datetime import datetime
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def get_sample_queries(self) -> Dict[str, str]:
        """Return sample ShopifyQL queries for reference"""
        return {
            "Products by Type": "SHOW products WHERE product_type = 'T-Shirt' ORDER BY created_at DESC LIMIT 50",
            "High Value Orders": "SHOW orders WHERE total_price >= 100 ORDER BY total_price DESC LIMIT 25",
            "Recent Customers": "SHOW customers WHERE created_at >= '2024-01-01' ORDER BY created_at DESC LIMIT 100",
            "Tagged Products": "SHOW products WHERE tags CONTAINS 'featured' OR tags CONTAINS 'sale' LIMIT 50"
        }
        
        