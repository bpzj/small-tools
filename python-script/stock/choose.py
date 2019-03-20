import tushare

stocks = tushare.get_stock_basics()

# 过滤城市
cities = ['北京', '上海', '深圳', '杭州']
filter_city = stocks.loc[stocks.area.isin(cities)]
# codes = stocks.query('area == "上海"')

# 上市日期 15年之后
filter_year = filter_city.loc[filter_city.timeToMarket >= 20150101]

# 行业

# 流通值范围

# 30日涨幅

print(filter_year)


