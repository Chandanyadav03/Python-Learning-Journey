marks = {
    "chandan": 98,
    "yadav": 93,
    "alice": 80,
     0 : "bob"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"chandan" : 99, "vipul" : 85})
print(marks)

print(marks.get("chandan2")) # Get none if key is not present
print(marks["chandan2"]) # print(marks["unknown"]) # KeyError if key is not present