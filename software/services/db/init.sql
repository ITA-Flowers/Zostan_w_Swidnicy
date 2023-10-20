USE swidnica;

CREATE TABLE User (

    Email VARCHAR(25) PRIMARY KEY,
    Password VARCHAR(20),
    PhoneNumber VARCHAR(9)
	
);

CREATE TABLE Company (

    Name VARCHAR(40) PRIMARY KEY,
    Email VARCHAR(25),
    NIP VARCHAR(16),
    Password VARCHAR(20),
    PhoneNumber VARCHAR(9)
	
);

CREATE TABLE Courses (
    Id int PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(20),
    CompanyName VARCHAR(40),
    Spaces INT,
    Place VARCHAR(20),
    FOREIGN KEY (CompanyName) REFERENCES Company(Name)
	
);

CREATE TABLE JobOffers (
    Id int PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(20),
    CompanyName VARCHAR(40),
    Description VARCHAR(200),
    Place VARCHAR(20),
    FOREIGN KEY (CompanyName) REFERENCES Company(Name)
	
);

CREATE TABLE CV (
    Id int PRIMARY KEY,
    UserEmail VARCHAR(25),
    Adress VARCHAR(30),
    DateOfBirth DATE,
    Name VARCHAR(15),
    Surame VARCHAR(20),
    FOREIGN KEY (UserEmail) REFERENCES User(Email)
	
);

CREATE TABLE Skills (
    CVId int,
    UserEmail VARCHAR(25),
    Skill VARCHAR(20),
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE Education (
    CVId int,
    UserEmail VARCHAR(25),
    School VARCHAR(40),
    Begin DATE,
    End DATE,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE Experience (
    CVId int,
    UserEmail VARCHAR(25),
    Company VARCHAR(40),
    Begin DATE,
    End DATE,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE CourseAplicants (
    UserEmail VARCHAR(25),
    CourseId int,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CourseId) REFERENCES Courses(Id)
);

CREATE TABLE SkillsToLearn (
    CourseId int,
    Skill VARCHAR(20),
	FOREIGN KEY (CourseId) REFERENCES Courses(Id)
);

CREATE TABLE JobAplicants (
    UserEmail VARCHAR(25),
    JobOfferId int,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (JobOfferId) REFERENCES JobOffers(Id)
);

CREATE USER 'exampleuser'@'%';
SET PASSWORD FOR 'exampleuser'@'%' = PASSWORD('my_cool_secret');	
grant all privileges on *.* to 'exampleuser'@'%';