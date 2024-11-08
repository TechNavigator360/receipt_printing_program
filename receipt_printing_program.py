# This is a school assignment

# Definitions

# Company details
company_name = "Coding Temple, Inc."
company_address_1 = "283 Franklin St."
company_address_2 = "Boston, MA"

# Product details
product_name_1 = "Books"
product_price_1 = 49.95
product_name_2 = "Computer"
product_price_2 = 579.99
product_name_3 = "Monitor"
product_price_3 = 124.89

# Total calculation
total_price = product_price_1 + product_price_2 + product_price_3

# Define widths for columns
line_length = 40 # Number of characters in one line
header_tab_space = 8 # Number of spaces that simulate tabs for header alignment
product_column_width = 20
price_column_width = 20


# Formatting the receipt
# The .2f formatting specification for 2 decimal in price

receipt = f"""
{'*' * line_length}
\n
{" " * header_tab_space}{company_name}
{" " * header_tab_space}{company_address_1}
{" " * header_tab_space}{company_address_2}
\n
{'_' * line_length}
{'_' * line_length}
{"Product Name".ljust(product_column_width)} Product Price
{product_name_1.ljust(product_column_width)} ${product_price_1:.2f}
{product_name_2.ljust(product_column_width)} ${product_price_2:.2f}
{product_name_3.ljust(product_column_width)} ${product_price_3:.2f}
{'_' * line_length}
{'_' * line_length}
{' ' * price_column_width} Total
{' ' * price_column_width} ${total_price:.2f}
{'_' * line_length}
{'_' * line_length}
\n
{"Thank you for shopping with us today!".center(line_length)}
\n
{'*' * line_length}
"""

print("nick is cool")

# Print the receipt
print(receipt)