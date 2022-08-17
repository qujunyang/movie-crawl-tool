import Demo

urlSum = []
names = []
locations = []
kinds = []
languages = []
zz = []
web = []
imagines = []
# number = []


def get():
    R = 0
    import requests
    from bs4 import BeautifulSoup

    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/103.0.0.0 Safari/537.36 '
    }
    html = requests.get('https://www.dytt8.net/html/gndy/jddy/20160320/50523.html', headers=header)
    html.encoding = 'UTF-8'
    soup = BeautifulSoup(html.text, 'html.parser')
    for tag in soup.find_all('a')[19:42]:
        urlSum.append(tag.get('href'))
        # R += 1
        # number.append(R)
        # print(tag.get('href'))
        # print(urlSum)
    # html = requests.get('https://www.dytt8.net/html/gndy/jddy/20160320/50523.html', headers=header)
    print("get()ok")


def final():
    from bs4 import BeautifulSoup
    import requests
    from lxml import etree
    import pandas as pd
    import 测试 as np
    from matplotlib import pyplot as plt
    for i in urlSum:
        place = []
        url = "{}".format(i)
        # url="https://www.ygdy8.com/html/gndy/dyzz/20211122/62056.html"
        # print(url)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
            "Cookie": "XLA_CI=83a58d3aea8b4d52f99c87618e6a29a9; cscpvcouplet5409_fidx=3; cscpvrich4016_fidx=2 "
        }
        res = requests.get(url, headers=header)
        # 修改编码格式“res.apparent_encoding”是更精确的编码格式
        res.encoding = res.apparent_encoding
        response = res.text
        html = etree.HTML(response)
        # 片名
        name = html.xpath('//*[@id="Zoom"]/td/text()[2]')
        o = Demo.find(name)
        a = str(o)[2:]
        names.append(a)
        print(a)
        # 产地
        location = html.xpath('//*[@id="Zoom"]/td/text()[5]')
        place = Demo.find(location)
        a = str(place)[2:]
        locations.append(a)
        print(a)
        # 类别
        variety = html.xpath('//*[@id="Zoom"]/td/text()[6]')
        kind = Demo.find(variety)
        a = str(kind)[2:]
        kinds.append(a)
        print(a)
        # 语言
        speak = html.xpath('//*[@id="Zoom"]/td/text()[7]')
        language = Demo.find(speak)
        a = str(language)[2:]
        languages.append(a)
        print(a)
        # 链接
        link = html.xpath('//*[@id="Zoom"]/td/a/@href')
        # web.append(link[0])
        for j in link:
            web.append(j)
        print(link)
        # 封面
        img = html.xpath('//*[@id="Zoom"]/td/img/@src')
        # for ji in img:
            # web.append(ji)

        imagines.append(img[0])
        print(img)
    print("final()ok")


def toCsv():
    import pandas as pd
    import 测试 as np
    from matplotlib import pyplot as plt

    site = ({
             'film_name': names,
             'film_location': locations,
             'film_kind': kinds,
             'film_language': languages,
             'film_link': web,
             'film_img': imagines
             })
    df = pd.DataFrame(site)
    df.to_excel(r'D:\finally.xlsx', encoding='utf-8')
    print("输入成功")


# names = []
# locations = []
# kinds = []
# languages = []
# zz = []
# web = []
# imagines = []

if __name__ == '__main__':
    get()
    # print(urlSum)
    final()
    toCsv()
