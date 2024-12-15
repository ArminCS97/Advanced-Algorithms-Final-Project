import numpy as np
import numpy.random
from faker import Faker
from faker.exceptions import UniquenessException

from bst_frequencies import BSTFrequencySearch
from bst_lexicographical import BSTLexicographicalSearch
from linear import LinearSearch
from obst import OBSSearch
import pickle
import random


def generate_data(n_words):
    faker = Faker('en_US')

    # Generate random unique words
    words = []
    for _ in range(n_words):
        try:
            words.append(faker.unique.word())
        except UniquenessException:
            faker.unique.clear()  # Reset the unique constraints
            words.append(faker.unique.word())

    # Generate random frequencies
    frequencies_raw = np.random.random(n_words)
    dummy_frequencies_raw = np.random.random(n_words + 1)

    # Normalize to ensure total sum = 1
    total_sum = 1.0
    frequencies_portion = 0.7  # 70% for successful searches
    dummy_frequencies_portion = 0.3  # 30% for unsuccessful searches

    frequencies = frequencies_raw / frequencies_raw.sum() * (total_sum * frequencies_portion)
    dummy_frequencies = dummy_frequencies_raw / dummy_frequencies_raw.sum() * (total_sum * dummy_frequencies_portion)

    # Sort words and frequencies lexicographically
    sorted_data = sorted(zip(words, frequencies))
    sorted_words, sorted_frequencies = zip(*sorted_data)

    return list(sorted_words), list(sorted_frequencies), dummy_frequencies


if __name__ == "__main__":
    n_words = 3_000
    words, frequencies, dummy_frequencies = generate_data(n_words)

    assert abs(sum(frequencies) + sum(dummy_frequencies) - 1) < 1e-9, "Frequencies do not sum to 1"

    linear_search = LinearSearch(words)
    bst_frequencies_search = BSTFrequencySearch(words=words, frequencies=frequencies)
    bst_lexicographical_search = BSTLexicographicalSearch(words)
    obst_search = OBSSearch(words, frequencies, dummy_frequencies)

    linear_search.construct()
    bst_frequencies_search.construct()
    bst_lexicographical_search.construct()
    obst_search.construct()

    # Test the OBST with a few words
    test_words = words[:10]  # Test the first 10 words
    for word in test_words:
        assert obst_search.search(word), f"Search failed for {word}"
        assert linear_search.search(word), f"Search failed for {word}"
        assert bst_lexicographical_search.search(word), f"Search failed for {word}"
    for freq in frequencies[:10]:
        assert bst_frequencies_search.search('word', freq), f"Search failed for {freq}"

    print("All tests passed successfully.")

    d = {
        "linear_search": linear_search,
        "bst_frequencies_search": bst_frequencies_search,
        "bst_lexicographical_search": bst_lexicographical_search,
        "obst_search": obst_search,
        'random_words': random.sample(words, 10),
        'random_frequencies': random.sample(frequencies, 10)
    }

    # Pickle the dictionary
    with open("search_objects.pkl", "wb") as f:
        pickle.dump(d, f)

    print("Search objects have been successfully pickled.")
