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
    average_ball FLOAT NOT NULL
);

INSERT INTO human (id,surname,name,middle_name,status) VALUES (1,'Иванова','Татьяна','Николаевна','Преподаватель');
INSERT INTO human (surname,name,status,course,faculty,assessment,average_ball)
			VALUES
            ('Петров','Олег','Студент',4,'Психология',8,4.0),
            ('Пупкин','Сергей','Студент',2,'Биология',4,5.8),
            ('Денисов','Николай','Студент',1,'Физика и математика',7,4.5),
            ('Никольский','Вадим','Студент',3,'Информатика',8,8.5),
            ('Зеленкин','Антон','Студент',4,'Иностранные языки',8,7.9);