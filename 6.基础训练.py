print(bool("Hello"))
print(bool(10))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
x = 200
print(isinstance(x, int))

print("-----------------------------------------")

"""thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist = ["apple", "banana", "cherry"]
thistuple = ("apple", "banana", "cherry")
print(thistuple)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
thisset = {"apple", "banana", "cherry"}
print(thisset)"""


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)"""

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
