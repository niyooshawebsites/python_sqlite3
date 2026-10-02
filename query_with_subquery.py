import sqlite3
import pandas as pd

# Part 1: Build and explore tables

conn = sqlite3.connect("experiment.db")

conn.execute(
    """CREATE TABLE IF NOT EXISTS experiment (
        experiment_id INTEGER PRIMARY KEY,
        experiment_name TEXT NOT NULL,
        subject TEXT NOT NULL,
        duration_mins INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""
)

conn.execute("""
    CREATE TABLE IF NOT EXISTS material (
        material_id INTEGER PRIMARY KEY,
        experiment_id INTEGER NOT NULL,
        item TEXT NOT NULL,
        quantity_g INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# conn.executemany("""
#     INSERT INTO experiment (experiment_id, experiment_name, subject, duration_mins) VALUES (?, ?, ?, ?)""", [
#         (1, 'Volcano Reaction', 'Chemistry', 20),
#         (2, 'Plant Growth Test', 'Biology', 15),
#         (3, 'Magnet Strength Test', 'Physics', 45),
#         (4, 'Light Reflection', 'Physics', 30),
#         (5, 'Water Filtration', 'Earth Science', 10),
#     ])

# conn.executemany("""INSERT INTO material (material_id, experiment_id, item, quantity_g) VALUES(?, ?, ?, ?)""", [
#         (1, 1, 'Baking Soda', 100),
#         (2, 1, 'Vinegar', 150),
#         (3, 2, 'Soil', 250),
#         (4, 2, 'Seeds', 20),
#         (5, 3, 'Bar Magnet', 80),
#         (6, 4, 'Mirror', 120),
#         (7, 5, 'Sand', 150),
#         (8, 5, 'Filter Paper', 10),
#     ])

conn.commit()

print("Experiment table: ")
print(pd.read_sql("""SELECT * FROM experiment""", conn))
print("\n")

print("Material table: ")
print(pd.read_sql("""SELECT * FROM material""", conn))
print("\n")

# Part 2 Alias for columns
col_alias = pd.read_sql("SELECT experiment_name AS activity, subject AS topic, duration_mins AS time_mins FROM experiment", conn)
print(col_alias)
print("\n")

# Part3 Alias for tables
tbl_alias = pd.read_sql("SELECT e.experiment_name AS activity, m.item, m.quantity_g AS grams FROM experiment AS e INNER JOIN material AS m ON e.experiment_id = m.experiment_id", conn)

print(tbl_alias)
print("\n")

# part 4 Subquery with IN
large_materials = pd.read_sql("SELECT experiment_name AS activity, subject AS topic FROM experiment WHERE experiment_id IN (SELECT experiment_id FROM material WHERE quantity_g > 100)", conn)

print("Subquery with IN --experiments with material over 100g")
print(large_materials)
print("\n")

# ---- PART 5: Subquery with = ----

quickest = pd.read_sql(
    "SELECT experiment_name AS activity, duration_mins AS time "
    "FROM experiment "
    "WHERE duration_mins = (SELECT MIN(duration_mins) FROM experiment)",
    conn
)

print("Subquery with = -- the quickest experiment:")
print(quickest)

conn.close()