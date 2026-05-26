-- Таблица Факультеты (Faculties)
CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != ''),
    Dean VARCHAR(100) NOT NULL CHECK (Dean != ''),
    Financing DECIMAL(12,2) NOT NULL DEFAULT 0 CHECK (Financing >= 0)
);

-- Таблица Кафедры (Departments)
CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != ''),
    Financing DECIMAL(12,2) NOT NULL CHECK (Financing >= 0),
    FacultyId INTEGER NOT NULL REFERENCES Faculties(Id)
);


-- Таблица Группы (Groups)
CREATE TABLE Groups (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE CHECK (Name != ''),
    Rating INTEGER NOT NULL CHECK (Rating >= 0 AND Rating <= 5),
    Year INTEGER NOT NULL CHECK (Year >= 1 AND Year <= 5),
    DepartmentId INTEGER NOT NULL REFERENCES Departments(Id)
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

-- Таблица Дисциплины (Subjects)
CREATE TABLE Subjects (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != '')
);

-- Таблица Лекции (Lectures)
CREATE TABLE Lectures (
    Id SERIAL PRIMARY KEY,
    LectureRoom VARCHAR(50) NOT NULL CHECK (LectureRoom != ''),
    SubjectId INTEGER NOT NULL REFERENCES Subjects(Id),
    TeacherId INTEGER NOT NULL REFERENCES Teachers(Id)
);

-- Таблица Кураторы (Curators)
CREATE TABLE Curators (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(50) NOT NULL CHECK (Name != ''),
    Surname VARCHAR(50) NOT NULL CHECK (Surname != '')
);

-- Таблица Группы и кураторы (GroupsCurators)
CREATE TABLE GroupsCurators (
    Id SERIAL PRIMARY KEY,
    CuratorId INTEGER NOT NULL REFERENCES Curators(Id),
    GroupId INTEGER NOT NULL REFERENCES Groups(Id)
);

-- Таблица Группы и лекции (GroupsLectures)
CREATE TABLE GroupsLectures (
    Id SERIAL PRIMARY KEY,
    GroupId INTEGER NOT NULL REFERENCES Groups(Id),
    LectureId INTEGER NOT NULL REFERENCES Lectures(Id)
);

-- Заполнение данными

-- Заполняем факультеты
INSERT INTO Faculties (Name, Dean, Financing) VALUES
('Математический', 'Иванов А.С.', 10000.00),
('Computer Science', 'Петрова М.И.', 25000.00),
('Гуманитарный', 'Сидоров В.П.', 8000.00),
('Естественно‑научный', 'Орлова Л.М.', 20000.00);

-- Заполняем кафедры
INSERT INTO Departments (Name, Financing, FacultyId) VALUES
('Высшая математика', 15000.00, 1),
('Информатика', 30000.00, 2),
('История', 8000.00, 3),
('Биология', 22000.00, 4);

-- Заполняем группы
INSERT INTO Groups (Name, Rating, Year, DepartmentId) VALUES
('М‑101', 4, 1, 1),
('И‑201', 5, 2, 2),
('Г‑502', 3, 5, 3),
('Б‑501', 4, 5, 4),
('М‑305', 2, 3, 1);

-- Заполняем преподавателей
INSERT INTO Teachers (Surname, Name, Position, Salary, Premium, EmploymentDate, IsAssistant, IsProfessor) VALUES
('Васильев', 'Иван', 'Профессор', 1200.00, 300.00, '1998-05-15', FALSE, TRUE),
('Григорьева', 'Мария', 'Доцент', 900.00, 200.00, '2005-09-01', FALSE, FALSE),
('Дмитриев', 'Алексей', 'Профессор', 1100.00, 250.00, '1999-03-10', FALSE, TRUE),
('Егорова', 'Елена', 'Ассистент', 500.00, 180.00, '2010-08-20', TRUE, FALSE),
('Фёдоров', 'Сергей', 'Ассистент', 450.00, 150.00, '2012-06-15', TRUE, FALSE),
('Павлова', 'Анна', 'Старший преподаватель', 600.00, 400.00, '2008-02-28', FALSE, FALSE),
('Adams', 'Samantha', 'Профессор', 1300.00, 350.00, '2001-09-01', FALSE, TRUE);

-- Заполняем дисциплины
INSERT INTO Subjects (Name) VALUES
('Математика'),
('Программирование'),
('История'),
('Биология'),
('Физика'),
('Database Theory');

-- Заполняем кураторов
INSERT INTO Curators (Name, Surname) VALUES
('Ольга', 'Николаева'),
('Дмитрий', 'Козлов'),
('Елена', 'Смирнова');

-- Связываем кураторов с группами
INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
(1, 1),  -- Ольга Николаева курирует М‑101
(2, 2),  -- Дмитрий Козлов курирует И‑201
(3, 3);  -- Елена Смирнова курирует Г‑502

-- Заполняем лекции
INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
('B103', 1, 1),  -- Математика, Васильев
('A205', 2, 2),  -- Программирование, Григорьева
('C301', 3, 3),  -- История, Дмитриев
('B103', 4, 4),  -- Биология, Егорова
('A205', 5, 6),  -- Физика, Павлова
('B103', 6, 7),  -- Database Theory, Samantha Adams
('B103', 1, 7);  -- Математика, Samantha Adams

-- Связываем группы с лекциями
INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
(1, 1),  -- М‑101 на лекции 1 (Математика, B103)
(2, 2),  -- И‑201 на лекции 2 (Программирование, A205)
(3, 3),  -- Г‑502 на лекции 3 (История, C301)
(4, 4),  -- Б‑501 на лекции 4 (Биология, B103)
(5, 5),  -- М‑305 на лекции 5 (Физика, A205)
(1, 6),  -- М‑101 на лекции 6 (Database Theory, B103, Samantha Adams)
(1, 7);  -- М‑101 на лекции 7 (Математика, B103, Samantha Adams)

-- Запросы для Задания 1

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
SELECT Surname AS "Фамилия"
FROM Teachers
WHERE IsProfessor = TRUE AND Salary > 1050;

-- 6. Вывести названия кафедр, фонд финансирования которых меньше 11000 или больше 25000
SELECT Name AS "Название кафедры"
FROM Departments
WHERE Financing < 11000 OR Financing > 25000;

-- 7. Вывести названия факультетов кроме факультета “Computer Science” (с использованием NOT IN)
SELECT Name AS "Название факультета"
FROM Faculties
WHERE Name NOT IN ('Computer Science');

-- 8. Вывести фамилии и должности преподавателей, которые не являются профессорами
SELECT Surname AS "Фамилия", Position AS "Должность"
FROM Teachers
WHERE IsProfessor = FALSE;

-- 9. Вывести фамилии, должности, ставки и надбавки ассистентов, у которых надбавка в диапазоне от 160 до 550
SELECT Surname AS "Фамилия", Position AS "Должность", Salary AS "Ставка", Premium AS "Надбавка"
FROM Teachers
WHERE IsAssistant = TRUE AND Premium BETWEEN 160 AND 550;

-- 10. Вывести фамилии и ставки ассистентов
SELECT Surname AS "Фамилия", Salary AS "Ставка"
FROM Teachers
WHERE IsAssistant = TRUE;

-- 11. Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000
SELECT Surname AS "Фамилия", Position AS "Должность"
FROM Teachers
WHERE EmploymentDate < '2000-01-01';

-- 12. Вывести названия кафедр в алфавитном порядке. Выводимое поле должно иметь название “Name of Department”
SELECT Name AS "Name of Department"
FROM Departments
ORDER BY Name ASC;

-- 13. Вывести фамилии ассистентов, имеющих зарплату (сумма ставки и надбавки) не более 1200
SELECT Surname AS "Фамилия"
FROM Teachers
WHERE IsAssistant = TRUE AND (Salary + Premium) <= 1200;

-- 14. Вывести названия групп 5‑го курса, имеющих рейтинг в диапазоне от 2 до 4
SELECT Name AS "Название группы"
FROM Groups
WHERE Year = 5 AND Rating BETWEEN 2 AND 4;

-- 15. Вывести фамилии ассистентов со ставкой меньше 550 или надбавкой меньше 200
SELECT Surname AS "Фамилия"
FROM Teachers
WHERE IsAssistant = TRUE AND (Salary < 550 OR Premium < 200);

-- Запросы для Задания 2

-- 1. Вывести все возможные пары строк преподавателей и групп (декартово произведение)
SELECT t.Surname AS "Фамилия преподавателя", t.Name AS "Имя преподавателя",
       g.Name AS "Название группы"
FROM Teachers t
CROSS JOIN Groups g;

-- 2. Вывести названия факультетов, фонд финансирования кафедр которых превышает фонд финансирования факультета
SELECT DISTINCT f.Name AS "Название факультета"
FROM Faculties f
JOIN Departments d ON f.Id = d.FacultyId
WHERE d.Financing > f.Financing;

-- 3. Вывести фамилии кураторов групп и названия групп, которые они курируют
SELECT c.Surname AS "Фамилия куратора", g.Name AS "Название группы"
FROM Curators c
JOIN GroupsCurators gc ON c.Id = gc.CuratorId
JOIN Groups g ON gc.GroupId = g.Id;

-- 4. Вывести имена и фамилии преподавателей, которые читают лекции у группы “P107”
-- Сначала добавим группу P107 для демонстрации запроса
INSERT INTO Groups (Name, Rating, Year, DepartmentId)
VALUES ('P107', 4, 3, 2);

-- Добавим лекцию для группы P107
INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId)
VALUES ('A205', 2, 2);  -- Программирование, Григорьева

-- Свяжем группу P107 с лекцией
INSERT INTO GroupsLectures (GroupId, LectureId)
VALUES (6, (SELECT MAX(Id) FROM Lectures));

-- Теперь выполним запрос
SELECT t.Name AS "Имя", t.Surname AS "Фамилия"
FROM Teachers t
JOIN Lectures l ON t.Id = l.TeacherId
JOIN GroupsLectures gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
WHERE g.Name = 'P107';

-- 5. Вывести фамилии преподавателей и названия факультетов, на которых они читают лекции
SELECT DISTINCT t.Surname AS "Фамилия преподавателя", f.Name AS "Название факультета"
FROM Teachers t
JOIN Lectures l ON t.Id = l.TeacherId
JOIN GroupsLectures gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id;

-- 6. Вывести названия кафедр и названия групп, которые к ним относятся
SELECT d.Name AS "Название кафедры", g.Name AS "Название группы"
FROM Departments d
JOIN Groups g ON d.Id = g.DepartmentId;

-- 7. Вывести названия дисциплин, которые читает преподаватель “Samantha Adams”
SELECT s.Name AS "Название дисциплины"
FROM Subjects s
JOIN Lectures l ON s.Id = l.SubjectId
JOIN Teachers t ON l.TeacherId = t.Id
WHERE t.Name = 'Samantha' AND t.Surname = 'Adams';

-- 8. Вывести названия кафедр, на которых читается дисциплина «Математика»
SELECT DISTINCT d.Name AS "Название кафедры"
FROM Departments d
JOIN Groups g ON d.Id = g.DepartmentId
JOIN GroupsLectures gl ON g.Id = gl.GroupId
JOIN Lectures l ON gl.LectureId = l.Id
JOIN Subjects s ON l.SubjectId = s.Id
WHERE s.Name = 'Математика';

-- 9. Вывести названия групп, которые относятся к факультету “Computer Science”
SELECT g.Name AS "Название группы"
FROM Groups g
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id
WHERE f.Name = 'Computer Science';

-- 10. Вывести названия групп 5‑го курса, а также название факультетов, к которым они относятся
SELECT g.Name AS "Название группы", f.Name AS "Название факультета"
FROM Groups g
JOIN Departments d ON g.DepartmentId = d.Id
JOIN Faculties f ON d.FacultyId = f.Id
WHERE g.Year = 5;

-- 11. Вывести полные имена преподавателей и лекции, которые они читают (названия дисциплин и групп),
-- причём отобрать только те лекции, которые читаются в аудитории “B103”
SELECT
    t.Name AS "Имя преподавателя",
    t.Surname AS "Фамилия преподавателя",
    s.Name AS "Название дисциплины",
    g.Name AS "Название группы",
    l.LectureRoom AS "Аудитория"
FROM Teachers t
JOIN Lectures l ON t.Id = l.TeacherId
JOIN Subjects s ON l.SubjectId = s.Id
JOIN GroupsLectures gl ON l.Id = gl.LectureId
JOIN Groups g ON gl.GroupId = g.Id
WHERE l.LectureRoom = 'B103';
