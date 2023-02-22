-- Create Table whose default id = 1 and is UNIQE
CREATE TABLE IF NOT EXISTS `uniqe_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
	);
