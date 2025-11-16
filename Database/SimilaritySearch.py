import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

os.system('cls' if os.name == 'nt' else 'clear')

# Read environment variables
secure_connect_bundle_path = os.getenv('ASTRA_DB_SECURE_CONNECT_BUNDLE')
application_token = os.getenv('ASTRA_DB_TOKEN')

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

# Define keyspace and vector dimension
keyspace = "catalog"
v_dimension = 5

# Function to get productdescvector by productid
def get_productdescvector(productid):
    query = f"SELECT productdescvector FROM {keyspace}.ProductDescVectors WHERE productid = {productid}"
    row = session.execute(query).one()
    if row:
        return row.productdescvector
    else:
        raise ValueError(f"Product with id {productid} not found")

# Example productid to find similar matches
productid = 1

# Fetch the productdescvector for the given productid
productdescvector = get_productdescvector(productid)

# Query to find similar matches using the fetched productdescvector
ann_query = (
    f"SELECT ProductDesc, similarity_cosine(ProductDescVector, {productdescvector}) as similarity FROM {keyspace}.ProductDescVectors "
    f"ORDER BY ProductDescVector ANN OF {productdescvector} LIMIT 2"
)
for row in session.execute(ann_query):
    print(f"[{row.productdesc}\" (sim: {row.similarity:.4f})")

print("Data with similar match.")






