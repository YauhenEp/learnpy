import random
import string

number_keys = random.randint(1, 26)
keys = random.sample(string.ascii_lowercase, number_keys)
random_dict = {key: random.randint(1, 100) for key in keys}
# print(random_dict)
num_dicts = random.randint(2, 10)
final_dict = []
for _ in range(num_dicts):
    number_keys = random.randint(1, 26)
    keys = random.sample(string.ascii_lowercase, number_keys)
    random_dict = {key: random.randint(1, 100) for key in keys}
    final_dict.append(random_dict)
print(final_dict)

new_dict = {}
key_tracking = {}
for extracted_dict_index, extracted_dict in enumerate(final_dict):
    print(extracted_dict, extracted_dict_index)
    for key, value in extracted_dict.items():
        print(key, value)
        if key in new_dict:
            print(new_dict[key])
            if value > new_dict[key]:
                new_dict[key] = value
                key_tracking[key] = f"{key}_{extracted_dict_index}"
        else:
            new_dict[key] = value
            key_tracking[key] = key
renamed_new_dict = {key_tracking[key]: value for key, value in new_dict.items()}
print(renamed_new_dict)