import os
import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Path to your Secure Connect Bundle
secure_connect_bundle_path = '<Your local drive path>/secure-connect-taskgenai.zip'
# Your application token
application_token = 'AstraCS:NExTIcHNSrxqIDUHPZGvGOlK:997f68ea875dcebf51e3eccf3fead5602d039cd886d122a2b9f73bb48fe1e48d'

KEYSPACE = "fashiondb"  # Replace with your actual keyspace name

# Read environment variables
# secure_connect_bundle_path = os.getenv('ASTRA_DB_SECURE_CONNECT_practice')
# application_token = os.getenv('ASTRA_DB_TOKEN_practice')

# Debug prints to check environment variables
print(f"Secure Connect Bundle Path: {secure_connect_bundle_path}")
print(f"Application Token: {application_token}")

# Check if the environment variables are loaded correctly
if not secure_connect_bundle_path or not os.path.exists(secure_connect_bundle_path):
    raise FileNotFoundError(f"Secure connect bundle not found at path: {secure_connect_bundle_path}")

if not application_token:
    raise ValueError("Application token not found in environment variables")

# Connect to the Cassandra database using the secure connect bundle
session = Cluster(
    cloud={"secure_connect_bundle": secure_connect_bundle_path},
    auth_provider=PlainTextAuthProvider("token", application_token),
).connect()


# Use the keyspace
session.set_keyspace('fashiondb')

# Create a table
session.execute("CREATE TABLE IF NOT EXISTS ProductImageVectors2 (ProductId int PRIMARY KEY, ProductDesc text, price int);")

# Insert data
session.execute("INSERT INTO ProductImageVectors2 (ProductId, ProductDesc, price) VALUES (2, 'Proline WoMen Cream-Coloured Polo T-Shirt', 3400);")

# Select data
results = session.execute("SELECT * FROM ProductImageVectors2 WHERE ProductId = 2;")
for row in results:
    print(row)

df = pd.read_sql_query(results, session)
print(df)


