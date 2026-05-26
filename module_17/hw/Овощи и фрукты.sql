CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('овощ', 'фрукт')),
    color VARCHAR(50),
    calories INTEGER CHECK (calories >= 0),
    description TEXT
);

-- Заполнение таблицы тестовыми данными: 4 овоща и 4 фрукта
INSERT INTO products (name, type, color, calories, description) VALUES
-- Овощи
('Морковь', 'овощ', 'оранжевый', 41, 'Источник бета‑каротина, полезен для зрения'),
('Огурец', 'овощ', 'зелёный', 15, 'Низкокалорийный овощ, содержит много воды'),
('Помидор', 'овощ', 'красный', 24, 'Сочный овощ, богат ликопином'),
('Болгарский перец', 'овощ', 'красный', 26, 'Богатый источник витамина C, сладкий вкус'),

-- Фрукты
('Апельсин', 'фрукт', 'оранжевый', 47, 'Цитрусовый фрукт'),
('Яблоко', 'фрукт', 'красный', 52, 'Сладкий фрукт, богат витамином C и клетчаткой'),
('Банан', 'фрукт', 'жёлтый', 89, 'Содержит калий, быстро даёт энергию'),
('Груша', 'фрукт', 'зелёный', 57, 'Сладкий, содержит пищевые волокна');

-- 1. Отображение всей информации из таблицы с овощами и фруктами
SELECT * FROM products;

-- 2. Отображение всех овощей
SELECT * FROM products
WHERE type = 'овощ';

-- 3. Отображение всех фруктов
SELECT * FROM products
WHERE type = 'фрукт';

-- 4. Отображение всех названий овощей и фруктов
SELECT name FROM products;

-- 5. Отображение всех цветов (уникальные значения)
SELECT DISTINCT color FROM products;

-- 6. Отображение фруктов конкретного цвета (пример для оранжевых фруктов)
SELECT * FROM products
WHERE type = 'фрукт' AND color = 'оранжевый';

-- 7. Отображение овощей конкретного цвета (пример для зелёных овощей)
SELECT * FROM products
WHERE type = 'овощ' AND color = 'зелёный';

-- Домашнее задание 2

-- 8. Отображение всех овощей с калорийностью меньше указанной
-- Замените 50 на нужное значение калорийности
SELECT * FROM products
WHERE type = 'овощ' AND calories < 50;

-- 9. Отображение всех фруктов с калорийностью в указанном диапазоне
-- Замените 40 и 80 на нужные границы диапазона
SELECT * FROM products
WHERE type = 'фрукт' AND calories BETWEEN 40 AND 80;

-- 10. Отображение всех овощей, в названии которых есть указанное слово
-- Замените 'Морковь' на нужное слово
SELECT * FROM products
WHERE type = 'овощ' AND name LIKE 'Морковь';

-- 11. Отображение всех овощей и фруктов, в кратком описании которых есть указанное слово
-- Замените '%фрукт%' на нужное слово
SELECT * FROM products
WHERE description LIKE '%фрукт%';

-- 12. Отображение всех овощей и фруктов жёлтого или красного цвета
SELECT * FROM products
WHERE color IN ('жёлтый', 'красный');

--  Показать количество овощей
SELECT COUNT(*) AS vegetable_count
FROM products
WHERE type = 'овощ';

--  Показать количество фруктов
SELECT COUNT(*) AS fruit_count
FROM products
WHERE type = 'фрукт';

--  Показать количество овощей и фруктов заданного цвета
-- Замените 'красный' на нужный цвет
SELECT COUNT(*) AS count_by_color
FROM products
WHERE color = 'красный';

--  Показать количество овощей и фруктов каждого цвета
SELECT color, COUNT(*) AS count
FROM products
GROUP BY color
ORDER BY count DESC;

--  Показать цвет с минимальным количеством овощей и фруктов
SELECT color, COUNT(*) AS min_count
FROM products
GROUP BY color
ORDER BY min_count ASC
LIMIT 1;

--  Показать цвет с максимальным количеством овощей и фруктов
SELECT color, COUNT(*) AS max_count
FROM products
GROUP BY color
ORDER BY max_count DESC
LIMIT 1;

--  Показать минимальную калорийность овощей и фруктов
SELECT MIN(calories) AS min_calories
FROM products;

--  Показать максимальную калорийность овощей и фруктов
SELECT MAX(calories) AS max_calories
FROM products;

--  Показать среднюю калорийность овощей и фруктов
SELECT ROUND(AVG(calories), 2) AS avg_calories
FROM products;

--  Показать фрукт с минимальной калорийностью
SELECT *
FROM products
WHERE type = 'фрукт'
ORDER BY calories ASC
LIMIT 1;

--  Показать фрукт с максимальной калорийностью
SELECT *
FROM products
WHERE type = 'фрукт'
ORDER BY calories DESC
LIMIT 1;

