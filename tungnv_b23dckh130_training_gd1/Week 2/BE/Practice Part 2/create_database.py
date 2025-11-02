import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='NguyenVinhTung2005'
    )
    
    cursor = connection.cursor()
    
    # Tao database
    cursor.execute("CREATE DATABASE IF NOT EXISTS typ CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
    print("[OK] Da tao database 'typ'")

    cursor.execute("SHOW DATABASES LIKE 'typ'")
    result = cursor.fetchone()
    if result:
        print(f"[OK] Database 'typ' ton tai: {result[0]}")
    
    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"[ERROR] Loi: {e}")

