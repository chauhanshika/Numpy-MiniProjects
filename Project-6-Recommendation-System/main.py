import numpy as np

ratings = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
    [0, 1, 5, 4]
])

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

target_user = ratings[0]

similarities = []

for i in range(len(ratings)):
    sim = cosine_similarity(target_user, ratings[i])
    similarities.append(sim)

similarities = np.array(similarities)
print("\nUser Similarities:\n", similarities)

most_similar_user = np.argmax(similarities[1:]) + 1
print("\nMost Similar User Index:", most_similar_user)
