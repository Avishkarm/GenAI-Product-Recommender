import re
import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from getpass import getpass


# Read environment variables
secure_connect_bundle_path = os.getenv('ASTRA_DB_SECURE_CONNECT_BUNDLE')
application_token = os.getenv('ASTRA_DB_TOKEN')

# Define keyspace and vector dimension
ASTRA_KEYSPACE = 'fashion'
#keyspace = "catalog"

v_dimension = 5

cloud_config = {
    'secure_connect_bundle': secure_connect_bundle_path
}

cluster = Cluster(cloud=cloud_config, auth_provider=PlainTextAuthProvider("token", application_token))
session = cluster.connect(keyspace=ASTRA_KEYSPACE)

# Function to load data from Cassandra tables
def load_data_from_cassandra(session):
    query_customers = "SELECT * FROM customers "
    rows_customers = session.execute(query_customers)
    customers = []
    for row in rows_customers:
        customers.append(row)

    return customers

# Main function
def main():
    customers = load_data_from_cassandra(session)
    print(customers)

# Execute the main function
if __name__ == "__main__":
    main()
