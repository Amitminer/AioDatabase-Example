import asyncio
from aiodatabase import Database as AioDatabase

async def main():
    # Database var
    db = AioDatabase()

    # Creating a localhost connection using SQL
    await db.connect("config2.yml", "queries.sql")

    # Clearing the cars table
    await db.execute("clear_cars_table")

    # Inserting cars into the database
    carsList = [
        ("Nissan GTR", "R35"),
        ("Toyota", "Supra-MK4"),
        ("Lamborghini", "Aventador SVJ"),
        ("Porsche", "911 GT3"),
        ("Tesla Cybertruck", "sucks"),
        ("BMW", "M5 CS"),
    ]

    # Inserting each car into the database
    for car in carsList:
        await db.execute("add_car", car)

    # Function to remove a car by name
    async def remove_car(car_name):
        result = await db.fetchone("get_car_by_name", (car_name,))
        if result:
            car_id = result[0]
            await db.execute("remove_car", (car_id,))
            print(f"Removed car: {car_name}")
        else:
            print(f'Car "{car_name}" not found.')

    # Remove Tesla Cybertruck
    await remove_car("Tesla Cybertruck")

    # Fetch and print data
    print("All Cars:")
    results = await db.fetchall("get_all_cars")
    for result in results:
        print(result)

    await db.close()


# Run the main function
asyncio.run(main())
