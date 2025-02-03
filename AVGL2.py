def OrderTheStudentMark(marksWithoutOrder,numOfStudent):
    # Ordering By No Fail Highest Mark
    # Ordering By Less Fail Highest Mark
    # if all is the same then order by the name in ascending order (remaining)
    NoFailStudents = []
    LessFailStudents = []

    orderedMarks = {}
    for key,value in marksWithoutOrder.items():
        if value[0][1] == 0:
            NoFailStudents.append(key)
        elif value[0][1] != 0:
            LessFailStudents.append([key,value[0][1]])


    while NoFailStudents.__len__() > 0: 
        highestMark = 0
        highestMarkIndex = 0
        for z in range(NoFailStudents.__len__()):
            thisStudentDic = marksWithoutOrder[NoFailStudents[z]] 

            if thisStudentDic[0][0] > highestMark:
                highestMark = thisStudentDic[0][0]
                highestMarkIndex = z
        orderedMarks[NoFailStudents[highestMarkIndex]] = marksWithoutOrder[NoFailStudents[highestMarkIndex]][0] 
        NoFailStudents.pop(highestMarkIndex)
    
    while LessFailStudents.__len__() > 0:

        sameCoursesFound = False
        for z in range(LessFailStudents.__len__()):
            if z == 0:
                minimalCreditFail = LessFailStudents[z][1]
                minimalCreditFailIndex = z
                thisStudentDiC = marksWithoutOrder[LessFailStudents[minimalCreditFailIndex][0]] 
            elif LessFailStudents[z][1] < minimalCreditFail:
                minimalCreditFail = LessFailStudents[z][1]
                minimalCreditFailIndex = z
                thisStudentDiC = marksWithoutOrder[LessFailStudents[minimalCreditFailIndex]] 
        for x in range(LessFailStudents.__len__()):
            if x == minimalCreditFailIndex:
                continue
            elif LessFailStudents[z][1] == minimalCreditFail:
                sameCoursesFound = True
                break
        if sameCoursesFound:
            sameStudents = []
            for j in range(LessFailStudents.__len__()):
                if j == minimalCreditFailIndex:
                    continue
                elif LessFailStudents[j][1] == minimalCreditFail:
                    sameStudents.append([LessFailStudents[j][0],j])
            while sameStudents.__len__() > 0:
                thishighestMark = 0
                thishighestMarkIndex = 0
                for z in range(sameStudents.__len__()):
                    thisStudentDiC = marksWithoutOrder[sameStudents[z][0]] 
                    if thisStudentDiC[0][0] > thishighestMark:
                        thishighestMark = thisStudentDiC[0][0]
                        thishighestMarkIndex = z
                orderedMarks[sameStudents[thishighestMarkIndex][0]] = marksWithoutOrder[sameStudents[z][0]] 
                LessFailStudents.pop(sameStudents[thishighestMarkIndex][1])
                sameStudents.pop(thishighestMarkIndex)
                
        else:
            orderedMarks[LessFailStudents[minimalCreditFailIndex][0]] = marksWithoutOrder[LessFailStudents[minimalCreditFailIndex][0]][0]
            LessFailStudents.pop(minimalCreditFailIndex)
    return orderedMarks

for _ in range(int(input())):
    numOfCourses = int(input())
    courses = [ z.split() for z in input().split(",")]
    numOfStudent = int(input())
    studentMarksWithoutOrdering = {}
    for i in range(numOfStudent):
        thisStudentMark = list(map(str,input().split(",")))
        studentMarksWithoutOrdering[thisStudentMark[0]] = []
        thisStudentAverage = round(sum([(int(thisStudentMark[j]) * int(courses[j-1][1])) for j in range(1,thisStudentMark.__len__())]) / sum([int(courses[n][1])for n in range(courses.__len__())]),2)
        studentPassedArray = [[True, 0] if (int(thisStudentMark[q]) * int(courses[q-1][1])) > (100 * int(courses[q-1][1]) * 0.5) else [False, int(courses[q-1][1])] for q in range(1, thisStudentMark.__len__())]
        numOfFailedCourses = sum([studentPassedArray[c][1] for c in range(studentPassedArray.__len__())])
        studentFailed = "false" if numOfFailedCourses  <  sum([int(courses[n][1]) for n in range(courses.__len__())]) * 0.5 else "true"
        studentMarksWithoutOrdering[thisStudentMark[0]].append([thisStudentAverage,numOfFailedCourses,studentFailed])
    
    orderedStudentMarks = OrderTheStudentMark(studentMarksWithoutOrdering,numOfStudent)
    for key,value in orderedStudentMarks.items():
        print(f"{key},{','.join(str(v) for v in value)}")