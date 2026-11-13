1. What did you learn about Django models?

I learned how Django models are used to store and manage application data. In this project, I worked with models for products, orders and boxes. I also learned how Django ORM makes it easier to perform database operations without writing SQL queries for everything.

2. How did you connect products with orders?

I used an OrderItem model to connect products and orders. It has two ForeignKeys, one for the Order and another for the Product. This means one order can have multiple order items, and each item is connected to a particular product. I also used a quantity field to store how many units of a product were included in an order.

3. How did you calculate product dimensions and weight?

I used the length, width, height and weight values stored for each product. I checked the product dimensions against the available box dimensions and calculated the total weight based on the products and their quantities in the order. Then I compared that weight with the box's maximum weight capacity.

4. How did you implement the box recommendation logic?

First, I fetched the products and quantities from an order. Then I checked the available boxes based on their dimensions and weight capacity. Boxes that did not meet the requirements were excluded. From the remaining suitable boxes, I selected the one with the lowest cost.

5. What errors did you encounter?

During development, I faced some issues with database migrations and model relationships. I also needed to check the dimension and weight calculations carefully because even a small mistake could affect the box recommendation.

6. How did you debug them?

Whenever I faced an error, I first checked the terminal to understand what was causing it. Then I checked the related model, view or function. I also used print statements to check values during execution. After making changes, I ran the application again to see whether the issue was fixed.

7. How did you test your application?

I checked the application with different product details, quantities and box sizes. I focused on whether the correct box was selected, whether the weight limit was followed and what happened when no suitable box was available. I also checked the main features through the application.

8. What would you improve in the next version?

In the next version, I would like to improve the frontend and make the application easier to use. I would also add more automated test cases, improve the box recommendation logic and include features like order history and better error messages.