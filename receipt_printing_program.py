# Company details
company_name = "Tech Store"
company_address_1 = "123 Tech Ave"
company_address_2 = "Innovation City"

# Product details
product_name_1 = "Books"
product_price_1 = 49.95
product_name_2 = "Computer"
product_price_2 = 579.99
product_name_3 = "Monitor"
product_price_3 = 124.89

# Total calculation
total_price = product_price_1 + product_price_2 + product_price_3

# Formatting the receipt with empty lines
# The .2f formatting specification for 2 decimal in price

receipt = f"""
{'*' * 40}
\n
\t\t\t{company_name}
\t\t\t{company_address_1}
\t\t\t{company_address_2}
\n
{'-' * 40}
Product Name \t\t Product Price
{product_name_1.ljust(20)} ${product_price_1:.2f}
{product_name_2.ljust(20)} ${product_price_2:.2f}
{product_name_3.ljust(20)} ${product_price_3:.2f}
{'-' * 40}
{'-' * 40}
\t\t\t\t\t Total
\t\t\t\t\t ${total_price:.2f}
{'-' * 40}
{'-' * 40}
\n
Thank you for shopping with us today!
\n
{'*' * 40}
"""

# Print the receipt
print(receipt)