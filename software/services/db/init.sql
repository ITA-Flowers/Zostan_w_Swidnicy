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
	create table if not exists Skills
(
    id   int auto_increment comment 'Skill''s ID'
        primary key,
    name varchar(256) not null comment 'Skill''s name'
)
    comment 'Worker''s possible skills';

create table if not exists Users
(
    uuid         uuid default uuid() not null comment 'Unique User ID'
        primary key,
    password     varchar(128)        not null comment 'User''s password hash',
    email        varchar(80)         not null comment 'Users''s email',
    phone_number varchar(20)         null comment 'User''s phone number',
    is_company   tinyint(1)          not null comment 'Company type account flag',
    is_admin     tinyint(1)          not null comment 'Administrator type account flag'
)
    comment 'Users';

create table if not exists Companies
(
    id           int auto_increment comment 'Company''s ID'
        primary key,
    FK_User_uuid uuid         not null comment 'Foreign key - User''s UUID',
    nip          varchar(16)  not null comment 'Company''s NIP number',
    name         varchar(128) not null comment 'Company''s name',
    description  varchar(512) null comment 'Information about the company',
    address      varchar(512) null comment 'Company''s address',
    logo_img     blob         null comment 'Company''s brand mark logotype image',
    constraint Companies_Users_uuid_fk
        foreign key (FK_User_uuid) references Users (uuid)
)
    comment 'Companies';

create table if not exists Courses
(
    id            int auto_increment comment 'Course''s ID'
        primary key,
    FK_Company_id int                    not null comment 'Foreign Key - Company''s ID',
    title         varchar(256)           not null comment 'Course''s title',
    price         int  default 0         not null comment 'Course price',
    duration      int                    not null comment 'Course duration in hours',
    places        int  default 1         not null comment 'Course available places',
    address       varchar(512)           null comment 'Course address',
    description   varchar(1024)          null comment 'Course description',
    opportunities varchar(1024)          null comment 'Possible opportunities after the course',
    expire_date   date                   null comment 'Course expiration date',
    img           blob                   null comment 'Course''s image',
    created_at    date default curdate() not null comment 'Course publish date',
    constraint Courses_Companies_id_fk
        foreign key (FK_Company_id) references Companies (id)
)
    comment 'Course offers';

create table if not exists CourseRequirements
(
    id           int auto_increment comment 'Requirement''s ID'
        primary key,
    FK_Course_id int not null comment 'Foreign key - Course''s ID',
    FK_Skill_id  int not null comment 'Foreign key - Skill''s ID',
    constraint CourseRequirements_Courses_id_fk
        foreign key (FK_Course_id) references Courses (id),
    constraint CourseRequirements_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Course''s requirements';

create table if not exists CourseSkills
(
    id           int auto_increment comment 'Record''s ID'
        primary key,
    FK_Course_id int not null comment 'Foreign key - Course''s ID',
    FK_Skill_id  int not null comment 'Foreign key - Skill''s ID',
    constraint CourseSkills_Courses_id_fk
        foreign key (FK_Course_id) references Courses (id),
    constraint CourseSkills_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Skills to obtain after the course';

create table if not exists Jobs
(
    id               int auto_increment comment 'Job Offer''s ID'
        primary key,
    FK_Company_id    int                                                                   not null comment 'Foreign key - Company''s ID',
    title            varchar(256)                                                          not null comment 'Job Offer''s title',
    working_time     enum ('full-time', 'part-time', 'temporary')                          not null comment 'Job''s working time enum',
    contract_type    enum ('employment', 'contract', 'task-specific', 'internship', 'b2b') not null comment 'Type of job''s contract',
    work_type        enum ('stationary', 'hybrid', 'remote', 'mobile')                     not null comment 'Type of work',
    position         varchar(80)                                                           not null comment 'Official position',
    address          varchar(256)                                                          not null comment 'Work address',
    salary_min       int                                                                   null comment 'Minimal salary',
    salary_max       int                                                                   null comment 'Maximal salary',
    responsibilities varchar(1024)                                                         not null comment 'Work responsibilities',
    description      varchar(1024)                                                         null comment 'Job description',
    expire_date      date                                                                  null comment 'Job offer''s expiration date',
    img              blob                                                                  null comment 'Job''s image',
    created_at       date default curdate()                                                not null comment 'Job offer publish date',
    constraint Jobs_Companies_id_fk
        foreign key (FK_Company_id) references Companies (id)
)
    comment 'Job offers';

create table if not exists JobRequirements
(
    id          int auto_increment comment 'Requirement''s ID'
        primary key,
    FK_Job_id   int not null comment 'Foreign key - Job''s ID',
    FK_Skill_id int not null comment 'Foreign key - Skill''s ID',
    constraint JobRequirements_Jobs_id_fk
        foreign key (FK_Job_id) references Jobs (id),
    constraint JobRequirements_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Job''s requirements';

create table if not exists Workers
(
    id           int auto_increment comment 'Worker''s ID'
        primary key,
    FK_User_uuid uuid        not null comment 'Foreign key - User''s UUID',
    name         varchar(40) null comment 'User''s name',
    surname      varchar(60) null comment 'User''s surname',
    profile_img  blob        null comment 'Personal profile photo image',
    constraint Workers_Users_uuid_fk
        foreign key (FK_User_uuid) references Users (uuid)
)
    comment 'Workers';

create table if not exists CourseParticipants
(
    id           int auto_increment comment 'Course participant ID'
        primary key,
    FK_Course_id int not null comment 'Foreign key - Course''s ID',
    FK_Worker_id int not null comment 'Foreign key - Worker''s ID',
    constraint CourseParticipants_Courses_id_fk
        foreign key (FK_Course_id) references Courses (id),
    constraint CourseParticipants_Workers_id_fk
        foreign key (FK_Worker_id) references Workers (id)
)
    comment 'Course''s participants';

create table if not exists JobApplicants
(
    id           int auto_increment comment 'JobApplicant''s ID'
        primary key,
    FK_Job_id    int not null comment 'Foreign key - Job''s ID',
    FK_Worker_id int not null comment 'Foreign key - Worker''s ID',
    constraint JobApplicants_Jobs_id_fk
        foreign key (FK_Job_id) references Jobs (id),
    constraint JobApplicants_Workers_id_fk
        foreign key (FK_Worker_id) references Workers (id)
)
    comment 'Job offer applicants';

create table if not exists Reports
(
    id            int auto_increment comment 'Report''s ID'
        primary key,
    FK_Worker_id  int          not null comment 'Foreign key - Worker''s ID',
    date_of_birth date         not null comment 'Worker''s date of birth',
    address       varchar(512) null comment 'Worker''s address',
    constraint Reports_Workers_id_fk
        foreign key (FK_Worker_id) references Workers (id)
)
    comment 'Worker''s report';

create table if not exists ReportEducations
(
    id             int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id   int                                                                                          not null comment 'Foreign key - Reports'' ID',
    level          enum ('primary', 'secondary', 'bachelor', 'master', 'doctorate', 'vocational', 'continuing') not null comment 'Level of education',
    school         varchar(512)                                                                                 not null comment 'School''s name',
    specialization varchar(128)                                                                                 null comment 'Specialization',
    begin_date     date                                                                                         not null comment 'Education beginning date',
    end_date       date                                                                                         null comment 'Education end date',
    is_ongoing     tinyint(1)                                                                                   not null comment 'Whether education process is ongoing - flag',
    constraint ReportEducations_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
)
    comment 'Educations for worker''s reports';

create table if not exists ReportExperience
(
    id            int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id  int                                                                   not null comment 'Foreign key - Report''s ID',
    company_name  varchar(128)                                                          not null comment 'Company''s name',
    position      varchar(80)                                                           not null comment 'Official position',
    address       varchar(512)                                                          not null comment 'Work address',
    contract_type enum ('employment', 'contract', 'task-specific', 'internship', 'b2b') not null comment 'Type of job''s contract',
    work_type     enum ('stationary', 'hybrid', 'remote', 'mobile')                     not null comment 'Type of work',
    begin_date    date                                                                  not null comment 'Work beginning date',
    end_date      date                                                                  null comment 'Work end date',
    is_ongoing    tinyint(1)                                                            not null comment 'Whether work is ongoing - flag',
    constraint ReportExperience_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
)
    comment 'Worker''s experience in report';

create table if not exists ReportSkills
(
    id           int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id int not null comment 'Foreign key - Report''s ID',
    FK_Skill_id  int not null comment 'Foreign key - Skill''s ID',
    constraint ReportSkills_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id),
    constraint ReportSkills_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Worker''s skills in report';



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