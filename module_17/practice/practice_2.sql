CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10, 2) CHECK (salary > 0),
    department_id INT REFERENCES departments(id),
    hired_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    employee_id INT REFERENCES employees(id),
    budget NUMERIC(12, 2) CHECK (budget >= 0),
    is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO departments (name)
VALUES
    ('IT'),
    ('HR'),
    ('Finance'),
    ('Marketing');

INSERT INTO employees (name, salary, department_id, hired_at)
VALUES
    ('Анна Иванова', 150000, 1, '2023-01-15'),
    ('Иван Петров', 90000, 1, '2023-03-10'),
    ('Мария Смирнова', 110000, 2, '2022-11-20'),
    ('Олег Кузнецов', 130000, 3, '2021-06-05'),
    ('Алексей Орлов', 70000, NULL, '2024-02-01'),
    ('Елена Соколова', 160000, 1, '2020-09-12');

INSERT INTO projects (name, employee_id, budget, is_active)
VALUES
    ('CRM System', 1, 500000, TRUE),
    ('Website Redesign', 2, 200000, TRUE),
    ('Hiring Platform', 3, 300000, TRUE),
    ('Accounting Automation', 4, 350000, FALSE),
    ('Internal Chat', 1, 150000, TRUE);

SELECT 
	name, 
    salary,
    CASE 
        WHEN salary >= 150000 THEN 'high' 
        WHEN salary >= 80000 THEN 'medium'
        ELSE 'low'
    END AS salary_level
FROM employees;

-- -------------

SELECT 
	e.name as employe_name,
	coalesce(d.name, 'без отдела') as department_name
from employees e
left join departments d on e.department_id= d.id

-- --------------

SELECT 
	d.id,
	d.name
from departments d
where exists (
	select 1 from employees e
	where e.department_id =d.id
);

-- --------------

SELECT 
	d.id,
	d.name
from employees d
where exists (
	select 1 from projects e
	where e.employee_id =d.id
);

-- ----------------

select 
	name as project_name,
	budget,
	case
		when is_active= true then 'active'
		else 'close'
	end as project_status
from projects

-- ------------------

select 
	e.name as employee_name,
	count(p.id) as project_count
from employees e 
left join projects p on p.employee_id= e.id 
group by e.id, e.name 
order by  project_count desc;

-- ----------------

UPDATE projects
SET budget = budget + 50000
WHERE is_active = true
returning id, name, budget, is_active;
	
-- ----------------

delete from projects 
where is_active = false 
returning id, name, budget, is_active;
create table employee_profiles(
	id SERIAL primary key,
	employee_id INT unique references employees(id),
	phone TEXT unique ,
	address TEXT,
	birth_data DATE 
);

insert into employee_profiles(employee_id, phone, address, birth_data)
values 
	(1, '+70000000001', 'address-1', '1980-05-25'),
	(2, '+70000000002', 'address-2', '1981-05-25'),
	(3, '+70000000003', 'address-3', '1982-05-25');

select 
	e.name as employee_name,
	ep.phone,
	ep.address,
	ep.birth_data
from employees e
join employee_profiles ep on ep.employee_id= e.id;

insert into employee_profiles(employee_id,phone,address,birth_data)
values
	(1, '+70000000004', 'address-4', '1983-05-25');

-- ---------------------

create table skills(
	id SERIAL primary key,
	name TEXT not null unique 
);

create table employee_skills(
	employee_id INT references employees(id),
	skill_id int references skills(id),
	primary key (employee_id, skill_id)
);

insert into skills (name)
values 
	('SQL'),
	('PostgreSQL'),
	('MySQL'),
	('Exel');

insert into employee_skills (employee_id, skill_id)
values 
	(1, 1),
	(2, 1),
	(3, 1),
	(1, 2),
	(2, 2),
	(3, 2),
	(1, 4);

select 
	e.name as employee_name,
	s.name as skill_name
from employee_skills es 
join employees e on es.employee_id= e.id 
join skills s on es.skill_id= s.id
order by e.name, s.name;

-- -------------

select
	e.name as employee_name,
	e.salary as salary,
	d.name AS department_name,
    ep.phone AS phone,
    ep.address AS address,
    p.name AS project_name,
    s.name AS skill_name
FROM employees e
left JOIN employee_profiles ep ON ep.employee_id=e.id
left JOIN departments d ON e.department_id = d.id
left JOIN projects p ON p.employee_id = e.id
left JOIN employee_skills es ON es.employee_id=e.id
left JOIN skills s ON es.skill_id = s.id
ORDER BY e.name, s.name, p.name;


-- -------------------------------

SELECT
    e.name AS employee_name,
    COALESCE(SUM(p.budget), 0) AS total_budget
FROM employees e
LEFT JOIN projects p ON p.employee_id = e.id
GROUP BY e.id, e.name
ORDER BY e.name;

-- ------------------------------

SELECT
    p.name AS project_name,
    p.budget AS budget,
    e.name AS employee_name,
    d.name AS department_name
FROM projects p
JOIN employees e ON p.employee_id = e.id
JOIN departments d ON e.department_id = d.id
WHERE
    p.is_active = true
    AND p.budget > 200000.00
    AND e.department_id IS NOT NULL
ORDER BY p.budget DESC;

