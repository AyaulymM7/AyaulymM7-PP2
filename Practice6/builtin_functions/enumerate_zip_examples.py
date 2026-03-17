names = ["Ali", "Aruzhan", "Dana"]
scores = [85, 90, 78]

# enumerate
for i, name in enumerate(names):
    print(i, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

# sorted
nums = [5, 2, 9, 1]
print("Sorted:", sorted(nums))

# type conversion
x = "10"
print(type(x))
x = int(x)
print(type(x))