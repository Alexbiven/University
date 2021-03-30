CREATE DATABASE University;

Use University

CREATE TABLE Human
(
	id INT PRIMARY KEY AUTO_INCREMENT,
	surname VARCHAR(20)NOT NULL,
    name VARCHAR(15) NOT NULL,
    middle_name VARCHAR(20)NOT NULL,
    status TEXT NOT NULL,
    course INT NOT NULL,
    faculty TEXT NOT NULL,
    assessment INT NOT NULL,
    average_ball FLOAT NOT NULL,
    login VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL
);




CREATE TABLE Registration
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(30) NOT NULL,
    password VARCHAR(35) NOT NULL,
    status TEXT NOT NULL

);

CREATE TABLE Authorization
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(30) NOT NULL,
    password VARCHAR(35) NOT NULL

);