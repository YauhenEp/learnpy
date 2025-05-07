import csv
import re
import docx

def read_docx_file(file_name):
    doc = docx.Document(file_name)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def count_word(text):
    word_dict = {}
    for raw in text.split('\n'):
        for word in raw.split(' '):
            lower_word = word.lower()
            print(lower_word)
            if lower_word in word_dict:
                word_dict[lower_word] += 1
            else:
                word_dict[lower_word] = 1
    print(word_dict)
    return word_dict

def write_csv(word_dict):
    with open('test_word_csv.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in word_dict.items():
            writer.writerow([key, value])

def write_word_count(file_name):
    docx_text = read_docx_file(file_name)
    word_dict = count_word(docx_text)
    write_csv(word_dict)

# write_word_count('news_list.docx')

def write_letter_count(file_name):
    text = read_docx_file(file_name)
    letter_list = count_letter(text)
    write_letter_csv(letter_list)

def count_letter(text):
    letter_object_list = []
    letter_list = list(text)
    for letter in letter_list:
        lower_letter = letter.lower()
        letter_count = -1
        count_uppercase = -1
        all_letters = 0
        for let in letter_list:
            if let.lower() == letter:
                letter_count += 1
            if let.upper() == letter:
                count_uppercase += 1
            all_letters += 1
        letter_object_list.append({
            'letter': lower_letter,
            'count_all': letter_count,
            'count_uppercase': letter_count,
            'percentage': letter_count / all_letters * 100
        })
    print(letter_object_list)
    return letter_object_list

def write_letter_csv(letter_list):
    with open('test_letter_csv.csv', 'w', newline='') as csvfile:
        headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for dict_letter in letter_list:
            writer.writerow({
                'letter': dict_letter['letter'],
                'count_all': dict_letter['count_all'] ,
                'count_uppercase': dict_letter['count_uppercase'] ,
                'percentage': dict_letter['percentage']
            })
write_letter_count('news_list.docx')

