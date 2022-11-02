from datetime import datetime
import pickle

print("""


        *___   _  _______  _______  _______    _______  _______ 
        |   | | ||       ||       ||       |  |       ||       |
        |   |_| ||    ___||    ___||    _  |  |    ___||   _   |
        |      _||   |___ |   |___ |   |_| |  |   | __ |  | |  |
        |     |_ |    ___||    ___||    ___|  |   ||  ||  |_|  |
        |    _  ||   |___ |   |___ |   |      |   |_| ||       |
        |___| |_||_______||_______||___|      |_______||_______| *
        
        """)

# http://patorjk.com/


def main():
    print()
    print("\t  "+"_"*52)
    print("""\t |                                                    |       
\t |        ,--,--,--.  ,---.  ,--,--,  ,--.,--.        |
\t |        |        | | .-. : |      \ |  ||  |        |
\t |        |  |  |  | \   --. |  ||  | '  ''  '        |
\t |        `--`--`--'  `----' `--''--'  `----'         |
\t |                                                    |""")
    print("\t |\t\t1. 냉장고 속 음식 보기                |")
    print("\t |\t\t2. 냉장고 속 음식 추가                |")
    print("\t |\t\t3. 냉장고 속 음식 삭제                |")
    print("\t |\t\t4. 프로그램 종료                      |")
    print("\t |"+"_"*52+"|")
    print()
    menu = int(input("\t\t메뉴 선택 > "))
    if (menu == 1):
        printFridge()
    elif (menu == 2):
        inputFridge()
    elif (menu == 3):
        deleteFridge()
    elif (menu == 4):
        exitFridge()
    else:
        while (menu != 1 and menu != 2 and menu != 3 and menu != 4):
            print()
            print("-"*50)

            print("\t\t1. 냉장고 내용물 보기")
            print("\t\t2. 냉장고 내용물 추가")
            print("\t\t3. 냉장고 내용물 삭제")
            print("\t\t4. 프로그램 종료")
            print("-"*50)
            menu = int(input("\t다시 선택해주세요 > "))
            if (menu == 1):
                printFridge()
            elif (menu == 2):
                inputFridge()
            elif (menu == 3):
                deleteFridge()
            elif (menu == 4):
                exitFridge()
    print()


def printFridge():
    print()

    with open('fridge_dict.pkl', "rb") as fr:
        fridge = pickle.load(fr)
    print("-"*16+"냉장고 속 음식 보기"+"-"*16)
    if len(fridge) == 0:
        print("\t\t❗ 음식이 없어요")
        main()

    print("   이 름, 유 통 기 한, 갯 수   ·  ·  ·  ·   음식 갯수 >", len(fridge))
    for name, date in fridge.items():
        print("   "+name+", "+date[0]+", "+date[1]+"개")
    main()


def inputFridge():
    print()
    with open('fridge_dict.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print("- "*9+"냉장고 속 음식 추가"+"- "*9)
    name = input("\t무슨 음식인가요? > ")
    dateandant = ["name", 0]
    dateandant[0] = input("\t유통기한은요? (YYYYMMDD) > ")
    dateandant[1] = input("\t갯수는? > ")
    fridge[name] = dateandant

    with open('fridge_dict.pkl', 'wb') as f:
        pickle.dump(fridge, f)

    main()


def deleteFridge():
    with open('fridge_dict.pkl', "rb") as fr:
        fridge = pickle.load(fr)

    print("-"*16+"냉장고 내용물 삭제"+"-"*16)
    if len(fridge) == 0:
        print("\t❗ 음식이 없어 삭제할 수 없습니다.")
        main()
    name = input("\t삭제할 음식은? > ")
    if name not in fridge:
        print("\t\t❗ 입력한 음식이 없습니다.")
        while name not in fridge:
            name = input("\t삭제할 음식은? > ")
            if name not in fridge:
                print("\t\t입력한 음식이 없습니다.")
    else:
        del fridge[name]
    with open('fridge_dict.pkl', 'wb') as f:
        pickle.dump(fridge, f)
    main()


def exitFridge():
    print()
    isExit = input("""   정말 keep Go를 나가시겠습니까?
    
   나가시겠다면 아무 키를, 
   메뉴로 돌아가려면 1을 입력하세요 > """)
    if isExit == "1":
        main()
    else:
        exit()


main()
