import io
import os
import base64
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

# AstraDB details from environment variables

# Path to your Secure Connect Bundle
secure_connect_bundle_path = '<Your local drive path>/secure-connect-taskgenai.zip'

# Your application token
application_token = 'AstraCS:NExTIcHNSrxqIDUHPZGvGOlK:997f68ea875dcebf51e3eccf3fead5602d039cd886d122a2b9f73bb48fe1e48d'

KEYSPACE = "fashiondb"  # Replace with your actual keyspace name


def connect_astra():
    cloud_config = {
        'secure_connect_bundle': secure_connect_bundle_path
    }

    auth_provider = PlainTextAuthProvider('token', application_token)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect(KEYSPACE)
    
    database_name = "TaskGenAI"
    print(f"Connected to database: {database_name}, Keyspace: {KEYSPACE}")
    return session, database_name, KEYSPACE

# Initialize AstraDB session and get database details
session, database, keyspace = connect_astra()
print(f"Using database: {database}, Keyspace: {keyspace}")
