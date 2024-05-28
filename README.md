
---

# AioDatabase Example

This repository provides example code demonstrating how to use the AioDatabase library to manage SQLite and MySQL databases.

## Overview

AioDatabase is a simple database abstraction layer for SQLite and MySQL. This repository contains example scripts and configurations to help you get started quickly.

## Prerequisites

- Python 3.6 or higher
- AioDatabase library
- SQLite or MySQL database

## Installation

First, clone this repository:

```bash
git clone https://github.com/Amitminer/AioDatabase-Example.git
cd AioDatabase-Example
```

Install the required dependencies:

```bash
pip install aiodatabase
```

## Configuration

Modify `config.yml` to match your database configuration.

## Example Scripts

### 1. Connecting to the Database

```python
import asyncio
from aiodatabase import Database as AioDatabase

async def main():
    # Database var
    db = AioDatabase()

    # Creating a localhost connection using SQL
    await db.connect("config.yml", "queries.sql")

    # Your database operations go here

    await db.close()

# Run the main function
asyncio.run(main())
```

### 2. Executing Queries

```python
async def execute_query():
    await db.execute("get_all_cars")
    results = await db.fetchall("get_all_cars")
    for result in results:
        print(result)

# Include this in the main function or another coroutine
await execute_query()
```

### 3. Inserting Data

```python
async def insert_data():
    carsList = [
        ("Nissan GTR", "R35"),
        ("Toyota", "Supra-MK4"),
        ("Lamborghini", "Aventador SVJ"),
        ("Porsche", "911 GT3"),
        ("Tesla Cybertruck", "sucks"),
        ("BMW", "M5 CS"),
    ]

    for car in carsList:
        await db.execute("add_car", car)

# Include this in the main function or another coroutine
await insert_data()
```

### 4. Removing Data

```python
async def remove_car(car_name):
    result = await db.fetchone("get_car_by_name", (car_name,))
    if result:
        car_id = result[0]
        await db.execute("remove_car", (car_id,))
        print(f"Removed car: {car_name}")
    else:
        print(f'Car "{car_name}" not found.')

# Include this in the main function or another coroutine
await remove_car("Tesla Cybertruck")
```

### 5. Fetching Data

```python
async def fetch_data():
    results = await db.fetchall("get_all_cars")
    for result in results:
        print(result)

# Include this in the main function or another coroutine
await fetch_data()
```

### 6. Clearing the Table

```python
async def clear_table():
    await db.execute("clear_cars_table")

# Include this in the main function or another coroutine
await clear_table()
```

### 7. Complete Example

```python
import asyncio
from aiodatabase import Database as AioDatabase

async def main():
    # Database var
    db = AioDatabase()

    # Creating a localhost connection using SQL
    await db.connect("config.yml", "queries.sql")

    # Clearing the cars table
    await clear_table()

    # Inserting cars into the database
    await insert_data()

    # Remove Tesla Cybertruck
    await remove_car("Tesla Cybertruck")

    # Fetch and print data
    await fetch_data()

    await db.close()

async def clear_table():
    await db.execute("clear_cars_table")

async def insert_data():
    carsList = [
        ("Nissan GTR", "R35"),
        ("Toyota", "Supra-MK4"),
        ("Lamborghini", "Aventador SVJ"),
        ("Porsche", "911 GT3"),
        ("Tesla Cybertruck", "EV"),
        ("BMW", "M5 CS"),
    ]
    for car in carsList:
        await db.execute("add_car", car)

async def remove_car(car_name):
    result = await db.fetchone("get_car_by_name", (car_name,))
    if result:
        car_id = result[0]
        await db.execute("remove_car", (car_id,))
        print(f"Removed car: {car_name}")
    else:
        print(f'Car "{car_name}" not found.')

async def fetch_data():
    results = await db.fetchall("get_all_cars")
    for result in results:
        print(result)

# Run the main function
asyncio.run(main())
```

## Sample Configuration Files

### config.yml

```yaml
database:
  # Specify the database type: either "sqlite" or "mysql".
  type: sqlite

  # Configuration for SQLite database
  sqlite:
    # The name of the SQLite database file. 
    # You can provide an absolute path or just the file name if it is located in the data folder.
    file: data.sqlite

  # Configuration for MySQL database
  mysql:
    host: 127.0.0.1
    # It's recommended not to use the "root" user for security reasons.
    username: root
    password: ""
    schema: your_schema
```

### queries.sql

```sql
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

-- #{ clear_cars_table
DELETE FROM cars;
-- #}

-- #{ get_all_cars
SELECT name, model FROM cars;
-- #}

-- #{ get_car_by_name
SELECT id FROM cars WHERE name = ?;
-- #}
```

## Running the Example

To run the test script:

```bash
python test_script.py
```

This will demonstrate the basic operations of connecting to the database, inserting data, fetching data, and removing data using AioDatabase.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

---
