submit_credit = 0
read_credit = 0
submit_GPA = 0
read_GPA = 0
submit_subject = 0
read_subject = 0
final_readscore = 0
final_subscore = 0

while True :
    num = input("작업을 선택하세요.")

    if num == '1' :
        credit = int(input("학점을 입력하세요:"))
        score = input("평점을 입력하세요:")
        print("입력되었습니다.")
        read_subject += 1
        if score == "F" :
            read_credit += credit

        else :
            submit_credit += credit
            read_credit += credit

    elif num == '2' :
        final_subscore = submit_credit/submit_subject
        final_readscore = 
        print("제출용: " + submit_credit + "학점 (GPA: " + submit_GPA + ")")
        print("열람용: " + read_credit + "학점 (GPA: " + read_GPA + ")")
        break
    else :
        print("다시 입력하세요")

print("프로그램을 종료합니다.")

if score == "A+" :
    submit_GPA += 4.5
    read_GPA += 4.5
elif score == "A" :
    submit_GPA += 4
    read_GPA += 4
elif score == "B+" :
    submit_GPA += 3.5
    read_GPA += 3
elif score == "B" :
    submit_GPA += 3
    read_GPA += 3
elif score == "C+" :
    submit_GPA += 2.5
    read_GPA += 2.5
elif score == "C" :
    submit_GPA += 2
    read_GPA += 2
elif score == "D+" :
    submit_GPA += 1.5
    read_GPA += 1.5
elif score == "D" :
    submit_GPA += 1
    read_GPA += 1
