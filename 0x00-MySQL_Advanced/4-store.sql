-- Task4. Buy buy buy
-- creates a trigger that decreases
-- the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
