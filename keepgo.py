import subprocess

# 필요한 모듈 리스트
required_modules = ["datetime", "pickle", "tabulate", "strChanger", "date_calculate", "isDate"]

# 모듈 설치 함수
def install_module(module):
    subprocess.check_call(["pip", "install", module])

# 필요한 모듈 설치
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {module} module...")
        install_module(module)

from datetime import datetime
import pickle  # 객체 저장 파일 생성
from tabulate import tabulate  # 표 작성
# 내가 만든 모듈
import strChanger as sc
import date_calculate as dc
import isDate as id


# 리포지토리 keepgo로 바뀐지 확인

# fridge = dict()
# with open('fridge.pkl', 'wb') as f:
#     pickle.dump(fridge, f)

print(sc.str_Green("""

*___   _  _______  _______  _______    _______  _______
|   | | ||       ||       ||       |  |       ||       |
|   |_| ||    ___||    ___||    _  |  |    ___||   _   |
|      _||   |___ |   |___ |   |_| |  |   | __ |  | |  |
|     |_ |    ___||    ___||    ___|  |   ||  ||  |_|  |
|    _  ||   |___ |   |___ |   |      |   |_| ||       |
|___| |_||_______||_______||___|      |_______||_______| *

        """))

# http://patorjk.com/


def main():
    # 메뉴창 출력문
    print(" "+"_"*52)
    print("""|                                                    |
|        ,--,--,--.  ,---.  ,--,--,  ,--.,--.        |
|        |        | | .-. : |      \ |  ||  |        |
|        |  |  |  | \   --. |  ||  | '  ''  '        |
|        `--`--`--'  `----' `--''--'  `----'         |
|                                                    |""")
    print("|\t\t1. 냉장고 열어보기                   |")
    print("|\t\t2. 냉장고에 음식 넣기                |")
    print("|\t\t3. 음식 정보 바꾸기                  |")
    print("|\t\t4. 냉장고에서 음식 꺼내기            |")
    print("|\t\t5. 프로그램 종료                     |")
    print("|"+"_"*52+"|")
    print()
    # 메뉴창 출력 끝

    # 메뉴 선택 창
    menu = input("\t\t메뉴 선택 > ")
    if menu == "1":
        printFridge()
    elif menu == "2":
        inputFridge()
    elif menu == "3":
        setFridge()
    elif menu == "4":
        deleteFridge()
    elif menu == "5":
        exitFridge()
    else:  # 다른 수(str형태)가 입력됐을 때 while문을 돌린다.
        while (menu != "1"
               and menu != "2"
               and menu != "3"
               and menu != "4"
               and menu != "5"):
            print()
            menu = input("\t다시 선택해주세요 > ")
            if menu == "1":
                printFridge()
            elif menu == "2":
                inputFridge()
            elif menu == "3":
                setFridge()
            elif menu == "4":
                deleteFridge()
            elif menu == "5":
                exitFridge()


def printFridge():
    print()
    today = datetime.today().strftime('%Y-%m-%d')

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)
    print(sc.str_Yellow("냉장고 열어보기 * 🍅 * 🥕 * 🥬 * 🥩 * 🥚 * 🍇 * 🥔 * 🧀"))
    print()

    if len(fridge) == 0:
        print(sc.str_Red("\t\t  ❗ 음식이 없어요"))
        backtomenu()

    # tabulate로 출력 시도.
    # 이 순간에만 fridge_dict로 따로 딕셔너리 만들어서 출력해볼 예정

    # 갯수 리스트
    amount_list = list()
    # 유통기한 리스트
    date_list = list()
    # 남은 기한 리스트
    left_date_list = list()
    list_temp = list()

    # 유통기한 리스트
    for i in range(0, len(fridge)):
        date_list.append(list(list(fridge.values())[i])[1])

    # 갯수 리스트
    for i in range(0, len(fridge)):
        amount_list.append(list(list(fridge.values())[i])[0])

    # 남은 기한을 date_calculate.py에 넘겨줄 list
    for i in range(0, len(fridge)):
        list_temp.append(list(list(fridge.values())[i])[1])

    # 남은 기한 dc.ca() 이용해 계산
    for i in range(0, len(fridge)):
        left_date_list.append(dc.ca(list_temp[i]))

    fridge_dict = {"이름": list(fridge.keys()),
                   "갯수": amount_list,
                   "유통기한": date_list,
                   "남은 기한": left_date_list}

    headers = ["이름", "갯수", "유통기한", "남은 기한"]
    print(tabulate(fridge_dict, stralign="center",
          tablefmt='rounded_grid', headers=headers))
    backtomenu()


def inputFridge():
    print()

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print(sc.str_Magenta("냉장고에 음식 넣기 + 🍅 + 🥕 + 🥬 + 🥩 + 🥚 + 🍇 + 🥔 + 🧃"))
    name = input("\n\t  무슨 음식인가요? > ")
    # 음식 이름 입력
    date_and_amount = ["name", 0]

    # 음식 갯수 입력
    date_and_amount[0] = input("\n\t  갯수는요? > ")
    # 숫자인지 판별
    while (date_and_amount[0].isdigit() == False):
        print(sc.str_Red('\n\t❗ 숫자만 입력해주세요.'))
        date_and_amount[0] = input("\n\t  갯수는요? > ")

    # 유통기한 입력
    date_and_amount[1] = input("\n\t  유통기한은요? (YYYY-MM-DD) > ")
    while (id.isDate(date_and_amount[1]) == False):
        print('\033[31m' + '\n\t❗ YYYY-MM-DD 형태로 입력해주세요.' + '\033[0m')
        date_and_amount[1] = input("\n\t  유통기한은요? (YYYY-MM-DD) > ")
    fridge[name] = date_and_amount

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)

    print("\n\t\t"+sc.str_Blue(name)+"을(를) 넣었습니다!")

    backtomenu()


def deleteFridge():
    with open("fridge.pkl", "rb") as fr:
        fridge = pickle.load(fr)

    print()
    print(sc.str_Cyan("냉장고에서 음식 꺼내기 - 🍅 - 🥕 - 🥬 - 🥩 - 🥚 - 🍇 - 🥔 - 🍠"))
    if len(fridge) == 0:
        print("\n\t  ❗ 음식이 없어 꺼낼 수 없습니다.")
        backtomenu()

    name = input("\n\t\t꺼낼 음식은? > ")
    while name not in fridge:
        print(sc.str_Red("\n\t\t❗ 입력한 음식이 없습니다."))
        name = input("\n\t\t꺼낼 음식은? > ")

    amount = int(input("\n\t\t꺼낼 음식의 갯수는? > "))
    while amount <= 0 or amount > int(fridge[name][0]):
        print(sc.str_Red("\n\t\t❗ 입력한 음식의 갯수가 올바르지 않습니다."))
        amount = int(input("\n\t\t꺼낼 음식의 갯수는? > "))

    fridge[name][0] = str(int(fridge[name][0]) - amount)
    if fridge[name][0] == "0":
        del fridge[name]
        print("\n\t\t" + sc.str_Blue(name) + "을(를) 모두 꺼냈습니다!")
    else:
        print("\n\t\t" + sc.str_Blue(name) + "을(를) " + str(amount) + "개 꺼냈습니다!")

    with open("fridge.pkl", "wb") as f:
        pickle.dump(fridge, f)

    backtomenu()
    with open("fridge.pkl", "rb") as fr:
        fridge = pickle.load(fr)

    print()
    print(sc.str_Cyan("냉장고에서 음식 꺼내기 - 🍅 - 🥕 - 🥬 - 🥩 - 🥚 - 🍇 - 🥔 - 🍠"))
    if len(fridge) == 0:
        print("\n\t  ❗ 음식이 없어 꺼낼 수 없습니다.")
        backtomenu()

    name = input("\n\t\t꺼낼 음식은? > ")

    while name not in fridge:
        print(sc.str_Red("\n\t\t❗ 입력한 음식이 없습니다."))
        name = input("\n\t\t꺼낼 음식은? > ")

    del fridge[name]
    print("\n\t\t" + sc.str_Blue(name) + "을(를) 꺼냈습니다!")

    with open("fridge.pkl", "wb") as f:
        pickle.dump(fridge, f)
    backtomenu()

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print()
    print(sc.str_Cyan("냉장고에서 음식 꺼내기 - 🍅 - 🥕 - 🥬 - 🥩 - 🥚 - 🍇 - 🥔 - 🍠"))
    if len(fridge) == 0:
        print("\n\t  ❗ 음식이 없어 꺼낼 수 없습니다.")
        backtomenu()

    name = input("\n\t\t꺼낼 음식은? > ")

    while name not in fridge:
        print(sc.str_Red("\n\t\t❗ 입력한 음식이 없습니다."))
        name = input("\n\t\t꺼낼 음식은? > ")

    del fridge[name]
    print("\n\t\t"+sc.str_Blue(name)+"을(를) 꺼냈습니다!")

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)
    backtomenu()


def setFridge():
    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)
    print()
    print(sc.str_BYellow("음식 정보 바꾸기 • 🍅 • 🥕 • 🥬 • 🥩 • 🥚 • 🍇 • 🥔 • 🥗"))
    if len(fridge) == 0:
        print(sc.str_Red("\n\t  ❗ 음식이 없어 수정할 수 없습니다."))
        backtomenu()

    name = input("\n\t수정할 음식은? > ")
    while name not in fridge:
        print('\033[31m' + '\n\t\t❗ 입력한 음식이 없습니다.' + '\033[0m')
        name = input("\n\t수정할 음식은? > ")

    set_list = [['음식 이름은 "1️" ', '음식 갯수는 "2️" ', '유통기한은 "3️" ']]
    print("\n"+tabulate(set_list, stralign="center",
          tablefmt='rounded_grid'))
    menu = input("\n\t무엇을 수정하시겠어요? > ")
    while (menu != "1"
           and menu != "2"
           and menu != "3"):
        print()
        menu = input("\t다시 선택해주세요 > ")

    if menu == "1":
        new_name = input("\n\t무슨 음식인가요? > ")
        fridge[new_name] = fridge.pop(name)
    elif menu == "2":
        new_num = input("\n\t몇 개인가요? > ")
        while (new_num[0].isdigit() == False):
            print('\033[31m' + '\n\t❗ 숫자만 입력해주세요.' + '\033[0m')
            new_num = input("\n\t  몇 개인가요? > ")
        fridge[name][0] = new_num
    elif menu == "3":
        new_date = (input("\n\t유통기한(YYYY-MM-DD) > "))
        while (id.isDate(new_date) == False):
            print('\033[31m' + '\n\t❗ YYYY-MM-DD 형태로 입력해주세요.' + '\033[0m')
            new_date = input("\n\t유통기한(YYYY-MM-DD) > ")
        fridge[name][1] = new_date

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)

    print("\n\t\t"+sc.str_Blue(name)+"을(를) 수정했습니다!")

    backtomenu()


def exitFridge():
    print()
    isExit = input(sc.str_Green("""
    \t정말 keep Go를 나가시겠습니까? 🥺

   \t나가시겠다면 아무 키를,
   \t메뉴로 돌아가려면 1을 입력하세요 > """))
    if isExit == "1":
        backtomenu()
    else:
        exit()


def backtomenu():
    print()
    inputMeun = input("\t 엔터를 누르면 메뉴로 돌아갑니다 ⬇️  ")
    if(str(type(inputMeun)) == "<class 'str'>") :
        main()


main()
