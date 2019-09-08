d={"name": "Armen", "age": 15, "grades": [10, 8, 8, 4, 6, 7]}
sum=0
for x in d["grades"]:
    sum+=x
if sum/len(d["grades"])>7:
    print("Good job")
else:
    print("You need to work more")