import tushare as ts
import QUANTAXIS as qa

ts.set_token("14bb77ad0add9b8326b8d694a3a4b8ac6d84b48f5b297a866d98129a")
pro = ts.pro_api()
# 获取基本数据，需要数据：上市日期，行业
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code, symbol, name, industry, list_date')

# 上市日期 在 15年 股灾之后
filter_year = data.loc[data.list_date >= '20150630']
# 行业


# 获取信息： 所在城市
stocks = pro.stock_company(exchange='SSE', fields='ts_code, city, main_business')
stocks = stocks.append(pro.stock_company(exchange='SZSE', fields='ts_code, city, main_business'), ignore_index=True)
# 过滤城市
cities = ['北京市', '上海市', '深圳市', '杭州市', '广州市']
filter_city = stocks.loc[stocks.city.isin(cities)]



# qa.QA_fetch_get_stock_day()

# 流通值范围 50亿 - 200亿

# 1月31日 以来的涨幅 < 60%

# 3月26日以来 跌幅 < 0%

print(filter_year)
print(filter_city)


