USE swidnica;

CREATE TABLE ip_addresses (

    ip_address VARCHAR(15) PRIMARY KEY
	
);

CREATE TABLE login_time (

    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_id VARCHAR(15) NOT NULL,
    time INT NOT NULL DEFAULT 1,
    FOREIGN KEY (ip_id) REFERENCES ip_addresses(ip_address)
	
);

INSERT INTO ip_addresses (ip_address) VALUES
    ('192.168.1.1'),
    ('10.0.0.1'),
    ('172.16.0.1'),
    ('192.168.2.1'),
    ('10.0.0.2'),
    ('172.16.0.2');


INSERT INTO login_time (ip_id, time) VALUES
    ('192.168.1.1', 5),
    ('10.0.0.1', 3),
    ('172.16.0.1', 2),
    ('192.168.2.1', 7),
    ('10.0.0.2', 4),
    ('172.16.0.2', 6),
    ('192.168.1.1', 2),
    ('10.0.0.1', 1),
    ('172.16.0.1', 3);

CREATE USER 'exampleuser'@'%';
SET PASSWORD FOR 'exampleuser'@'%' = PASSWORD('my_cool_secret');	
grant all privileges on *.* to 'exampleuser'@'%';