progresses=[93, 30, 55]		
speeds =[1, 30, 5]


def check(data1, data2):
    if data1 and data1[0] >= 100:
        del data1[0]
        del data2[0]
        return 1+ check(data1,data2)
    else:
        return 0



def solution(progresses, speeds):
    answer = []
    while progresses:
        progresses = [x+y for x,y in zip(progresses,speeds)]  
        complete_work=check(progresses,speeds)   
        if complete_work >0:
            answer.append(complete_work)
    return answer

