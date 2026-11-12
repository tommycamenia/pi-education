CREATE TABLE `chat_messages` (
	`id` text PRIMARY KEY NOT NULL,
	`owner` text NOT NULL,
	`request_key` text NOT NULL,
	`role` text NOT NULL,
	`name` text NOT NULL,
	`email` text NOT NULL,
	`phone` text NOT NULL,
	`body` text NOT NULL,
	`created_at` text NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `chat_idempotency` ON `chat_messages` (`owner`,`request_key`);--> statement-breakpoint
CREATE INDEX `chat_owner_created` ON `chat_messages` (`owner`,`created_at`);--> statement-breakpoint
ALTER TABLE `requests` ADD `nickname` text DEFAULT '' NOT NULL;