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

select_data_query = """
    SELECT *
    FROM Fridge
"""

new_cursor.execute(select_data_query)
selected_data = new_cursor.fetchall()

# 선택된 데이터 출력
for row in selected_data:
    food_name, expiration_date, food_pieces = row
    print(f"Food Name: {food_name}, Expiration Date: {expiration_date}, Food Pieces: {food_pieces}")


new_cursor.close()
new_connection.close()

admin_cursor.close()
admin_connection.close()
