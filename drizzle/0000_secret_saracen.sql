CREATE TABLE `documents` (
	`id` text PRIMARY KEY NOT NULL,
	`request_id` text NOT NULL,
	`object_key` text NOT NULL,
	`name` text NOT NULL,
	`type` text NOT NULL,
	`size` integer NOT NULL,
	`created_at` text NOT NULL,
	FOREIGN KEY (`request_id`) REFERENCES `requests`(`id`) ON UPDATE no action ON DELETE no action
);
--> statement-breakpoint
CREATE INDEX `documents_request` ON `documents` (`request_id`);--> statement-breakpoint
CREATE TABLE `requests` (
	`id` text PRIMARY KEY NOT NULL,
	`reference` text NOT NULL,
	`owner` text NOT NULL,
	`request_key` text NOT NULL,
	`kind` text NOT NULL,
	`guardian` text NOT NULL,
	`email` text NOT NULL,
	`phone` text NOT NULL,
	`child` text NOT NULL,
	`dob` text NOT NULL,
	`program` text NOT NULL,
	`campus` text NOT NULL,
	`preferred_date` text NOT NULL,
	`preferred_time` text NOT NULL,
	`notes` text NOT NULL,
	`consent` text NOT NULL,
	`status` text DEFAULT 'pending' NOT NULL,
	`created_at` text NOT NULL,
	`updated_at` text NOT NULL,
	`version` integer DEFAULT 1 NOT NULL
);
--> statement-breakpoint
CREATE UNIQUE INDEX `requests_reference_unique` ON `requests` (`reference`);--> statement-breakpoint
CREATE UNIQUE INDEX `request_idempotency` ON `requests` (`owner`,`request_key`);--> statement-breakpoint
CREATE INDEX `requests_owner` ON `requests` (`owner`);--> statement-breakpoint
CREATE INDEX `requests_created` ON `requests` (`created_at`);