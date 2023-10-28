USE swidnica;

CREATE TABLE User (

    Email VARCHAR(40) PRIMARY KEY,
    Password VARCHAR(20),
    PhoneNumber VARCHAR(9)
	
);

CREATE TABLE CompanyUser (
    Email VARCHAR(40) PRIMARY KEY,
    Password VARCHAR(20),
    PhoneNumber VARCHAR(9)
	
);

CREATE TABLE CategoryOfCompany (
    CategoryId INT PRIMARY KEY,
    Category VARCHAR(20)
	
);

CREATE TABLE Company (
    Name VARCHAR(40),
    CompanyUserEmail VARCHAR(40),
    NIP VARCHAR(13) PRIMARY KEY,
    CategoryId INT,
    FOREIGN KEY (CategoryId) REFERENCES CategoryOfCompany(CategoryId),
    FOREIGN KEY (CompanyUserEmail) REFERENCES CompanyUser(Email)
);

CREATE TABLE Courses (
    Id int PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(40),
    CompanyNIP VARCHAR(13),
    Spaces INT,
    Place VARCHAR(40),
    FOREIGN KEY (CompanyNIP) REFERENCES Company(NIP)
	
);

CREATE TABLE JobOffers (
    Id int PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(40),
    CompanyNIP VARCHAR(13),
    Description VARCHAR(200),
    Place VARCHAR(40),
    FOREIGN KEY (CompanyNIP) REFERENCES Company(NIP)
	
);

CREATE TABLE CV (
    Id int PRIMARY KEY,
    UserEmail VARCHAR(40),
    Adress VARCHAR(30),
    DateOfBirth DATE,
    Name VARCHAR(15),
    Surname VARCHAR(20),
    FOREIGN KEY (UserEmail) REFERENCES User(Email)
	
);

CREATE TABLE Skills (
    CVId int,
    UserEmail VARCHAR(40),
    Skill VARCHAR(40),
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE Education (
    CVId int,
    UserEmail VARCHAR(40),
    School VARCHAR(40),
    Begin DATE,
    End DATE,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE Experience (
    CVId int,
    UserEmail VARCHAR(40),
    Company VARCHAR(40),
    Begin DATE,
    End DATE,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CVId) REFERENCES CV(Id)
);

CREATE TABLE CourseAplicants (
    UserEmail VARCHAR(40),
    CourseId int,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (CourseId) REFERENCES Courses(Id)
);

CREATE TABLE SkillsToLearn (
    CourseId int,
    Skill VARCHAR(50),
	FOREIGN KEY (CourseId) REFERENCES Courses(Id)
);

CREATE TABLE JobAplicants (
    UserEmail VARCHAR(40),
    JobOfferId int,
    FOREIGN KEY (UserEmail) REFERENCES User(Email),
	FOREIGN KEY (JobOfferId) REFERENCES JobOffers(Id)
);


INSERT INTO CategoryOfCompany (CategoryId, Category)
VALUES (1,"Wędkarstwo"),(2,"Spawanie"),
    (3,"Informatyka"),(4,"Gastronomia");

INSERT INTO CompanyUser (Email, Password, PhoneNumber)
VALUES ("JacekPlacek@edu.pl","Haslo123","777666555"),("JanekTytus@edu.com","TylkoHaslo321","774616355"),
    ("emailprzykladowy@gmail.pl","Has123lo","997666500"),("Szyk.bart.ula.ek@gmail.com","HaszowaneHaslo","694206910");

INSERT INTO Company (Name, NIP, CompanyUserEmail, CategoryId)
VALUES ("WarmuzBaitzzz","111-122-22-33","JacekPlacek@edu.pl",1), ("SzybkiSpawex","222-233-33-11","JanekTytus@edu.com",2), 
    ("Może Nie Dobrze, Ale Drogo","333-311-11-55","Szyk.bart.ula.ek@gmail.com",3), ("Maharadża KEBAP","999-911-11-00","emailprzykladowy@gmail.pl",4);

INSERT INTO Courses (Id, Name, CompanyNIP, Spaces, Place)
VALUES (1,"Dobieranie Przynęty","111-122-22-33",4,"Świdnica ul.Pełczyńskiego 7"), (2,"Spawanie Podstawowe","222-233-33-11",5,"Świdnica ul.Zabłotnia 17"), 
    (3,"Java dla początkujących","333-311-11-55",2,"Świdnica ul. Piękna 17"), (4,"Kręcenie kebaba wołowego","999-911-11-00",1, "Świdnica ul.Złota 100");

INSERT INTO SkillsToLearn (CourseId, Skill)
VALUES (1,"Dobieranie Przynęt"),(2,"Spawanie podstawowych elementów stalowych"),
    (3,"Programowanie w języku JAVA"),(4,"Wykonywanie kebabów wołowych");

INSERT INTO JobOffers (Id, Name, CompanyNIP,Description,Place)
VALUES (1,"Sprzedawca","111-122-22-33","Praca w sklepie z akcesoriami wędkarskimi","Świdnica ul.Pełczyńskiego 7"),(2,"Młodszy Spawacz","222-233-33-11","Spawanie elementów stalowych","Świdnica ul.Zabłotnia 17"),
    (3,"Junior Java developer","333-311-11-55","Pisanie aplikacji w języku Java","Świdnica ul. Piękna 17"),(4,"Kucharz","999-911-11-00","Praca w budce z kebabem","Świdnica ul.Złota 100");

INSERT INTO User(Email, Password, PhoneNumber)
VALUES ("jan.kowalski@email.com","haslo123","123456789"), ("anna.nowak@email.com","tajnehaslo","987654321"), 
    ("marta.wisniewska@email.com","securepass","555666777"), ("adam.janowski@email.com", "12345678","111222333");

INSERT INTO CV(Id, UserEmail, Adress, DateOfBirth, Name, Surname)
VALUES (1, "jan.kowalski@email.com", "Świdnica ul. Kwiatowa 5", "1990-05-15", "Jan", "Kowalski"), 
    (2, "anna.nowak@email.com", "Kraków ul. Leśna 10", "1985-12-20", "Anna", "Nowak"),
    (3, "marta.wisniewska@email.com", "Świdnica ul. Słoneczna 3", "1992-07-08", "Marta", "Wiśniewska"),
    (4, "adam.janowski@email.com", "Szczecin ul. Morska 15", "1988-03-25", "Adam", "Janowski");

INSERT INTO Skills (CVId, UserEmail, Skill)
VALUES (1, "jan.kowalski@email.com", "Programowanie w języku Java"),
    (1, "jan.kowalski@email.com", "Zarządzanie projektem"),
    (2, "anna.nowak@email.com", "Angielski - zaawansowany"),
    (2, "anna.nowak@email.com", "Rozwiązywanie konfliktów"),
    (3, "marta.wisniewska@email.com", "Tworzenie stron internetowych"),
    (3, "marta.wisniewska@email.com", "Obsługa narzędzi graficznych"),
    (4, "adam.janowski@email.com", "Obsługa maszyn CNC"),
    (4, "adam.janowski@email.com", "Spawanie TIG");

INSERT INTO Education (CVId, UserEmail, School, Begin, End)
VALUES (1, "jan.kowalski@email.com", "Politechnika Warszawska", "2010-09-01", "2015-06-30"),
    (1, "jan.kowalski@email.com", "Liceum im. Adama Mickiewicza", "2006-09-01", "2010-06-30"),
    (2, "anna.nowak@email.com", "Uniwersytet Jagielloński", "2005-10-01", "2010-07-15"),
    (2, "anna.nowak@email.com", "Liceum Ogólnokształcące nr 3", "2001-09-01", "2005-06-30"),
    (3, "marta.wisniewska@email.com", "Akademia Sztuk Pięknych", "2011-10-01", "2016-07-15"),
    (3, "marta.wisniewska@email.com", "Liceum Plastyczne im. Jana Matejki", "2007-09-01", "2011-06-30"),
    (4, "adam.janowski@email.com", "Politechnika Wrocławska", "2012-10-01", "2017-07-15"),
    (4, "adam.janowski@email.com", "Technikum Mechaniczne nr 5", "2008-09-01", "2012-06-30");

INSERT INTO Experience (CVId, UserEmail,Company,Begin,End)
VALUES (1, "jan.kowalski@email.com", "Firma ABC Sp. z o.o.", "2015-07-01", "2020-12-31"),
    (2, "anna.nowak@email.com", "XYZ Corporation", "2010-06-01", "2015-06-30"),
    (3, "marta.wisniewska@email.com", "Graphic Designs Ltd.", "2016-03-15", "2019-12-31"),
    (4, "adam.janowski@email.com", "MetalTech Manufacturing", "2017-01-15", "2022-05-30");

INSERT INTO CourseAplicants (UserEmail,CourseId)
VALUES ("jan.kowalski@email.com",2), ("jan.kowalski@email.com",1), ("anna.nowak@email.com",2), ("marta.wisniewska@email.com",3),
    ("jan.kowalski@email.com",4), ("anna.nowak@email.com",4), ("marta.wisniewska@email.com",2);

INSERT INTO JobAplicants (UserEmail,JobOfferId)
VALUES ("jan.kowalski@email.com",2), ("jan.kowalski@email.com",1), ("anna.nowak@email.com",2), ("marta.wisniewska@email.com",3),
    ("jan.kowalski@email.com",4), ("anna.nowak@email.com",4), ("marta.wisniewska@email.com",2), ("adam.janowski@email.com",3);








CREATE USER 'exampleuser'@'%';
SET PASSWORD FOR 'exampleuser'@'%' = PASSWORD('my_cool_secret');	
grant all privileges on *.* to 'exampleuser'@'%';