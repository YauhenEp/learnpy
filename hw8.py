import json

class JsonWriter(object):
    def __init__(self, *filename_list):
        self.filenameList = filename_list

    def generate_json(self):
        json_text = ''
        for filename in self.filenameList:
            print('filename --- ', filename)
            data = json.load(open(filename))
            json_text += json.dumps(data, indent=4)
        return json_text