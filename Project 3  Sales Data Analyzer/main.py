import numpy as np

sales = np.array([
    [[200, 220, 250], [180, 190, 210]],
    [[150, 160, 170], [140, 150, 160]],
    [[300, 320, 330], [280, 290, 310]]
])

total_sales = np.sum(sales)
region_sales = np.sum(sales, axis=(0,2))

print("Total Sales:", total_sales)
print("Sales per Region:", region_sales)
