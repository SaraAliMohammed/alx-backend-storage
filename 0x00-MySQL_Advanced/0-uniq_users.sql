-- Task0. We are all unique! - creates a table users
-- Script can be executed on any database
CREATE TABLE IF NOT EXISTS `users` (
	`id` INT NOT NULL PRIMARY KEY Auto_INCREMENT,
	`email` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255)
);
