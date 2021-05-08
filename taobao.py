import requests
import re


def getHTMLText(url):
    kv={
        'cookie': 't=9ec7209ff601ac0c23427f62908b42af; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; cna=U7x8F9Wb73MCAbckUrCjI6ra; _m_h5_tk=0968c48b3998d02039ebfd01cfdf1319_1620463229925; _m_h5_tk_enc=ac95a176e7d2ca49241f418368df8084; _tb_token_=5373343859e3b; xlly_s=1; cookie2=151999da668fb808367798645c30c710; v=0; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _uab_collina=162045570479195492020648; _samesite_flag_=true; unb=111702062; uc3=id2=UoCIQetnfyMe&nk2=EFY193GQ6QUn&vt3=F8dCuwgubSOCSOOsMqg%3D&lg2=UIHiLt3xD8xYTw%3D%3D; csg=1b404324; lgc=shan50054; cookie17=UoCIQetnfyMe; sgcookie=E100AGZzhKlqxgnXoQxm7eSNHn5NOUCUII6PS4zCjd3mMItNzcj0FpBwUa1oejwR2WbV6xm%2Bg9kgeK80013axkzcWQ%3D%3D; dnk=shan50054; skt=60d7c6d7c1c4d8c3; existShop=MTYyMDQ1ODUzMA%3D%3D; uc4=nk4=0%40Eo9LPQia7VZ%2B69QkNSicSwZI4RM%3D&id4=0%40UOg0M1CsJrl1Trfcm7cByJozZs4%3D; tracknick=shan50054; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=42e; _nk_=shan50054; cookie1=BvLZXAjTAtvknHL01uSa3Deai6PSj88hher2pxipU3M%3D; enc=WCQKfoUgQhb5k1H8ZCQQydkxa24Ub49BCGPFVMkmzBPplB3oaM5ZSdIooguLgKQgILnqi%2FW9hkCIgm5eJNn3IQ%3D%3D; mt=ci=63_1; uc1=cookie14=Uoe2zX5dg3jzAw%3D%3D&pas=0&cookie21=W5iHLLyFe3xm&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D; x5sec=7b227365617263686170703b32223a223463363164363965323732356135343234636537336264663363373063393932434d475032595147454b57636a6f6d483575657374674561437a45784d5463774d6a41324d6a73784d4b6546677037382f2f2f2f2f77453d227d; JSESSIONID=56AB36C5DBABBDFF705B2303B2C49AAC; isg=BBISyB5Jpjs_LNpbVkfuvYcoY9j0Ixa92Pq4VNxrN0Ww77LpxLZ4zJwNW0tTn45V; tfstk=c4_CBwGF9vDIoKZr86NZY9cH6IY5ZncXNk9hOiU3r6T_AK5Ci2g2hBQFqY39DC1..; l=eBr0tS9njmGYRrZsBOfwourza77tjIRAguPzaNbMiOCP_85p5s2PW66yh489CnGVh6jpR3-IkQOyBeYBqIv4n5U62j-lasMmn',
        'user-agent':'Mozilla/5.0'
    }
    try:
        r = requests.get(url, headers=kv,timeout=300)
        # r=requests.get(url,timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        pri = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) #价格
        plt = re.findall(r'\"view_sales\"\:\".*?\"', html)#销量
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)#名称

        for i in range(len(plt)):
            pricc=eval(pri[i].split(':')[1])  #价格
            price = eval(plt[i].split(':')[1])#销量
            title = eval(tlt[i].split(':')[1])#名称
            # numi=eval(num[i].split(':')[1])
            ilt.append([pricc,price, title])
    except:
        print("")


def printGoodsList(ilt):

    tplt = "{:4}\t{:6}\t{:8}\t{:10}"
    print(tplt.format("序号","价格", "销量","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1],g[2]))


def main():
    goods = '小米手机'
    depth = 10
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            # print(html)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()

