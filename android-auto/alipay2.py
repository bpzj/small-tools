from time import sleep

import common


def ling_ji_fen():
    common.link_device()
    common.kill_app(r"com.eg.android.AlipayGphone")
    common.open_app(r"com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin")
    common.tap_by_content_regexp(r'''android:id/tabs.*?我的.*?id/tab_description.*?bounds="(\[.*?\])"''')
    sleep(5)
    ui = common.current_ui()
    if "积分待领取" in ui:
        common.tap_by_content_regexp(r'''支付宝会员.*?id/item_left_text.*?bounds="(\[.*?\])"''', ui)
    else:
        print("没有未领取的积分")
        exit(0)

    ui = common.current_ui()
    if "领积分" in ui:
        common.tap_by_content_regexp(r'''领积分.*?bounds="(\[.*?\])"''', ui)

    ui = common.current_ui()
    if "点击领取" in ui:
        common.tap_by_content_regexp(r'''点击领取.*?bounds="(\[.*?\])"''', ui)


if __name__ == '__main__':
    ling_ji_fen()
