# Write a solution to find the ids of products that are both low fat and recyclable.

CREATE TABLE Products (
  product_id int,
  low_fats enum('Y','N'),
  recyclable enum('Y','N')
);

SELECT product_id FROM Products
WHERE low_fats='Y' and recyclable='Y';