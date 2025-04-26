from hw4 import normalize_text

class From_File:
    def __init__(self, *filename_list):
        self.filenameList = filename_list

    def generate_file_text(self):
        all_text = ''
        for filename in self.filenameList:
            with open(filename) as f:
                text = f.read()
                formatted_text = normalize_text(text)
                all_text += formatted_text
                print(formatted_text)
        return all_text


# ff = From_File(['test_module.py', 'tasks.py'])
# ff.generate_file_text()