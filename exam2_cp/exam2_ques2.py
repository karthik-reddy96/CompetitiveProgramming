def queueReconstruction(personList):
    personList=sorted(personList)
    personList.reverse()
    
    for i in range(len(personList)-1):
        if(personList[i][0]==personList[i+1][0]):
            if(personList[i][1]>personList[i+1][1]):
                personList[i],personList[i+1]=personList[i+1],personList[i]
                i=0
  
    answer = []
    for person in personList:
        answer.insert(person[1], person)
       
    return answer
   

print (queueReconstruction([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
print(queueReconstruction([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]]))
print(queueReconstruction([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]))
