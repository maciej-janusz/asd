from utils import *


def most_common(arr):
    lead = 0
    cnt = 0
    for i in range(len(arr)):
        if cnt == 0:
            lead = arr[i]
            cnt += 1
        else:
            if lead == arr[i]:
                cnt += 1
            else:
                cnt -= 1
    if cnt == 0 or arr.count(lead)/len(arr) < 0.5:
        return None
    return lead

arr = randomArray(10, min=0, max=3)
print(most_common(arr))