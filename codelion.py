import random
import time #time.sleep()을 사용하기 위해

#for 반복문
for x in range(30): #0부터 29까지 반복
    print(random.choice(["된장찌개","피자","제육볶음","치킨","떡볶이"])) #리스트
    print("이 문장도 반복되나")

#while 반복문
while True: #무한반복
    print(random.choice(["된장찌개","피자","제육볶음","치킨","떡볶이"]))
    time.sleep(1) #1초 동안 쉼
    break #while 반복문 종료

#반복문에 변수 부여하기
lunch = random.choice(["된장찌개","피자","제육볶음","치킨","떡볶이"])
dinner = random.choice(["김밥","쫄면","돈까스"])
lunch = "냉장고" #변수의 내용 변경하기
print(lunch)

#딕셔너리
info = {"고향":"수원","취미":"영화보기","좋아하는 음식":"국수"}
print(info)
print(info.get("취미")) #원하는 데이터만 불러옴
info2 = {"특기":"피아노", "사는곳":"서울"}
print(info2.get("특기"))
print(info2.get("사는곳"))

info["특기"] = "피아노" #딕셔너리 내용 추가
del info["좋아하는 음식"] #딕셔너리 내용 삭제
info.clear() #딕셔너리 내용 모두 삭제

#리스트
food = ["된장찌개", "피자", "제육볶음"]
print(food[0]) #리스트의 첫번째 데이터 출력
print(food[-1]) #리스트의 가장 마지막 데이터 출력
food.append("김밥") #리스트 요소 추가
del food[1] #리스트 요소 삭제 (1은 두번째 요소 삭제)

#끝까지 반복
for x in range(30):
    print(x) #0~29 출력

food = ["된장찌개", "피자", "제육볶음"]
#반복문을 이용하여 리스트의 내용 모두 출력 
for x in range(3):
    print(food[x])
#리스트 요소 하나하나에 접근, 중간에 잘못된 요소가 있더라도 오류없이 끝까지 출력
for x in food:
    print(x)

info = {"고향":"수원","취미":"영화보기","좋아하는 음식":"국수"}
#반복문을 이용하여 딕셔너리에 모든 요소를 하나하나씩 접근하여 출력
for x,y in info.items():
    print(x)
    print(y)

#집합
#리스트와 달리 순서가 없음
#리스트와 달리 겹치는 원소가 없음(겹치는 원소 입력 불가)
#합집합: 겹치는 원소를 하나로 합쳐줌
#차집합: 겹치는 원소를 없앰
#교집합: 겹치는 원소만 뽑음
food = ["된장찌개", "피자", "제육볶음"]
food_set1 = set(food) #food라는 리스트를 food_set1이라는 집합으로 변경
print(food_set1) #출력되는 순서는 입력한 순서와 다를 수 있음

#합집합, 교집합, 차집합
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])
menu3 = menu1 | menu2 #합집합
menu4 = menu1 & menu2 #교집합
menu5 = menu1 - menu2 #차집합

#if
food = ["된장찌개", "피자", "제육볶음"]
print(food)
if (food == "제육볶음"):
    print("곱빼기 주세요")
else:
    print("그냥 주세요")
print("종료")

#음식 메뉴 추천 프로그램
print("")
print("---------- 오늘 뭐 드실? ----------")
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]
while True:
    print(lunch)
    item = input("음식을 추가 해주세요(종료:q): ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
print (lunch)

set_lunch = set(lunch) #lunch를 집합으로 변경
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요(종료:q): ")
    if(item == "q"):
        break
    else: 
        set_lunch = set_lunch - set([item]) #set_luch에서 아이템을 하나 제거한 것을 set_lunch로 재정의
print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_lunch)))

#함수
print("")
print("---------- 음료 만들기 ----------")
def make_dolcelatte():
    print("돌체라떼 만들기")
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml 넣는다")
    print("3. 찬 우유를 넣는다")
    print("4. 에스프레소샷을 넣는다.")

def make_blueberry_smoothie():
    print("블루베리스무디 만들기")
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다.")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다.")

def make_simple_latte():
    print("라떼 만들기")
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")

make_simple_latte() #make_simple_latte() 함수 실행

#익명게시판 만들기
print("")
print("---------- 익명게시판 만들기 ----------")
total_dic = {} #빈 딕셔너리 만들기
while True:
    question = input("질문을 입력해주세요: ")
    if question == "q":
        break
    else:
        total_dic[question] = "" #value에 빈 문자열을 입력
for i in total_dic:
    print(i)
    answer = input("답변을 입력해주세요: ")
    total_dic[i] = answer
print(total_dic)

total_list = [] #빈 리스트 만들기
while True:
    question = input("질문을 입력해주세요: ")
    if question == "q":
        break
    else:
        total_list.append{"질문":question, "답변": ""}
for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요: ")
    i["답변"] = answer
print(total_list)