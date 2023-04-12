file_path = "C:\data\class_colon.txt"

data_dict = {}

with open(file_path, "r") as f:
    for line in f:
        id, *data = line.strip().split(":")
        data_dict[id] = tuple(data)

# print(data_dict)
print(data_dict)
for k in data_dict:
    print(k, data_dict[k])

smax = 0; midx = 0
for k in data_dict:
    if int(data_dict[k][1]) > smax:
        smax = int(data_dict[k][1])
        midx = k
print('Information on the maximum courses you take = ', midx, '', data_dict[midx])

snumList = []
for k in data_dict:
    idata = int(data_dict[k][1])
    snumList.append(idata)

print('=', max(snumList))