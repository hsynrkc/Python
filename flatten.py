l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newlist = []
def flatten(x):
    for i in x:
        if isinstance(i, list):
            flatten(i)
        else:
            newlist.append(i)

flatten(l)
print(newlist)