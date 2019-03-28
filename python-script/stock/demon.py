# 1 新概念炒作

# 2 小盘股 < 80亿, 启动时 价钱不高

# 3 轻松突破压力位 10日线、20日线、60日线、120日线，突破20日线为一个买入点？结合成交量看？
# 3 第一个涨停就站上了所有的均线，上方无压力

# 4 换手率后期要高，资金持续炒作

import tushare as ts

ts.set_token("14bb77ad0add9b8326b8d694a3a4b8ac6d84b48f5b297a866d98129a")
pro = ts.pro_api()

df = pro.daily_basic(
    ts_code='',
    trade_date='20190328',
    fields='ts_code,trade_date,close,turnover_rate_f,volume_ratio,pe,pb,total_mv,circ_mv')

small = df.loc[df.circ_mv < 800000]
s_low = small.loc[small.close < 40]
# print(small)
print(s_low)


# 今日涨幅超过 9% 的
z_t = pro.daily(trade_date='20190328')
high = z_t.loc[(z_t.pct_chg > 9) & (z_t.pct_chg < 11)]
print(high)
