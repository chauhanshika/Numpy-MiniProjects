import numpy as np

sales = np.array([
    [[200, 220, 250], [180, 190, 210]],
    [[150, 160, 170], [140, 150, 160]],
    [[300, 320, 330], [280, 290, 310]]
])

total_sales = np.sum(sales)
region_sales = np.sum(sales, axis=(0,2))
product_sales = np.sum(sales, axis=(1,2))
best_product = np.argmax(product_sales)
monthly_sales = np.sum(sales, axis=(0,1))

print("\nSales Data Analysis\n")

print("Total Sales:", total_sales)
print("Sales per Region:", region_sales)
print("Sales per Product:", product_sales)
print("Best Selling Product Index:", best_product)
print("Monthly Sales:", monthly_sales)
