listOneDim = [10,20,30,40]

listTwoDim = [["Tom",10],["John",20],["Linda",30],["cici",40]]

print(listTwoDim)

track = int(input())
for time in range(track):
    add = input()
    add2 = input()
    listTwoDim.append([add, int(add2)])
for time in range(track):
    print(listTwoDim[time+4])

if ["Tom",10] in listTwoDim:
    print("very true")

for item in listTwoDim:     
    if "a" in item:
        print("yes")