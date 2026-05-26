CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(20) NOT NULL CHECK (type IN ('овощ', 'фрукт')),
    color VARCHAR(50),
    calories INTEGER CHECK (calories >= 0),
    description TEXT
);
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