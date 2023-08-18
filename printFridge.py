# print_fridge_module.py

from tabulate import tabulate

def print_fridge(cursor):
    select_data_query = """
        SELECT *
        FROM Fridge
    """
    cursor.execute(select_data_query)
    selected_data = cursor.fetchall()

    # 선택된 데이터 출력
    table_data = []
    for row in selected_data:
        food_name, expiration_date, food_pieces = row
        # datetime 객체를 날짜 형식으로 변환하여 추가
        formatted_date = expiration_date.date()  # 날짜 부분만 추출
        table_data.append([food_name, formatted_date, food_pieces])

    table_headers = ["Food Name", "Expiration Date", "Food Pieces"]
    table = tabulate(table_data, headers=table_headers, tablefmt="rounded_grid", stralign="center")
    print(table)
