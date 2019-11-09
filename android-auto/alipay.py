import common

if __name__ == '__main__':
    common.link_device()
    common.kill_app(r"com.eg.android.AlipayGphone")
    common.open_app(r"com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin")
    common.tap_by_content_regexp(r'''android:id/tabs.*?我的.*?id/tab_description.*?bounds="(\[.*?\])"''')
    ui = common.current_ui()
    if "积分待领取" in ui:
        common.tap_by_content_regexp(r'''支付宝会员.*?id/item_left_text.*?bounds="(\[.*?\])"''', ui)
    else:
        print("没有未领取的积分")
        exit(0)

    ui = common.current_ui()
    print(ui)
    if "领积分" in ui:
        common.tap_by_content_regexp(r'''领积分.*?bounds="(\[.*?\])"''', ui)

    ui = common.current_ui()
    if "点击领取" in ui:
        common.tap_by_content_regexp(r'''点击领取.*?bounds="(\[.*?\])"''', ui)
