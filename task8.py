import json

# dict to json
a = {
    "key1": "value1",
    "key2": "value2",
    "key3": 3,
    "isTrue": True,
    "isFalse": False,
    "isNone": None,
}

# with open('our_test.json', 'w') as fp:
#     fp.write(str(a))
# data = {}
# with open('example.json', 'r') as f:
#     data = f.read()

# print(data)

# eval

# print(eval("1" + "3"))
# print(eval("1 + 3"))
# eval("print(1 + 3)")
# eval("print('1 + 3')")
# b = eval('[1,2,3]')
# print(b)
# print(eval(data))

# json module
# dump
# with open('test_js_module.json', 'w') as outfile:
#     json.dump(a, outfile)
#
# json.dump(a, open('test_js1_module.json', 'w'))

# load
data = json.load(open("example.json"))
print(data)

# dumps, loads

astr = json.dumps(a)
print(astr)

data_loads = json.loads(astr)
print(data_loads)

# intend
print(json.dumps(a, indent=2))

# sort_keys
print(json.dumps(a, sort_keys=True, indent=4))

# import pyyaml