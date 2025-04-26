import random
import string

def get_random_string(minimum ,length):
    return random.randint(minimum, length)

def generate_random_dict():
    number_keys = get_random_string(1, 26)
    keys = random.sample(string.ascii_lowercase, number_keys)
    return {key: get_random_string(1, 100) for key in keys}


def generate_dict(minimum, maximum):
    num_dicts = get_random_string(minimum, maximum)
    final_dict = []
    for _ in range(num_dicts):
        number_keys = random.randint(1, 26)
        keys = random.sample(string.ascii_lowercase, number_keys)
        random_dict = {key: random.randint(1, 100) for key in keys}
        final_dict.append(random_dict)
    return final_dict

def renamed_dict(example_dict):
    new_dict = {}
    key_tracking = {}
    for extracted_dict_index, extracted_dict in enumerate(example_dict):
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
    return renamed_new_dict

text = """homEwork:
 tHis iz your homeWork, copy these Text to variable.


 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.


 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.


 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def get_space_number(work_text):
    space_count  = 0
    for i in range(len(work_text)):
        if work_text[i] == ' ' or work_text[i] == '\n':
            space_count += 1
    print(space_count)

def fix_mistakes(work_text):
    return work_text.replace(' iZ ', ' is ').replace(' iz ', ' is ').replace(' Iz ', ' is ')

def format_text(work_text):
    formated_text = work_text.lower().split('\n ')
    for i in range(len(formated_text)):
        formated_text[i] = formated_text[i].capitalize()
    return '\n'.join(formated_text)

def normalize_text(work_text):
    fixed_text = fix_mistakes(work_text)
    return format_text(fixed_text)