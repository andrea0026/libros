CREATE TABLE `authors` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` TEXT NOT NULL,
	`created_at` DATETIME NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `books` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` TEXT NOT NULL,
	`num_of_pages` INT NOT NULL,
	`created_at` TIMESTAMP NOT NULL,
	`updated_at` TIMESTAMP NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `favorites` (
	`author_id` INT NOT NULL,
	`book_id` INT NOT NULL
);

ALTER TABLE `favorites` ADD CONSTRAINT `favorites_fk0` FOREIGN KEY (`author_id`) REFERENCES `authors`(`id`);

ALTER TABLE `favorites` ADD CONSTRAINT `favorites_fk1` FOREIGN KEY (`book_id`) REFERENCES `books`(`id`);




