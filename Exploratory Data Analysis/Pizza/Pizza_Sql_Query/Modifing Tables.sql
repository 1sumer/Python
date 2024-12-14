create database pizza;

use pizza;

select * from order_details;

desc pizzas;

-- Add Primary Keys
ALTER TABLE order_details MODIFY order_details_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE orders ADD PRIMARY KEY (order_id);

-- Change data types to VARCHAR for columns used as keys
ALTER TABLE pizza_types MODIFY pizza_type_id VARCHAR(50);
ALTER TABLE pizzas MODIFY pizza_id VARCHAR(50);
ALTER TABLE pizzas MODIFY pizza_type_id VARCHAR(50);
ALTER TABLE order_details MODIFY pizza_id VARCHAR(50);


ALTER TABLE pizza_types ADD PRIMARY KEY (pizza_type_id);
ALTER TABLE pizzas ADD PRIMARY KEY (pizza_id);

-- Add Foreign Keys
ALTER TABLE order_details 
    ADD CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(order_id),
    ADD CONSTRAINT fk_pizza FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id);

ALTER TABLE pizzas 
    ADD CONSTRAINT fk_pizza_type FOREIGN KEY (pizza_type_id) REFERENCES pizza_types(pizza_type_id);


