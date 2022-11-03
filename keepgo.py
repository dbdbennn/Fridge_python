from datetime import datetime
import pickle
from tabulate import tabulate


# 리포지토리 keepgo로 바뀐지 확인

# 초기화
# fridge = dict()
# with open('fridge.pkl', 'wb') as f:
#     pickle.dump(fridge, f)

print('\033[92m'+"""

*___   _  _______  _______  _______    _______  _______
|   | | ||       ||       ||       |  |       ||       |
|   |_| ||    ___||    ___||    _  |  |    ___||   _   |
|      _||   |___ |   |___ |   |_| |  |   | __ |  | |  |
|     |_ |    ___||    ___||    ___|  |   ||  ||  |_|  |
|    _  ||   |___ |   |___ |   |      |   |_| ||       |
|___| |_||_______||_______||___|      |_______||_______| *

        """+'\033[0m')

# http://patorjk.com/


def str_Red(text):
    return '\033[92m'+text+'\033[0m'


def backtomenu():
    print()
    print("\t\t 메뉴로 돌아갑니다 ⬇️")
    print()


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

    menu = input("\t\t메뉴 선택 > ")
    if (menu == "1"):
        printFridge()
    elif (menu == "2"):
        inputFridge()
    elif (menu == "3"):
        deleteFridge()
    elif (menu == "4"):
        exitFridge()
    else:
        while (menu != "1" and menu != "2" and menu != "3" and menu != "4"):
            print()
            menu = input("\t다시 선택해주세요 > ")
            if (menu == "1"):
                printFridge()
            elif (menu == "2"):
                inputFridge()
            elif (menu == "3"):
                deleteFridge()
            elif (menu == "4"):
                exitFridge()


def printFridge():
    print()
    today = datetime.today().strftime('%Y-%m-%d')

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)
    print("냉장고 속 음식 보기 * 🍅 * 🥕 * 🥬 * 🥩 * 🥚 * 🍇 * 🥔")
    print()

    if len(fridge) == 0:
        print(str_Red("\t\t  ❗ 음식이 없어요"))
        backtomenu()
        main()

    # tabulate로 출력 시도.
    # 이 순간에만 fridge_dict로 따로 딕셔너리 만들어서 출력해볼 예정
    ant_list = list()
    num_list = list()

    for i in range(0, len(fridge)):
        ant_list.append(list((list(fridge.values()))[i])[0])

    for i in range(0, len(fridge)):
        num_list.append(list((list(fridge.values()))[i])[1])

    fridge_dict = {"이름": list(fridge.keys()),
                   "유통기한": ant_list,
                   "갯수": num_list}

    headers = ["이름", "유통기한", "갯수"]
    print(tabulate(fridge_dict, stralign="center",
          tablefmt='fancy_grid', headers=headers))
    backtomenu()
    main()


def inputFridge():
    print()

    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print("\t "+"- "*9+"냉장고 속 음식 추가"+"- "*9)
    name = input("\t\t  무슨 음식인가요? > ")
    dateandant = ["name", 0]
    dateandant[0] = input("\t\t  유통기한은요? (YYYY-MM-DD) > ")
    dateandant[1] = input("\t\t  갯수는요? > ")
    fridge[name] = dateandant

    with open('fridge.pkl', 'wb') as f:
        pickle.dump(fridge, f)
    backtomenu()
    main()


def deleteFridge():
    with open('fridge.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print()
    print("냉장고 속 음식 삭제 - 🍅 - 🥕 - 🥬 - 🥩 - 🥚 - 🍇 - 🥔")
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
    isExit = input("""
    \t\t정말 keep Go를 나가시겠습니까?

   \t\t나가시겠다면 아무 키를,
   \t\t메뉴로 돌아가려면 1을 입력하세요 > """)
    if isExit == "1":
        backtomenu()
        main()
    else:
        exit()


main()
