import pymysql
from pymysql import Error

class Database:
    def __init__(self):
        """简化版数据库连接工具(内置参数)"""
        self.connection = None
        self.host = 'localhost'  # 修改为您实际的数据库地址
        self.user = 'root'  # 修改为您的数据库用户名
        self.password = 'admin'  # 修改为您的数据库密码
        self.database = 'akup'  # 修改为您的数据库名
    
    def connect(self):
        """建立数据库连接"""
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("数据库连接成功")
            return True
        except Error as e:
            print(f"数据库连接失败: {e}")
            return False
    
    def is_connected(self):
        """检查连接状态"""
        if not self.connection:
            return False
        try:
            self.connection.ping(reconnect=False)
            return True
        except:
            return False
    
    def disconnect(self):
        """关闭数据库连接"""
        if self.is_connected():
            self.connection.close()
            print("数据库连接已关闭")
    
    def execute(self, query, params=None):
        """执行SQL查询"""
        if not self.is_connected():
            print("数据库未连接")
            return None
            
        try:
            cursor = self.connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query, params or ())
            
            if query.strip().lower().startswith('select'):
                result = cursor.fetchall()
            else:
                self.connection.commit()
                result = True
                
            cursor.close()
            return result
        except Error as e:
            print(f"SQL执行错误: {e}")
            return None