1. What did you learn about Django models?

I learned how to create models in Django and store data in the database. I created separate models for products, orders and boxes. I also learned how to use Django ORM to add, update and get data without writing SQL queries every time.

2. How did you connect products with orders?

I connected products and orders using Django model relationships. One order can have multiple products, so I used a Many-to-Many relationship. This made it easier to get all the products related to a particular order.

3. How did you calculate product dimensions and weight?

I took the length, width, height and weight of each product. I checked the dimensions against the available box dimensions and added the weights of all products in an order. Then I compared the total weight with the box's weight capacity.

4. How did you implement the box recommendation logic?

First, I got all the products in an order. Then I checked which boxes could handle the total weight and product dimensions. I removed the boxes that didn't meet the requirements. From the remaining boxes, I selected the one with the lowest cost.

5. What errors did you encounter?

Initially, I faced some errors with database migrations and model relationships. I also had some issues with the box selection logic because getting the correct dimensions and weight was a little confusing at first.

6. How did you debug them?

Whenever I got an error, I checked the terminal message first. Then I went to the related file and checked the code. I used print statements to understand the values and find where things were going wrong. After fixing the issue, I ran the application again.

7. How did you test your application?

I tested it with different products and different box sizes. I checked whether the application selected the correct box, whether it handled weight limits properly and what happened when no box was suitable. I also checked the main features manually.

8. What would you improve in the next version?

I would like to improve the frontend and make it easier to use. I would also add more test cases, improve the box selection logic and add features like order history and better error messages.