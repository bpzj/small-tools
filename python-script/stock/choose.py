import tushare

stocks = tushare.get_stock_basics()

# 过滤城市
cities = ['北京', '上海', '深圳', '杭州']
stocks = stocks.loc[stocks.area.isin(cities)]
# codes = stocks.query('area == "上海"')


print(stocks)


