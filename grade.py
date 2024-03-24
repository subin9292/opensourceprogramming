# 학점 계산 함수
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

# 각 항목을 담는 리스트 생성
name = []
c_score = []
eng_score = []
python_score = []
average_score=[]
total_score = []
grade = []
rank_list = []

# 학생 정보 입력 받기
for i in range(0, 5, 1):
    print(f"--- 학생 {i+1}의 정보 입력 ---")
    name.append(input("이름을 입력하세요: "))
    c_score.append(float(input("C언어 성적을 입력하세요: ")))
    eng_score.append(float(input("영어 성적을 입력하세요: ")))
    python_score.append(float(input("파이썬 성적을 입력하세요: ")))


    total_score.append(c_score[i] + eng_score[i] + python_score[i])
    average_score.append(total_score[i] / 3)

    grade.append(calculate_grade(average_score[i]))


#등수 구하기
for i in range(0, 5, 1):
  rank = 1
  for j in range(0, 5, 1):
     if average_score[i] < average_score[j]:
         rank += 1
  rank_list.append(rank)


#출력
print("\n======================================\n")

for i in range(0, 5, 1) :
   print("이름:",name[i], " 총점:","%.2f" %total_score[i], " 평균:","%.2f" %average_score[i], " 학점:", grade[i], " 등수:", rank_list[i])



