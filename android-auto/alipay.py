from time import sleep

import uiautomator2 as u2
import common


if __name__ == '__main__':
    d = u2.connect()
    d.app_stop("com.eg.android.AlipayGphone")
    d.app_start("com.eg.android.AlipayGphone")
    sleep(3)
    d(resourceId="com.alipay.android.phone.wealth.home:id/sigle_tab_bg").click()
    sleep(3)
    # 使用正则
    # if d(textMatches='.*个积分待领取').exists():
    if d(textMatches='.*支付宝会员').exists():
    # 使用xpath
    # if d.xpath('//*[contains(@text, "个积分待领取")]').exists:
        d(textMatches='.*支付宝会员').click()
        sleep(5)
        ui = common.current_ui()
        print(ui)
        common.tap_by_content_regexp(r'''领积分.*?bounds="(\[.*?\])"''',ui)

    else:
        print("没有未领取的积分")

