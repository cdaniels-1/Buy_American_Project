-- script for recreating products and spending rows tables
CREATE TABLE IF NOT EXISTS products (
	product_id INTEGER PRIMARY KEY,
	brand TEXT,
	item_description TEXT,
	country_of_origin TEXT,
	domestic_status	TEXT,
	has_multiple_countries INTEGER,
	is_a_la_carte INTEGER DEFAULT 0,
	exception_cheaper INTEGER,
	exception_non_domestic INTEGER,
	manual_override_status TEXT,
	last_updated TEXT,
	notes TEXT
);

CREATE TABLE IF NOT EXISTS spending_rows
(
	row_id INTEGER PRIMARY KEY,
	product_id INTEGER,
	customer_name TEXT,
	customer_id INTEGER,
	obligation_number INTEGER,
	obligation_date TEXT,
	quantity REAL,
	net_sales_ext REAL,
	notes TEXT,
	FOREIGN KEY (product_id) references products(product_id)
);