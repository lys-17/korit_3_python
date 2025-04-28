import mariadb

if __name__ == "__main__":
    connection = mariadb.connect(
        host="localhost",
        port=3306,
        user='root',
        password='1q2w3e4r',
        database='webtoon'
    )

    cursor = connection.cursor()
    dataList = [
        ('월', 'title', 'author1', '6.4', "imgurl1"),
        ('화', 'title', 'author2', '8.6', "imgurl2"),
        ('수', 'title', 'author3', '9.4', "imgurl3")
    ]

    sql = """
        insert into webtoon_tb
        values (default, ?, ?, ?, ?, ?)
    """
    cursor.executemany(sql, dataList)
    connection.commit()



