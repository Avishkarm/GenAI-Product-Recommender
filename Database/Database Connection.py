# Verify AstraDB Database Connection
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Path to your Secure Connect Bundle
secure_connect_bundle_path = 'secure_connect_bundle_path.zip'

# Your application token
application_token = 'AstraCS:Application_token'

# Setup authentication provider
auth_provider = PlainTextAuthProvider('token', application_token)

# Connect to the Cassandra database using the secure connect bundle
cluster = Cluster(
    cloud={"secure_connect_bundle": secure_connect_bundle_path},
    auth_provider=auth_provider
)
session = cluster.connect()

# Define keyspace
keyspace = "keyspace"

# Set the keyspace
session.set_keyspace(keyspace)

# Verify connection by querying the system.local table
rows = session.execute("SELECT release_version FROM system.local")
for row in rows:
    print(f"Connected to Cassandra, release version: {row.release_version}")

# Print the current keyspace
current_keyspace = session.execute("SELECT keyspace_name FROM system_schema.keyspaces WHERE keyspace_name = %s", [keyspace])
for row in current_keyspace:
    print(f"Connected to keyspace: {row.keyspace_name}")

print("Connected to AstraDB and keyspace successfully!")


