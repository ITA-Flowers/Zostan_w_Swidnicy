create table if not exists Skills
(
    id   int auto_increment comment 'Skill''s ID'
        primary key,
    name varchar(256) not null comment 'Skill''s name',
    constraint Skills_name
        unique (name)
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
    is_admin     tinyint(1)          not null comment 'Administrator type account flag',
    constraint Users_email
        unique (email)
)
    comment 'Users';

create table if not exists Companies
(
    id           int auto_increment comment 'Company''s ID'
        primary key,
    FK_User_uuid uuid         not null comment 'Foreign key - User''s UUID',
    nip          varchar(16)  not null comment 'Company''s NIP number',
    name         varchar(128) not null comment 'Company''s name',
    description  varchar(2048) null comment 'Information about the company',
    address      varchar(512) null comment 'Company''s address',
    url          varchar(512) null comment 'Company''s website address',
    logo_img     varchar(256) null comment 'Company''s brand mark logotype image filepath',
    constraint Companies_nip
        unique (nip),
    constraint Companies_Users_uuid_fk
        foreign key (FK_User_uuid) references Users (uuid)
            on update cascade on delete cascade
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
    img           varchar(256)           null comment 'Course''s image filepath',
    created_at    date default curdate() not null comment 'Course publish date',
    constraint Courses_Companies_id_fk
        foreign key (FK_Company_id) references Companies (id)
            on update cascade on delete cascade
)
    comment 'Course offers';

create table if not exists CourseRequirements
(
    id           int auto_increment comment 'Requirement''s ID'
        primary key,
    FK_Course_id int not null comment 'Foreign key - Course''s ID',
    FK_Skill_id  int not null comment 'Foreign key - Skill''s ID',
    constraint CourseRequirements_Courses_id_fk
        foreign key (FK_Course_id) references Courses (id)
            on update cascade on delete cascade,
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
        foreign key (FK_Course_id) references Courses (id)
            on update cascade on delete cascade,
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
    img              varchar(256)                                                          null comment 'Job''s image filepath',
    created_at       date default curdate()                                                not null comment 'Job offer publish date',
    constraint Jobs_Companies_id_fk
        foreign key (FK_Company_id) references Companies (id)
            on update cascade on delete cascade
)
    comment 'Job offers';

create table if not exists JobRequirements
(
    id          int auto_increment comment 'Requirement''s ID'
        primary key,
    FK_Job_id   int not null comment 'Foreign key - Job''s ID',
    FK_Skill_id int not null comment 'Foreign key - Skill''s ID',
    constraint JobRequirements_Jobs_id_fk
        foreign key (FK_Job_id) references Jobs (id)
            on update cascade on delete cascade,
    constraint JobRequirements_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Job''s requirements';

create table if not exists Workers
(
    id           int auto_increment comment 'Worker''s ID'
        primary key,
    FK_User_uuid uuid         not null comment 'Foreign key - User''s UUID',
    name         varchar(40)  null comment 'User''s name',
    surname      varchar(60)  null comment 'User''s surname',
    profile_img  varchar(256) null comment 'Personal profile photo image filepath',
    constraint Workers_Users_uuid_fk
        foreign key (FK_User_uuid) references Users (uuid)
            on update cascade on delete cascade
)
    comment 'Workers';

create table if not exists CourseParticipants
(
    id           int auto_increment comment 'Course participant ID'
        primary key,
    FK_Course_id int not null comment 'Foreign key - Course''s ID',
    FK_Worker_id int not null comment 'Foreign key - Worker''s ID',
    constraint CourseParticipants_Courses_id_fk
        foreign key (FK_Course_id) references Courses (id)
            on update cascade on delete cascade,
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
        foreign key (FK_Job_id) references Jobs (id)
            on update cascade on delete cascade,
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
            on update cascade on delete cascade
)
    comment 'Worker''s report';

create table if not exists ReportCerts
(
    id           int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id int          not null comment 'Foreign key - Report''s ID',
    certname     varchar(256) not null comment 'Cerificate''s name',
    hostname     varchar(256) not null comment 'Certificate course host''s name',
    obtain_date  date         not null comment 'Certificate''s obtain date',
    constraint ReportCerts_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
            on update cascade on delete cascade
)
    comment 'Report''s certificates';

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
            on update cascade on delete cascade
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
            on update cascade on delete cascade
)
    comment 'Worker''s experience in report';

create table if not exists ReportLanguages
(
    id           int auto_increment
        primary key,
    FK_Report_id int                                                                                             not null comment 'Foreign Key - Report''s ID',
    language     varchar(64)                                                                                     not null comment 'Language name',
    level        enum ('beginner', 'elementary', 'intermediate', 'upper-intermediate', 'advanced', 'proficient') not null comment 'Knowledge level',
    constraint ReportLang_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
            on update cascade on delete cascade
)
    comment 'Knowledge of foreign languages for report';

create table if not exists ReportLinks
(
    id           int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id int          not null comment 'Foreign key - Report''s ID',
    name         varchar(128) not null comment 'Link''s name',
    url          varchar(512) not null comment 'URL address',
    constraint ReportLinks_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
            on update cascade on delete cascade
)
    comment 'Report''s hyperlinks';

create table if not exists ReportSkills
(
    id           int auto_increment comment 'Record''s ID'
        primary key,
    FK_Report_id int not null comment 'Foreign key - Report''s ID',
    FK_Skill_id  int not null comment 'Foreign key - Skill''s ID',
    constraint ReportSkills_Reports_id_fk
        foreign key (FK_Report_id) references Reports (id)
            on update cascade on delete cascade,
    constraint ReportSkills_Skills_id_fk
        foreign key (FK_Skill_id) references Skills (id)
)
    comment 'Worker''s skills in report';


CREATE USER 'hyacinthus'@'%' IDENTIFIED BY 'FlowerChamaedorea000Z';
GRANT ALL PRIVILEGES ON swidnica.* TO 'hyacinthus'@'%';
FLUSH PRIVILEGES;
