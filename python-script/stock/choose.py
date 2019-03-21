import tushare as ts

ts.set_token("14bb77ad0add9b8326b8d694a3a4b8ac6d84b48f5b297a866d98129a")
pro = ts.pro_api()
stocks = pro.pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province,city')

# 过滤城市
cities = ['北京', '上海', '深圳', '杭州']
filter_city = stocks.loc[stocks.city.isin(cities)]
# codes = stocks.query('area == "上海"')

# 上市日期 15年之后
filter_year = filter_city.loc[filter_city.timeToMarket >= 20150101]

# 行业

# 流通值范围

# 30日涨幅

print(filter_year)


