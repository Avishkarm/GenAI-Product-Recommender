import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Set TensorFlow environment variable to suppress warnings
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Initialize embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# List of Texts
Product_descs = [
  " United Colors of Benetton Men Check White TShirts",
    "United Colors of Benetton Men Check Green Shirts",
    "Under colors of Benetton Men White Boxer Trunks",
    "Turtle Men Check Red Shirt",
    "United Colors of Benetton Men White Check Shirt",
    "United Colors of Benetton Men Check White Shirts",
    "Wrangler Men Broad Blue Shirt"
]

# Query text
query = "Wrangler Men Broad Blue Shirt"

# Get embedding for the query
query_embedding = embed_model.get_text_embedding(query)

# Store all embeddings and their corresponding texts
all_embeddings = []
for desc in Product_descs:
    # Get embeddings for the current text
    embedding = embed_model.get_text_embedding(desc)
    all_embeddings.append(embedding)

# Convert to numpy arrays for similarity calculation
query_embedding_np = np.array(query_embedding).reshape(1, -1)
all_embeddings_np = np.array(all_embeddings)

# Calculate cosine similarity between query and all texts
similarities = cosine_similarity(query_embedding_np, all_embeddings_np).flatten()

# Create a DataFrame to display results
results = pd.DataFrame({
    'Text': Product_descs,
    'Similarity Score': similarities
})

# Sort by similarity score in descending order
results = results.sort_values('Similarity Score', ascending=False)

print("Query:", query)
print("\nSimilarity Search Results:")
print(results)

# Find the most similar text
most_similar_idx = np.argmax(similarities)
print(f"\nMost similar text: \"{Product_descs[most_similar_idx]}\" with similarity score: {similarities[most_similar_idx]:.4f}")
