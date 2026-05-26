-- Таблица Кафедры (Departments)
CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != ''),
    Financing DECIMAL(12,2) NOT NULL CHECK (Financing >= 0)
);

-- Таблица Факультеты (Faculties)
CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != ''),
    Dean VARCHAR(100) NOT NULL CHECK (Dean != '')
);

-- Таблица Группы (Groups)
CREATE TABLE Groups (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE CHECK (Name != ''),
    Rating INTEGER NOT NULL CHECK (Rating >= 0 AND Rating <= 5),
    Year INTEGER NOT NULL CHECK (Year >= 1 AND Year <= 5)
);

-- Таблица Преподаватели (Teachers)
CREATE TABLE Teachers (
    Id SERIAL PRIMARY KEY,
    Surname VARCHAR(50) NOT NULL CHECK (Surname != ''),
    Name VARCHAR(50) NOT NULL CHECK (Name != ''),
    Position VARCHAR(50) NOT NULL CHECK (Position != ''),
    Salary DECIMAL(10,2) NOT NULL CHECK (Salary > 0),
    Premium DECIMAL(10,2) NOT NULL CHECK (Premium >= 0),
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
    IsAssistant BOOLEAN NOT NULL,
    IsProfessor BOOLEAN NOT NULL
);

-- Заполняем факультеты
INSERT INTO Faculties (Name, Dean) VALUES
('Математический', 'Иванов А.С.'),
('Computer Science', 'Петрова М.И.'),
('Гуманитарный', 'Сидоров В.П.'),
('Естественно‑научный', 'Орлова Л.М.');

-- Заполняем кафедры
INSERT INTO Departments (Name, Financing) VALUES
('Высшая математика', 15000.00),
('Информатика', 30000.00),
('История', 8000.00),
('Биология', 22000.00);

-- Заполняем группы
INSERT INTO Groups (Name, Rating, Year) VALUES
('М‑101', 4, 1),
('И‑201', 5, 2),
('Г‑502', 3, 5),
('Б‑501', 4, 5),
('М‑305', 2, 3);

-- Заполняем преподавателей
INSERT INTO Teachers (Surname, Name, Position, Salary, Premium, EmploymentDate, IsAssistant, IsProfessor) VALUES
('Васильев', 'Иван', 'Профессор', 1200.00, 300.00, '1998-05-15', FALSE, TRUE),
('Григорьева', 'Мария', 'Доцент', 900.00, 200.00, '2005-09-01', FALSE, FALSE),
('Дмитриев', 'Алексей', 'Профессор', 1100.00, 250.00, '1999-03-10', FALSE, TRUE),
('Егорова', 'Елена', 'Ассистент', 500.00, 180.00, '2010-08-20', TRUE, FALSE),
('Фёдоров', 'Сергей', 'Ассистент', 450.00, 150.00, '2012-06-15', TRUE, FALSE),
('Павлова', 'Анна', 'Старший преподаватель', 600.00, 400.00, '2008-02-28', FALSE, FALSE);

-- 1. Вывести таблицу кафедр, но расположить её поля в обратном порядке
SELECT Financing, Name, Id
FROM Departments;

-- 2. Вывести названия групп и их рейтинги с уточнением имён полей именем таблицы
SELECT Groups.Name AS "Groups.Name",
       Groups.Rating AS "Groups.Rating"
FROM Groups;

-- 3. Вывести для преподавателей их фамилию, процент ставки по отношению к надбавке
-- и процент ставки по отношению к зарплате (сумма ставки и надбавки)
SELECT
    Surname AS "Фамилия",
    CASE
        WHEN Premium > 0 THEN ROUND((Salary / Premium) * 100, 2)
        ELSE NULL
    END AS "Процент ставки к надбавке",
    ROUND((Salary / (Salary + Premium)) * 100, 2) AS "Процент ставки к зарплате"
FROM Teachers;

-- 4. Вывести таблицу факультетов в виде одного поля в формате «[dean]»
SELECT CONCAT('[', Dean, ']') AS dean
FROM Faculties;

-- 5. Вывести фамилии преподавателей, которые являются профессорами и ставка которых превышает 1050
SELECT Surname
FROM Teachers
WHERE IsProfessor = TRUE AND Salary > 1050;

-- 6. Вывести названия кафедр, фонд финансирования которых меньше 11000 или больше 25000
SELECT Name
FROM Departments
WHERE Financing < 11000 OR Financing > 25000;

-- 7. Вывести названия факультетов кроме факультета “Computer Science” (с использованием NOT IN)
SELECT Name
FROM Faculties
WHERE Name NOT IN ('Computer Science');

-- 8. Вывести фамилии и должности преподавателей, которые не являются профессорами
SELECT Surname, Position
FROM Teachers
WHERE IsProfessor = FALSE;

-- 9. Вывести фамилии, должности, ставки и надбавки ассистентов, у которых надбавка в диапазоне от 160 до 550
SELECT Surname, Position, Salary, Premium
FROM Teachers
WHERE IsAssistant = TRUE AND Premium BETWEEN 160 AND 550;

-- 10. Вывести фамилии и ставки ассистентов
SELECT Surname, Salary
FROM Teachers
WHERE IsAssistant = TRUE;

-- 11. Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000
SELECT Surname, Position
FROM Teachers
WHERE EmploymentDate < '2000-01-01';

-- 12. Вывести названия кафедр в алфавитном порядке. Выводимое поле должно иметь название “Name of Department”
SELECT Name AS "Name of Department"
FROM Departments
ORDER BY Name ASC;

-- 13. Вывести фамилии ассистентов, имеющих зарплату (сумма ставки и надбавки) не более 1200
SELECT Surname
FROM Teachers
WHERE IsAssistant = TRUE AND (Salary + Premium) <= 1200;

-- 14. Вывести названия групп 5‑го курса, имеющих рейтинг в диапазоне от 2 до 4
SELECT Name
FROM Groups
WHERE Year = 5 AND Rating BETWEEN 2 AND 4;

-- 15. Вывести фамилии ассистентов со ставкой меньше 550 или надбавкой меньше 200
SELECT Surname
FROM Teachers
WHERE IsAssistant = TRUE AND (Salary < 550 OR Premium < 200);

