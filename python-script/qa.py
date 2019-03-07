import QUANTAXIS as qa
import pymongo
import pandas as pd
from QUANTAXIS.QAUtil import DATABASE


def get_block():
    block = qa.QA_fetch_stock_block_adv()
    codes = block.data.reset_index().query('blockname == "上海"')
    # codes = block.data.reset_index().code
    print(codes)
    block = qa.QA_fetch_get_stock_block("ths")
    print(block)
    code_list = block[block.blockname == "边缘计算"]["code"].tolist()
    print(code_list)


class Strategy3(qa.QA_Strategy):
    def __init__(self):
        super().__init__()

    def on_bar(self, event):
        print(event)


def get_min_line_from_net():
    data = qa.QAFetch.QATdx.QA_fetch_get_stock_min('000001', '2018-11-01', '2018-12-01', '1min')
    print(data)


def save_stock_min_to_mongo():
    __data = qa.QAFetch.QATdx.QA_fetch_get_stock_min('000001', '2018-11-01', '2018-12-01', '1min')
    print(__data)
    client = DATABASE
    collection = client.stock_min
    collection.create_index(
        [
            ('code',
             pymongo.ASCENDING),
            ('time_stamp',
             pymongo.ASCENDING),
            ('date_stamp',
             pymongo.ASCENDING)
        ]
    )
    if len(__data) > 1:
        collection.insert_many(
            qa.QA_util_to_json_from_pandas(__data)[1:]
        )


if __name__ == '__main__':
    # get_block()

    # get_min_line_from_net()

    # save_stock_min_to_mongo()

    data = qa.QA_fetch_stock_min_adv("000001", '2018-11-01', '2018-12-01', '1min')
    print(data.to_qfq().panel_gen)





