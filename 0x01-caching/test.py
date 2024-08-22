#!/usr/bin/python3

a_dict = {"a": 1, "b": 2, "c": 3, "d": 4}

s_dict = dict(sorted(a_dict.items(), key=lambda item: item[1], reverse=True))
print(s_dict.popitem()[0])