from datetime import datetime
import datetime
import strChanger as sc

# today = datetime.date.today()
# input_date = '2022-12-10'
# input_date_list = input_date.split('-')
# input_date = datetime.date(
#     int(input_date_list[0]), int(input_date_list[1]), int(input_date_list[2]))

# print(input_date - today)

today = datetime.date.today()


def ca(input_date):
    input_date_list = input_date.split('-')
    input_date = datetime.date(
        int(input_date_list[0]), int(input_date_list[1]), int(input_date_list[2]))

    date_gap = (str(today-input_date).split(' '))[0]
    if input_date < today:
        return sc.str_Red(date_gap+"일 지났습니다❗")
    date_gap = int(date_gap)

    if date_gap <= 7:
        return sc.str_Yellow("일주일 정도 남았어요!")
    elif date_gap >= 30:
        return "한 달 넘게 남았어요"
    else:
        return date_gap, "남았어요"


# print(ca('2022-11-06'))
