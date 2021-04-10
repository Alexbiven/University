CREATE DATABASE University;

Use University

CREATE TABLE human
(
	id INT PRIMARY KEY AUTO_INCREMENT,
	surname VARCHAR(20)NOT NULL,
    name VARCHAR(15) NOT NULL,
    date_of_birth DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    login VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL
);



CREATE TABLE progress
(
	id INT PRIMARY KEY AUTO_INCREMENT,
	surname VARCHAR(20)NOT NULL,
    name VARCHAR(15) NOT NULL,
    date_of_birth DATE NOT NULL,
    status VARCHAR(20) NOT NULL  ,
    course INT NOT NULL,
    maths INT NOT NULL,
    physics INT NOT NULL,
    informatics INT NOT NULL,
    literature INT NOT NULL,
    philosophy INT NOT NULL,
    average_ball FLOAT NOT NULL

);



INSERT INTO human (id, login, password,name,surname) VALUES (1,'biven36', 'alexpolinka','Alexandr', 'Pisarev')


