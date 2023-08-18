import subprocess
import cx_Oracle
from tabulate import tabulate
from datetime import datetime  # datetime 모듈 추가

# 모듈 설치 함수
def install_module(module):
    subprocess.check_call(["pip", "install", module])

# 필요한 모듈들 목록
required_modules = ['cx_Oracle', 'tabulate']  # 필요한 모듈들 추가

# 필요한 모듈 설치
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Installing {module} module...")
        install_module(module)

from datetime import datetime
from tabulate import tabulate  # 표 작성
# 내가 만든 모듈
import strChanger as sc
import date_calculate as dc
import isDate as id
tabulate.WIDE_CHARS_MODE = False

import cx_Oracle

# 연결 정보
admin_username = "system"
admin_password = "1234"
hostname = "localhost"
port = "1521"
service_name = "XE"

dsn = cx_Oracle.makedsn(hostname, port, service_name=service_name)

# 관리자 계정으로 연결
admin_connection = cx_Oracle.connect(admin_username, admin_password, dsn)
admin_cursor = admin_connection.cursor()

# 사용자 'yje'가 이미 존재하는지 확인
existing_user_query = """
    SELECT COUNT(*)
    FROM dba_users
    WHERE username = 'YJE'
"""
admin_cursor.execute(existing_user_query)
user_count = admin_cursor.fetchone()[0]

if user_count == 0:
    # 사용자 'yje' 생성
    new_username = "YJE"
    new_password = "yje1234"
    admin_cursor.execute(f"CREATE USER {new_username} IDENTIFIED BY {new_password}")
    admin_cursor.execute(f"GRANT CONNECT, RESOURCE TO {new_username}")
    print("User 'YJE' created successfully.")

# 사용자 'yje' 계정으로 연결
new_dsn = cx_Oracle.makedsn(hostname, port, service_name=service_name)
new_connection = cx_Oracle.connect("YJE", "yje1234", dsn=new_dsn)
new_cursor = new_connection.cursor()

# 'Fridge' 테이블이 이미 존재하지 않는 경우에만 테이블 생성
existing_table_query = """
    SELECT COUNT(*)
    FROM all_tables
    WHERE owner = 'YJE' AND table_name = 'FRIDGE'
"""
new_cursor.execute(existing_table_query)
table_count = new_cursor.fetchone()[0]

if table_count == 0:
    create_table_query = """
        CREATE TABLE Fridge (
            food_name VARCHAR2(255),
            expiration_date DATE,
            food_pieces NUMBER(3)
        )
    """
    new_cursor.execute(create_table_query)
    new_connection.commit()
    print("Table 'Fridge' created successfully.")
else:
    print("Table 'Fridge' already exists.")


####################################################
#printFridge

select_data_query = """
    SELECT *
    FROM Fridge
"""

new_cursor.execute(select_data_query)
selected_data = new_cursor.fetchall()

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

new_cursor.close()
new_connection.close()

admin_cursor.close()
admin_connection.close()
