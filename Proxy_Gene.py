class TPCT_PROXY_GENE:
    import random, requests.sessions, requests
    from robobrowser import RoboBrowser
    import threading
    '''
     _____ ____   ____   ___ _____  _____ ____   ____ _____
    |  ___| __ ) | __ ) / _ \_   _ |_   _|  _ \ / ___|_   _|
    | |_  |  _ \ |  _ \| | | || |    | | | |_) | |     | |
    |  _| | |_)  | |_) | |_| || |    | | |  __/| |___  | |
    |_|   |____/ |____/ \___/ |_|    |_| |_|    \____| |_|
                                                          '''

    UserAgents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100409 Firefox/3.6.3 CometBird/3.6.3']
    browser = RoboBrowser(history=True, user_agent=UserAgents[random.randint(0, len(UserAgents) - 1)],
                           multiplier=True, parser='lxml')
    def __init__(self):
        self.proxy_gene()

    def proxy_gene(self):
        self.browser.open('https://www.hide-my-ip.com/proxylist.shtml')
        Data = \
            str(str(self.browser.find_all('script', {'type': 'text/javascript'})[4]).split('=')[2]).split(
                '<!-- proxylist -->')[0]
        data = ''
        a = 0
        proxy_info = ''
        for x in Data.split(':'):
            if a < 9:
                data += x
                a += 1
            else:
                data = data.replace(' ', '')
                data = data.replace('', '')
                data = data.replace("\n", '')
                if data.startswith('[{') or data.startswith('{'):
                    try:
                        formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                        proxy_info += formula + "\n"
                    except:
                        formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                        proxy_info += formula + "\n"
                else:
                    try:
                        if data.endswith('"s"'):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                            proxy_info += formula + "\n"
                        elif data.endswith('"f"'):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                            proxy_info += formula + "\n"
                        elif data.endswith('"t"'):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split(',')[0].split('"')[1]
                            proxy_info += formula + "\n"
                        elif data.endswith('"p"'):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split(',')[0].split('"')[1]
                            proxy_info += formula + "\n"
                        else:
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                            proxy_info += formula + "\n"
                    except:
                        if data.endswith('"i"'):
                            proxy_info += formula + "\n"
                        elif data.endswith("tp"):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                            proxy_info += formula + "\n"
                        elif data.endswith("n"):
                            formula = data.split('"i"')[1].split('"')[1] + ":" + data.split('"p"')[1].split('"')[1]
                            proxy_info += formula + "\n"

                a = 0
                data = ''
        self.browser.open('https://www.us-proxy.org/')
        a = 0
        pro = ''
        for proxie in self.browser.find_all('td'):
            if str(proxie.text).lower() != 'elite proxy' or str(proxie.text).lower() != 'anonymous' or str(
                    proxie.text).lower() != 'transparent' or str(proxie.text).lower() != 'no' or str(proxie.text).lower() != 'yes':
                if a < 7:
                    if a == 0 and not proxy_info.__contains__(proxie.text):
                        pro += proxie.text + ":"
                    elif a < 6:
                        pro += proxie.text + ":"
                    else:
                        pass
                    a += 1
                else:
                    a = 0
                    pro = ''
        self.browser.open('https://www.sslproxies.org/')
        for tr in self.browser.find_all('tr'):
            try:
                x = 0
                ip = ''
                for td in tr.find_all('td'):
                    if x == 0:
                        ip += td.text
                        x += 1
                    elif x == 1:
                        x += 1
                        ip += ':' + td.text
                        proxy_info += ip + "\n"
                        break
            except:
                pass
        self.browser.open('https://incloak.com/proxy-list/#list')
        for tr in self.browser.find_all('tr'):
            try:
                proxy_info += tr.find_all('td')[0].text + ':' + tr.find_all('td')[1].text+"\n"
            except:
                pass
        self.browser.open('http://ipaddress.com/proxy-list/')
        for tr in self.browser.find_all('tr'):
            try:
                if tr.find_all('td')[0].text.__contains__(':'):
                    proxy_info += tr.find_all('td')[0].text + "\n"
            except:
                pass
        proxy_info = proxy_info.split("\n")
        self.random.shuffle(proxy_info)
        return proxy_info

TPCT_PROXY_GENE()
