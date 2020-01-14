file = open("Task1_actual_pred_labels.txt")

lines = file.readlines()
file.close()
m = 0

act = []
pred = []
g =set()
for i in lines:
    i = i.strip().split()
    a = int(i[0])
    p = int(i[1])
    g.add(a)
    g.add(p)
    act.append(a)
    pred.append(p)

g = list(g)
g = sorted(g)
file = open("data/tags.txt")
t = file.readlines()
tag = {}

for i,key in enumerate(t):
    tag[i] = key.strip()

fm = open("Mang_MTL_mayank_labels.txt", "w")

for i in lines:
    i = i.strip().split()
    a = int(i[0])
    p = int(i[1])
    if(a != p):
        fm.write(tag[a] + " " + tag[p] + "\n")

lst = []
for i in tag:
    if(i not in g):
        lst.append(i)
for i in lst:
    del tag[i]
from sklearn.metrics import classification_report
print(classification_report(act, pred, target_names = tag.values()))

