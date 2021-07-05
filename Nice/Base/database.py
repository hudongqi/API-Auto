import pymysql
from Base.read_yaml import ReadYaml

class Database:

    def __init__(self):
        self.host = ReadYaml().get_value('database.host')
        self.port = ReadYaml().get_value('database.port')
        self.user = ReadYaml().get_value('database.user')
        self.password = ReadYaml().get_value('database.password')
        self.db_name = ReadYaml().get_value('database.name')
        self.charset = ReadYaml().get_value('database.charset')
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=str(self.password),
                                    db=self.db_name, charset=self.charset)
        self.cursor = self.conn.cursor()

    # 查询
    def search(self,sql):
        cur = self.cursor
        cur.execute(sql)
        self.close()
        result = cur.fetchall()

        a = []
        for row in result:
            id = row[0]
            a.append(id)

        return result



    def close(self):
        self.cursor.close()
        self.conn.close()



