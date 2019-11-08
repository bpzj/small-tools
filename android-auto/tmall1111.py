import common

if __name__ == '__main__':
    # common.link_device()
    # common.monkey_app(r"com.tmall.wireless")
    ui = common.current_ui()
    print(ui)
    if "积分待领取" in ui:
        common.tap_by_content_regexp(r'''支付宝会员.*?id/item_left_text.*?bounds="(\[.*?\])"''', ui)
    else:
        print("没有未领取的积分")
        exit(0)

    # ui = common.current_ui()
    # if "领积分" in ui:
    #     common.tap_by_content_regexp(r'''支付宝会员.*?id/item_left_text.*?bounds="(\[.*?\])"''', ui)

