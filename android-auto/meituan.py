from time import sleep

import uiautomator2 as u2


if __name__ == '__main__':
    d = u2.connect()
    d.app_stop("com.sankuai.meituan")
    d.app_start("com.sankuai.meituan")
    sleep(5)
    d(description="红包签到").click()
    sleep(5)
    d.click(0.688, 0.577)




