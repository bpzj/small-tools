#!/usr/bin/env python

import sys

"""
    +---------------------------------------+
    |         Keygen for 010 Editor         |
    +---------------------------------------+
    |                                       |
    |   ** FOR EDUCATION PURPOSES ONLY **   |
    |                                       |
    +---------------------------------------+

        _______          ____  ________          ________  ____ 
___  ___\   _  \ _______/_   |/   __   \___  ___/   __   \/_   |
\  \/  //  /_\  \\_  __ \|   |\____    /\  \/  /\____    / |   |
 >    < \  \_/   \|  | \/|   |   /    /  >    <    /    /  |   |
/__/\_ \ \_____  /|__|   |___|  /____/  /__/\_ \  /____/   |___|
      \/       \/                             \/                

"""

raw = [969622712, 594890599, 1593930257, 1052452058, 890701766, 1677293387, 394424968, 266815521, 1532978959, 1211194088, 2019260265, 729421127, 953225874, 1117854514, 892543556, 2000911200, 514538256, 1400963072, 486675118, 1862498216, 1136668818, 758909582, 1653935295, 821063674, 888606944, 687085563, 890056597, 1513495898, 365692427, 184357836, 677395407, 863045227, 818746596, 391985767, 1842768403, 758385145, 1478392706, 1985112985, 1552765320, 746944881, 368385984, 1758203153, 1240817244, 660489060, 756944316, 1290697955, 844453952, 288239112, 1769473626, 1922176006, 826636519, 391520695, 1081548223, 1069693142, 1244729994, 766313326, 1101031894, 624951698, 14501479, 1794907983, 1460682958, 1660839647, 1104890686, 897721119, 1442187162, 480708164, 454443986, 1064446153, 1595150448, 1041527979, 1145775470, 1399869657, 255985995, 802693350, 2005610078, 1897360642, 2146073193, 1538606632, 431647857, 964049561, 395138253, 19164808, 856904574, 730737943, 708645054, 1506870658, 933323739, 819349658, 1780571206, 236747382, 533160167, 2042104933, 670325172, 2040165158, 1354372994, 705785180, 1669754395, 1066536508, 1426207888, 1437950089, 741941201, 796931522, 1694313338, 1290302874, 1367672048, 2039808424, 1062939821, 954597728, 1668694488, 859122242, 1369582617, 140269649, 53024683, 729221831, 816609203, 736893191, 55706320, 262747091, 1629838835, 581764799, 1488480625, 1607077349, 1879925846, 1453945819, 1521965565, 856558562, 1530662365, 1230847072, 1404918182, 1281256849, 1238970765, 272453753, 1640907491, 2127893021, 350314733, 556617458, 654390256, 1648581270, 531062411, 1862873022, 1241517385, 1471028336, 5121143, 1444839026, 1183580211, 1573659650, 2018540230, 1487873223, 234237236, 898254600, 1023090193, 728843548, 2007454357, 1451820833, 267351539, 302982385, 26807015, 865879122, 664886158, 195503981, 1625037691, 1330347906, 1742434311, 1330272217, 1645368040, 542321916, 1782121222, 411042851, 435386250, 1176704752, 1454246199, 1136813916, 1707755005, 224415730, 201138891, 989750331, 1006010278, 1147286905, 406860280, 840388503, 1282017578, 1605698145, 23396724, 862145265, 1898780916, 1855549801, 1571519230, 2083204840, 1859876276, 1602449334, 1009413590, 690816450, 86131931, 345661263, 1565025600, 857544170, 1329948960, 1211787679, 994381573, 991984748, 1956475134, 1098146294, 1655714289, 659576699, 689116467, 1485584392, 451884118, 255590636, 2108114754, 1266252396, 1589326471, 2019907768, 15552498, 1651075358, 614606175, 1656823678, 797605325, 1681594366, 2005080248, 624648446, 884695971, 1526931791, 1595240948, 439447199, 2060396292, 680093752, 409028215, 469068267, 195583689, 1791650630, 507724330, 1364025102, 1094582668, 813049577, 32316922, 1240756058, 1176200235, 2104494066, 325396055, 1796606917, 1709197385, 525495836, 1510101430, 735526761, 767523533, 1374043776, 1559389967, 567085571, 1560216161, 867042846, 1001796703, 1568754293, 628841972, 173812827, 379868455, 384973125]


def decode_uses_left(n):
    n = (n^0x7328b47a)-0x18b3c906^0xbf32abce
    if n % 1179 == 0:
        return n/1179
    else:
        return 0


def encode_uses_left(n):
    return (n*1179^0xbf32abce)+0x18b3c906^0x7328b47a


def encode_name(name, is_not_fc_license, left, n_users):
    ans = 0
    left, n_users, x, y = left*17, n_users*15, 0, 0
    for ch in name:
        char = ord(ch.upper())
        ans += raw[char]
        if is_not_fc_license:
            ans ^= raw[char+13 & 0xff]
            ans *= raw[char+0x2f & 0xff]
            ans += raw[x & 0xff]
        else:
            ans ^= raw[char+0x3f & 0xff]
            ans *= raw[char+0x17 & 0xff]
            ans += raw[y & 0xff]
        ans += raw[left & 0xff]+raw[n_users & 0xff]
        x, y, left, n_users = x+19, y+7, left+9, n_users+13
    return ans


def encode_users(num):
    return (num*11 ^ 0x3421)-0x4d30 ^ 0x7892


def encode_password_date(a, b):
    return (a*17 ^ 0xa8e53167)+0x2c175^0xff22c078^b


def format_license(p):
    ans = []
    for i in range(0, len(p), 2):
        tmp = p[i] << 8 | p[i+1]
        ans.append("%04X" % (tmp & 0xffff))
    return '-'.join(ans)


#
# Version License
#
def generate_license_9c(name, num_users, version):
    p = [0 for _ in range(8)]
    p[3] = 0x9c
    csum = encode_name(name, True, 0, num_users)
    p[4] = csum & 0xff
    p[5] = csum>>8 & 0xff
    p[6] = csum>>16 & 0xff
    p[7] = csum>>24 & 0xff
    t = encode_users(num_users)
    p[2] = p[5]^(t & 0xff)
    p[1] = p[7]^(t>>8 & 0xff)
    t = (version^0xa7)-0x3d ^ 0x18  # p[0]^p[6]
    p[0] = t^p[6]
    return format_license(p)


#
#   Trial License
#
def generate_license_fc(name, offset=365):
    p = [0 for _ in range(8)]
    p[3] = 0xfc
    csum = encode_name(name, False, 0xff, 1)
    p[4] = csum & 0xff
    p[5] = csum>>8 & 0xff
    p[6] = csum>>16 & 0xff
    p[7] = csum>>24 & 0xff
    temp = encode_password_date(offset, csum)
    p[0] = temp & 0xff
    p[1] = temp >> 8 & 0xff
    p[2] = temp >> 16 & 0xff
    return format_license(p)


#
#   Time License
#
def generate_license_ac(name, n_users, days_left):
    # version = 2
    p = [0 for _ in range(10)]
    p[3] = 0xac
    days_left += 0x4596+83
    csum = encode_name(name, True, days_left, n_users)
    p[4] = csum & 0xff
    p[5] = csum>>8 & 0xff
    p[6] = csum>>16 & 0xff
    p[7] = csum>>24 & 0xff
    encoded_date = encode_password_date(days_left, 0x5b8c27)
    enc_users = encode_users(n_users)
    p[2] = p[5]^(enc_users & 0xff)
    p[1] = p[7]^(enc_users>>8 & 0xff)
    p[0] = p[6]^(encoded_date & 0xff)
    p[8] = p[4]^(encoded_date>>8 & 0xff)
    p[9] = p[5]^(encoded_date>>16 & 0xff)
    return format_license(p)


def show_help(program):
    print("""
Usage:
    %s ac <name> <no.of.users> <days>       (Time License)
    %s 9c <name> <no.of.users> <version>    (Version License)
    %s fc <name>                            (Trial License)
    """ % tuple([program]*3))

if __name__ == '__main__':
    print(generate_license_ac("lqt",10,10000))


if len(sys.argv) < 3 or \
    (sys.argv[1] == 'ac' and len(sys.argv) != 5) or \
    (sys.argv[1] == '9c' and len(sys.argv) != 5) or \
    (sys.argv[1] == 'fc' and len(sys.argv) != 3) or \
    sys.argv[1] not in ['ac', '9c', 'fc']:
    show_help(sys.argv[0])
    exit()

if sys.argv[1] == '9c':
    print(generate_license_9c(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))
elif sys.argv[1] == 'fc':
    print(generate_license_fc(sys.argv[2]))
else:
    print(generate_license_ac(sys.argv[2], int(sys.argv[3]), int(sys.argv[4])))



