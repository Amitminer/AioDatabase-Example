-- #! sqlite

-- #{ create_table
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    model TEXT
);
-- #}

-- #{ add_car
INSERT INTO cars (name, model) VALUES (?, ?);
-- #}

-- #{ remove_car
DELETE FROM cars WHERE id = ?;
-- #}

-- #{ update_car
UPDATE cars SET name = ?, model = ? WHERE id = ?;
-- #}

-- #{ get_all_cars
SELECT name, model FROM cars;
-- #}

-- #{ get_car_by_id
SELECT id, name, model FROM cars WHERE id = ?;
-- #}

-- #{ get_car_by_name
SELECT id, name, model FROM cars WHERE name = ?;
-- #}

-- #{ clear_cars_table
DELETE FROM cars;
-- #}
