CREATE USER 'Your_Database_User'@'localhost' IDENTIFIED BY 'Your_Database_Password';

CREATE DATABASE redis_cache;

GRANT ALL PRIVILEGES ON redis_cache.* TO 'Your_Database_User'@'localhost';

USE redis_cache;

CREATE TABLE products (
	product_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(50),
	retail_price  DOUBLE
);

INSERT INTO products (product_name, retail_price) VALUES ('PORTABLE MINI PROJECTOR', 90);
INSERT INTO products (product_name, retail_price) VALUES ('BLUETOOTH SPEAKER', 23.5);
INSERT INTO products (product_name, retail_price) VALUES ('NAIL POLISH', 5.29);
INSERT INTO products (product_name, retail_price) VALUES ('KIDS TABLET', 60);
INSERT INTO products (product_name, retail_price) VALUES ('THERMOS CUP', 4.89);