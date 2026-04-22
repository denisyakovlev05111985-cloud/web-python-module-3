# d= {
#     "a":1
#     "b":[1,2,3]
#     "bool"
# }

# keys= ["a","b","c"]
# d= dict.fromkeys(keys,1)

# print(d["d"])

# print(d.get("a"), d.get("d"))

# value= d.setdefault("e",0)
# print(value)

# fr= ["apple", "banana", "apple"]
# d= {}
# for word in fr:
#     d.setdefault(word, 0)
#     d[word] +=1

# print(d)

# d= {"a": 1}
# d.update({"a": 2,"b": 3})
# d.update(c= 4, d= 5)

# d.pop("d")
# del d["c"]
# # del d
# key, value = d.popitem()
# d.clear()
# print(d)

# d_1= {"a": 1}
# d_1.update({"a": 2,"b": 3})
# d_1.update(c= 4, d= 5)

# if "e" not in d_1:
#     print("ok")

# print(d_1.keys(), d_1.values())

# print(d_1.items())

# for key, value in d_1.items():
#     print(f"{key}={value}")