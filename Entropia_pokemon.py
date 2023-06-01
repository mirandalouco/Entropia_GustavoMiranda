import math

# Define the types of Pokémon and their quantities
types = {
    'Normal': 24,
    'Fire': 14,
    'Water': 35,
    'Electric': 9,
    'Grass': 15,
    'Ice': 5,
    'Fighting': 9,
    'Poison': 36,
    'Ground': 14,
    'Flying': 23,
    'Psychic': 18,
    'Bug': 14,
    'Rock': 12,
    'Ghost': 4,
    'Dragon': 4
}

# Count the number of Pokémon types
num_types = len(types)

# Calculate the total number of Pokémon
total_pokemon = sum(types.values())

# Calculate the probabilities of each Pokémon type
probabilities = {type_name: count / total_pokemon for type_name, count in types.items()}

# Calculate the entropy
entropy = -sum(probability * math.log2(probability) for probability in probabilities.values())

#Calculate the max entropy
m_entropy = math.log2(num_types)

# Print the entropy
print(f"The entropy of Pokémon types is: {entropy:.4f}")
print(f"The Max Entropy of Pokémon type is: {m_entropy:.4f}")
