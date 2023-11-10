USE swidnica;

CREATE TABLE `Users`(
	`uuid` UUID NOT NULL COMMENT 'Auto-generated Unique User ID' DEFAULT UUID(),
	email VARCHAR(80) NOT NULL COMMENT 'User''s e-mail address',
	`passwordHash` VARCHAR(255) NOT NULL COMMENT 'Hash of user''s password',
	`phoneNumber` VARCHAR(20) COMMENT 'User''s phone number',
	`name` VARCHAR(40) COMMENT 'User''s name',
	surname VARCHAR(60) COMMENT 'User''s surname',
	PRIMARY KEY(`uuid`)
) COMMENT 'Users'' personal data' ENGINE = InnoDB;

CREATE TABLE `Reports`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_userUUID` UUID NOT NULL,
	address VARCHAR(255) NOT NULL COMMENT 'Address',
	`dateOfBirth` DATE NOT NULL COMMENT 'User''s'' date of birth',
	PRIMARY KEY(id)
) COMMENT 'Users'' CVs';

CREATE TABLE `UsersSkills`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_reportId` INT UNSIGNED NOT NULL,
	`FK_skillId` INT UNSIGNED NOT NULL,
	PRIMARY KEY(id)
) COMMENT 'Users'' skills';

CREATE TABLE `UsersExperience`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_jobFormId` INT UNSIGNED NOT NULL,
	`FK_reportId` INT UNSIGNED NOT NULL,
	`companyName` VARCHAR(80) NOT NULL COMMENT 'Company''s name',
	`position` VARCHAR(80) NOT NULL COMMENT 'Job position',
	lokalization VARCHAR(255),
	`isCurrent` BOOLEAN NOT NULL COMMENT 'is employee still working there',
	`beginDate` DATE NOT NULL COMMENT 'Work''s date of beginning',
	`endDate` DATE COMMENT 'Work''s date of end',
	PRIMARY KEY(id)
) COMMENT 'Users'' experience';

CREATE TABLE `UsersEducation`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_reportId` INT UNSIGNED NOT NULL,
	`level`
		ENUM
			('primary', 'secondary', 'higher', 'bachelor', 'master', 'doctorate', 'vocational', 'continuing')
		NOT NULL COMMENT 'Education level',
	school VARCHAR(255) NOT NULL COMMENT 'Finished school name',
	specialization VARCHAR(80) COMMENT 'Specialization',
	`isCurrent` BOOLEAN NOT NULL COMMENT 'is user still studying there',
	`beginDate` DATE NOT NULL COMMENT 'Education''s date of beginning',
	`endDate` DATE COMMENT 'Education''s date of end',
	PRIMARY KEY(id)
) COMMENT 'Users'' education';

CREATE TABLE `Courses`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_companyNip` VARCHAR(13) NOT NULL,
	`name` VARCHAR(255) NOT NULL COMMENT 'Course''s name',
	places INT NOT NULL COMMENT 'Available places',
	`isOnline` BOOLEAN NOT NULL COMMENT 'is it course online',
	PRIMARY KEY(id)
) COMMENT 'Courses organized and hosted by companies';

CREATE TABLE `Skills`(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(100) NOT NULL COMMENT 'Skill''s name', PRIMARY KEY(id)
) COMMENT 'Possible skills';

CREATE TABLE `SkillsToLearn`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_courseId` INT UNSIGNED NOT NULL,
	`FK_skillId` INT UNSIGNED NOT NULL,
	PRIMARY KEY(id)
) COMMENT 'Skills to learn after the course completion';

CREATE TABLE `CourseParticipants`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_courseId` INT UNSIGNED NOT NULL,
	`FK_userUUID` UUID NOT NULL,
	PRIMARY KEY(id)
) COMMENT 'Course participats';

CREATE TABLE `JobApplicants`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_jobOfferId` INT UNSIGNED NOT NULL,
	`FK_userUUID` UUID NOT NULL,
	PRIMARY KEY(id)
) COMMENT 'Job applicants';

CREATE TABLE `JobOffers`(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`FK_jobFormId` INT UNSIGNED NOT NULL,
	`FK_companyNip` VARCHAR(13) NOT NULL,
	`name` VARCHAR(255) NOT NULL COMMENT 'Job''s name',
	`isOnline` BOOLEAN NOT NULL COMMENT 'is it remote job',
	PRIMARY KEY(id)
) COMMENT 'Companies'' job offers' ENGINE = InnoDB;

CREATE TABLE `Companies`(
	nip VARCHAR(13) NOT NULL COMMENT 'Company''s NIP number',
	`FK_categoryId` INT UNSIGNED,
	`name` VARCHAR(80) NOT NULL COMMENT 'Company''s name',
	email VARCHAR(80) NOT NULL COMMENT 'Company''s e-mail address',
	`passwordHash` VARCHAR(255) NOT NULL COMMENT 'Hash of company''s password',
	`phoneNumber` VARCHAR(20) COMMENT 'Company''s phone number',
	PRIMARY KEY(nip)
) COMMENT 'Companies'' data';

CREATE TABLE `CategoriesOfCompany`(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(40) NOT NULL COMMENT 'Company''s category', PRIMARY KEY(id)
) COMMENT 'Possible companies'' categories';

CREATE TABLE `JobForms`(
id INT UNSIGNED NOT NULL AUTO_INCREMENT, `name` VARCHAR(30) NOT NULL,
	PRIMARY KEY(id)
) COMMENT 'Job forms';

ALTER TABLE `Reports`
	ADD CONSTRAINT `FK_userUUID`
		FOREIGN KEY (`FK_userUUID`) REFERENCES `Users` (`uuid`) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `UsersSkills`
	ADD CONSTRAINT `id3_FK_reportID`
		FOREIGN KEY (`FK_reportId`) REFERENCES `Reports` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `UsersExperience`
	ADD CONSTRAINT `id1_FK_reportId`
		FOREIGN KEY (`FK_reportId`) REFERENCES `Reports` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `UsersEducation`
	ADD CONSTRAINT `id2_FK_reportId`
		FOREIGN KEY (`FK_reportId`) REFERENCES `Reports` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `UsersSkills`
	ADD CONSTRAINT `id1_FK_skillId`
		FOREIGN KEY (`FK_skillId`) REFERENCES `Skills` (id) ON DELETE Restrict
			ON UPDATE Cascade;

ALTER TABLE `SkillsToLearn`
	ADD CONSTRAINT `id2_FK_skillId`
		FOREIGN KEY (`FK_skillId`) REFERENCES `Skills` (id) ON DELETE Restrict
			ON UPDATE Cascade;

ALTER TABLE `SkillsToLearn`
	ADD CONSTRAINT `id2_FK_courseId`
		FOREIGN KEY (`FK_courseId`) REFERENCES `Courses` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `CourseParticipants`
	ADD CONSTRAINT `uuid2_FK_userUUID`
		FOREIGN KEY (`FK_userUUID`) REFERENCES `Users` (`uuid`) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `CourseParticipants`
	ADD CONSTRAINT `id1_FK_courseId`
		FOREIGN KEY (`FK_courseId`) REFERENCES `Courses` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `JobApplicants`
	ADD CONSTRAINT `uuid1_FK_userUUID`
		FOREIGN KEY (`FK_userUUID`) REFERENCES `Users` (`uuid`) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `JobApplicants`
	ADD CONSTRAINT `id1_FK_jobOfferId`
		FOREIGN KEY (`FK_jobOfferId`) REFERENCES `JobOffers` (id) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `JobOffers`
	ADD CONSTRAINT `nip1_FK_companyNip`
		FOREIGN KEY (`FK_companyNip`) REFERENCES `Companies` (nip) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `Courses`
	ADD CONSTRAINT `nip2_FK_companyNip`
		FOREIGN KEY (`FK_companyNip`) REFERENCES `Companies` (nip) ON DELETE Cascade
			ON UPDATE Cascade;

ALTER TABLE `Companies`
	ADD CONSTRAINT `id_FK_categoryId`
		FOREIGN KEY (`FK_categoryId`) REFERENCES `CategoriesOfCompany` (id)
			ON DELETE Restrict ON UPDATE Cascade;

ALTER TABLE `UsersExperience`
	ADD CONSTRAINT form
		FOREIGN KEY (`FK_jobFormId`) REFERENCES `JobForms` (id) ON DELETE No action
			ON UPDATE Cascade;

ALTER TABLE `JobOffers`
	ADD CONSTRAINT `FK_jobFormId`
		FOREIGN KEY (`FK_jobFormId`) REFERENCES `JobForms` (id) ON DELETE Restrict
			ON UPDATE Cascade;



CREATE USER 'exampleuser'@'%';
SET PASSWORD FOR 'exampleuser'@'%' = PASSWORD('my_cool_secret');	
grant all privileges on *.* to 'exampleuser'@'%';