numbers = [10, 20, 30, 40, 50]

print(numbers[0])  # Accessing elements
print(numbers[-1])  # Negative indexing
print(numbers[1:4])  # Extracting a sublist
print(len(numbers))  # Finding length


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Sorting by alphabet letters

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # Sorting by ascending