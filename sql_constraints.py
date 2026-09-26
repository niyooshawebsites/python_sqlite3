import sqlite3
import pandas as pd
from matplotlib import pyplot as plt

conn = sqlite3.connect('cities.db')
cursor = conn.cursor()

# # delete table
# conn.execute("""DROP TABLE IF EXISTS City;""")

# # create table
# conn.execute("""
#     CREATE TABLE IF NOT EXISTS City(
#         city_id INTEGER PRIMARY KEY,
#         city_name TEXT NOT NULL UNIQUE,
#         country TEXT NOT NULL,
#         population INTEGER,
#         is_capital TEXT DEFAULT 'No',
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     );
# """)

# conn.commit()

# print("Table created successfully!")

# # insert data
# conn.execute("""INSERT INTO City (city_id, city_name, country, population, is_capital) VALUES (1, 'Tokyo', 'Japan', 13960000, 'Yes');""")
# conn.execute("""INSERT INTO City (city_id, city_name, country, population, is_capital) VALUES (2, 'Nairobi', 'Kenya', 4397000, 'Yes');""")
# conn.execute("""INSERT INTO City (city_id, city_name, country, population) VALUES (3, 'Mumbai', 'India', 20667656);""")
# conn.execute("""INSERT INTO City (city_id, city_name, country, population) VALUES (4, 'Sao Paolo', 'Brazil', 12325232);""")
# conn.execute("""INSERT INTO City (city_id, city_name, country, population, is_capital) VALUES (5, 'London', 'UK', 9541000, 'Yes');""")
# conn.execute("""INSERT INTO City (city_id, city_name, country) VALUES (6, 'Sydney', 'Australia');""")

# conn.commit()
# print("Rows inserted successfully!")
# print("\n")

# # testing the Primary key
# try:
#     conn.execute("""INSERT INTO City VALUES (1, 'Cairo', 'Egypt', 21323000, 'Yes');""")
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print("Rejected: ", e)
#     print("The city_id has already been used!!!")
    
# # testing NOT NULL
# try:
#     conn.execute("""INSERT INTO City (city_id, city_name, country, population) VALUES (7, 'Sao Paolo', 'Brazil', 3645000);""")
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print("Rejected: ", e)
#     print("city_name can not be NULL and it must be unique")

# # NULL Values
# try:
#     null_population_records = pd.read_sql("""SELECT * FROM City WHERE population is NULL;""", conn)
#     print(null_population_records)
# except Exception as e:
#     conn.rollback()
#     print("Rejected: ", e)
#     print("Failed to fetch NULL population records")
    
# # NOT NULL Values
# try:
#     null_population_records = pd.read_sql("""SELECT * FROM City WHERE population is NOT NULL;""", conn)
#     print(null_population_records)
# except Exception as e:
#     conn.rollback()
#     print("Rejected: ", e)
#     print("Failed to fetch NULL population records")
    
# # NOT NULL Values with matplotlib
# try:
#     null_population_records = pd.read_sql("""SELECT city_name, population FROM City WHERE population is NOT NULL;""", conn)
#     plt.bar(null_population_records.city_name, null_population_records.population, color="blue")
#     plt.title("Cities-Population")
#     plt.xlabel("Cities")
#     plt.ylabel("Population")
#     plt.show()
# except Exception as e:
#     conn.rollback()
#     print("Rejected: ", e)
#     print("Failed to fetch NULL population records")

# cities not capital
try:
    cities_not_capital = pd.read_sql("""SELECT city_name, country FROM City WHERE is_capital = 'No';""", conn)
    print(cities_not_capital)
    fig, ax = plt.subplots(figsize = (8,3))
    ax.axis("off")
    table = ax.table(
        cellText = cities_not_capital.values,
        colLabels = cities_not_capital.columns,
        loc = "center",
        cellLoc = "center"
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 2)
    

    # All cell borders
    for cell in table.get_celld().values():
        cell.set_edgecolor("gray")

    # Header
    for column in range(len(cities_not_capital.columns)):
        cell = table[(0, column)]
        cell.set_facecolor("steelblue")
        cell.set_text_props(color="white", weight="bold")

    plt.title(
        "Non-Capital Cities",
        fontsize=14,
        fontweight="bold"
    )
    
    plt.show()
except Exception as e:
    conn.rollback()
    print("Rejected: ", e)
    print("No city with capital as 'no'")
    
conn.close()