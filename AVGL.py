for _ in range(int(input())):
    numOfCourses = int(input())
    courses = [z.split() for z in input().split(",")]
    numOfStudent = int(input())

    studentMarksWithoutOrdering = []

    for i in range(numOfStudent):
        thisStudentMark = list(map(str, input().split(",")))
        thisStudentName = thisStudentMark[0]

        totalCredits = sum([int(courses[j][1]) for j in range(len(courses))])
        earnedCredits = 0
        for j in range(1, len(thisStudentMark)):
            if int(thisStudentMark[j]) >= 50:
                earnedCredits += int(courses[j-1][1])

        thisStudentAverage = round(sum([(int(thisStudentMark[j]) * int(courses[j-1][1]))
                                   for j in range(1, len(thisStudentMark))]) / totalCredits, 2)

        failedCourses = len([int(x)
                            for x in thisStudentMark[1:] if int(x) < 50])
        failedSem = "true" if failedCourses > totalCredits//2 else "false"

        thisStudentData = [thisStudentName,
                           thisStudentAverage, failedCourses, failedSem]
        studentMarksWithoutOrdering.append(thisStudentData)

    studentMarksWithoutOrdering.sort(key=lambda x: (x[2], -x[1], x[0]))

    for student in studentMarksWithoutOrdering:
        print(",".join([str(x) for x in student]))

    print()
