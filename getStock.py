from db import Database
import tushare as ts
import pandas as pd

ts.set_token('31644a89238a09e5a20d7b07ff3e6ed8c54f78e37ad8be417d6ed577')
pro = ts.pro_api()

def get_stock_data():
    """获取全部股票数据并存入数据库"""
    try:
        # 1. 获取股票列表
        df = pro.stock_basic(exchange='', list_status='L')
        
        # 2. 处理数据格式
        df = df[['symbol', 'name', 'ts_code']]  # 选择需要的列
        df.columns = ['stock_code', 'stock_name', 'suffix']  # 重命名列

        
        # 3. 连接数据库
        db = Database()
        if not db.connect():
            print("数据库连接失败")
            return False
        
        print(df)
        # 5. 批量插入数据
        for _, row in df.iterrows():
            db.execute(
                "INSERT INTO stocks (stock_code, stock_name, suffix) VALUES (%s, %s, %s) "
                "ON DUPLICATE KEY UPDATE stock_name=VALUES(stock_name), suffix=VALUES(suffix)",
                (row['stock_code'], row['stock_name'], row['suffix'])
            )
        
        print(f"成功插入/更新 {len(df)} 条股票数据")
        return True
        
    except Exception as e:
        print(f"获取股票数据失败: {e}")
        return False
    finally:
        db.disconnect()

if __name__ == "__main__":
    get_stock_data()