from datetime import datetime
import pickle
from tabulate import tabulate
import strChanger as sc
import date_calculate as dc


# 리포지토리 keepgo로 바뀐지 확인

# 초기화
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
    print("|\t\t1. 냉장고 속 음식 보기               |")
    print("|\t\t2. 냉장고 속 음식 추가               |")
    print("|\t\t3. 냉장고 속 음식 삭제               |")
    print("|\t\t4. 프로그램 종료                     |")
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
        deleteFridge()
    elif menu == "4":
        exitFridge()
    else:  # 다른 수(str형태)가 입력됐을 때 while문을 돌린다.
        while (menu != "1"
               and menu != "2"
               and menu != "3"
               and menu != "4"):
            print()
            menu = input("\t다시 선택해주세요 > ")
            if menu == "1":
                printFridge()
            elif menu == "2":
                inputFridge()
            elif menu == "3":
                deleteFridge()
            elif menu == "4":
                exitFridge()


def printFridge():
    print()
    today = datetime.today().strftime('%Y-%m-%d')

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)
    print(sc.str_Yellow("냉장고 속 음식 보기 * 🍅 * 🥕 * 🥬 * 🥩 * 🥚 * 🍇 * 🥔"))
    print()

    if len(fridge) == 0:
        print(sc.str_Red("\t\t  ❗ 음식이 없어요"))
        backtomenu()
        main()

    # tabulate로 출력 시도.
    # 이 순간에만 fridge_dict로 따로 딕셔너리 만들어서 출력해볼 예정

    # 갯수 리스트
    amount_list = list()
    # 유통기한 리스트
    date_list = list()
    # 남은 기한 리스트
    left_date_list = list()
    list_temp = list()

    for i in range(0, len(fridge)):
        date_list.append(list(list(fridge.values())[i])[0])

    for i in range(0, len(fridge)):
        amount_list.append(list(list(fridge.values())[i])[1])

    for i in range(0, len(fridge)):
        list_temp.append(list(list(fridge.values())[i])[0])

    for i in range(0, len(fridge)):
        left_date_list.append(dc.ca(list_temp[i]))

    print(left_date_list)

    fridge_dict = {"이름": list(fridge.keys()),
                   "갯수": amount_list,
                   "유통기한": date_list,
                   "남은 기한": left_date_list}

    headers = ["이름", "갯수", "유통기한", "남은 기한"]
    print(tabulate(fridge_dict, stralign="center",
          tablefmt='fancy_grid', headers=headers))
    backtomenu()
    main()


def inputFridge():
    print()

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print(sc.str_Magenta("냉장고 속 음식 추가 + 🍅 + 🥕 + 🥬 + 🥩 + 🥚 + 🍇 + 🥔"))
    name = input("\n\t  무슨 음식인가요? > ")
    date_and_amount = ["name", 0]
    date_and_amount[0] = input("\t  유통기한은요? (YYYY-MM-DD) > ")
    date_and_amount[1] = input("\t  갯수는요? > ")
    fridge[name] = date_and_amount

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)
    backtomenu()
    main()


def deleteFridge():
    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print()
    print(sc.str_Cyan("냉장고 속 음식 삭제 - 🍅 - 🥕 - 🥬 - 🥩 - 🥚 - 🍇 - 🥔"))
    if len(fridge) == 0:
        print("\n\t  ❗ 음식이 없어 삭제할 수 없습니다.")
        backtomenu()
        main()

    name = input("\n\t\t삭제할 음식은? > ")

    while name not in fridge:
        print('\033[31m' + '\n\t\t❗ 입력한 음식이 없습니다.' + '\033[0m')
        name = input("\n\t\t삭제할 음식은? > ")

    del fridge[name]
    print("\n\t\t"+'\033[94m'+name+'\033[0m'+" 삭제했습니다!")

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)
    backtomenu()
    main()


def exitFridge():
    print()
    isExit = input(sc.str_Green("""
    \t정말 keep Go를 나가시겠습니까?

   \t나가시겠다면 아무 키를,
   \t메뉴로 돌아가려면 1을 입력하세요 > """))
    if isExit == "1":
        backtomenu()
        main()
    else:
        exit()


def backtomenu():
    print()
    print("\t\t 메뉴로 돌아갑니다 ⬇️")
    print()


main()
