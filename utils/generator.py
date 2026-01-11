import random

def mongodb_generator(collection_name):

    total_entries = collection_name.count_documents({})
    random_entry_id = random.randint(1, total_entries)

    while True:
        random_entry = collection_name.find_one({"id": random_entry_id})

        yield random_entry

        random_entry_id += 1
        if random_entry_id > total_entries:
            random_entry_id = 1