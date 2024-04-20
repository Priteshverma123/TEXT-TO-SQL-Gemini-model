import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("district.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

# Create the district table if not exists
table_info = """
CREATE TABLE IF NOT EXISTS district (
    name VARCHAR(50),
    population INT,
    sex_ratio FLOAT,
    literacy_rate FLOAT
);
"""
cursor.execute(table_info)
district_records = [
    ('North Delhi', 1500000, 0.96, 0.82),
    ('South Mumbai', 2000000, 1.02, 0.85),
    ('East Kolkata', 1800000, 1.05, 0.78),
    ('West Chennai', 1700000, 0.98, 0.83),
    ('Central Bengaluru', 2200000, 1.01, 0.87),
    ('North Hyderabad', 1600000, 0.99, 0.79),
    ('South Ahmedabad', 1900000, 1.03, 0.84),
    ('East Pune', 2100000, 1.04, 0.86),
    ('West Jaipur', 1400000, 0.97, 0.81),
    ('Central Lucknow', 1800000, 1.02, 0.88),
    ('North Patna', 1300000, 0.95, 0.77),
    ('South Kanpur', 2000000, 1.01, 0.83),
    ('East Nagpur', 1500000, 0.98, 0.82),
    ('West Visakhapatnam', 1700000, 1.05, 0.86),
    ('Central Indore', 2100000, 1.03, 0.87),
    ('North Thane', 1400000, 0.96, 0.81),
    ('South Bhopal', 1900000, 1.02, 0.85),
    ('East Agra', 1600000, 1.01, 0.79),
    ('West Vadodara', 1800000, 1.04, 0.86),
    ('Central Nashik', 2200000, 1.05, 0.88),
    ('North Nagaland', 1200000, 0.93, 0.76),
    ('South Kashmir', 2300000, 1.07, 0.89),
    ('East Assam', 1700000, 1.01, 0.82),
    ('West Punjab', 2000000, 1.06, 0.87),
    ('Central Gujarat', 2100000, 1.03, 0.84),
    ('North Haryana', 1500000, 0.97, 0.81),
    ('South Bihar', 1900000, 1.02, 0.86),
    ('East Odisha', 1800000, 1.04, 0.85),
    ('West Madhya Pradesh', 2200000, 1.05, 0.88),
    ('Central Rajasthan', 1700000, 1.01, 0.82),
    ('North Uttarakhand', 1300000, 0.96, 0.78),
    ('South Himachal Pradesh', 2000000, 1.02, 0.87),
    ('East Jharkhand', 1600000, 0.99, 0.83),
    ('West Chhattisgarh', 1900000, 1.03, 0.85),
    ('Central Telangana', 2100000, 1.04, 0.86),
    ('North Karnataka', 1400000, 0.97, 0.80),
    ('South Tamil Nadu', 2300000, 1.06, 0.88),
    ('East Kerala', 1700000, 1.01, 0.84),
    ('West Goa', 2000000, 1.05, 0.87),
    ('Central Andhra Pradesh', 2200000, 1.03, 0.85),
    ('North Maharashtra', 1500000, 0.96, 0.79),
    ('South Punjab', 1900000, 1.02, 0.86),
    ('East West Bengal', 1800000, 1.04, 0.85),
    ('West Uttar Pradesh', 2100000, 1.05, 0.88),
    ('Central Bihar', 1700000, 1.01, 0.83),
    ('North Jammu and Kashmir', 1300000, 0.97, 0.80),
    ('South Sikkim', 2000000, 1.03, 0.86),
    ('East Arunachal Pradesh', 1600000, 1.00, 0.82),
    ('West Mizoram', 1900000, 1.02, 0.84),
    ('Central Manipur', 2100000, 1.04, 0.87)
]



# ## Disspaly ALl the records
cursor.executemany("INSERT INTO district VALUES (?, ?, ?, ?)", district_records)

print("The inserted records are")
data=cursor.execute('''Select * from district''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()