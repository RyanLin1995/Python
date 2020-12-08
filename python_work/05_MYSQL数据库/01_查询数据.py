import pymysql


class GetData(object):

    def __init__(self):
        self.connect = pymysql.connect(host ="localhost", user="root", password="a12345",
                                  database="jingdong", charset="utf8")
        self.cursor = self.connect.cursor()

    def __del__(self):

        self.cursor.close()
        self.connect.cursor()

    def execute_sql(self, sql_command):

        self.cursor.execute(sql_command)
        for item in self.cursor.fetchall():
            print(item)

    def show_all_items(self):

        sql_command = "select * from goods;"
        self.execute_sql(sql_command)

    def show_cates(self):

        sql_command = "select name from goods_cates;"
        self.execute_sql(sql_command)

    def show_brands(self):

        sql_command = "select name from goods_brands;"
        self.execute_sql(sql_command)

    @staticmethod
    def print_menu():

        print("请选择你要查询的信息")
        print("---------------------------")
        print("1. 查询所有商品信息")
        print("2. 查询所有商品分类")
        print("3. 查询所有商品品牌分类")
        return input("请输入:")

    def run(self):

        while True:
            choose = self.print_menu()
            if choose == "1":
                self.show_all_items()

            if choose == "2":
                self.show_cates()

            if choose == "3":
                self.show_brands()

            if choose == "q" or choose == "0":
                exit()


def main():
    jd = GetData()
    jd.run()


if __name__ == '__main__':
    main()

