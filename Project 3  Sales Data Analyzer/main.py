import numpy as np

# sales data: products × regions × months
sales = np.array([
    [[200, 220, 250], [180, 190, 210]],
    [[150, 160, 170], [140, 150, 160]],
    [[300, 320, 330], [280, 290, 310]]
])

total_sales = np.sum(sales)
print("Total Sales:", total_sales)
