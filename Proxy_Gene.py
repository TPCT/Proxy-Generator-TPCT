class TPCT_PROXY_GENE:

    def __init__(self):
        self.Installer()
        self.plateform_check()
        self.proxy_gene()

    class Installer:
        import os, shutil
        def __init__(self):
            self.Admin_Rights()
            self.Import_Checker()

        def Admin_Rights(self):
            try:
                import os, sys, platform
                if str(platform.system()).lower().startswith('linux'):
                    open('/etc/Mod', 'w+')
                    os.unlink('/etc/Mod')
                elif str(platform.system()).lower().startswith('windows'):
                    open('c:/Mod', 'w+')
                    os.unlink('c:/Mod')
                else:
                    open('/etc/Mod', 'w+')
                    os.unlink('/etc/Mod')
            except KeyboardInterrupt as e:
                self.os._exit(1)
            except Exception as e:
                e = e.args
                if e[0] == 13:
                    print('[+] Sorry You Need To Use Script As Admin Script Will Exit')
                    sys.exit(1)
                else:
                    pass

        def Import_Checker(self):
            try:
                __import__('imp').find_module('robobrowser')
            except ImportError:
                import pip
                pip.main(['install', 'robobrowser'])
                pass
    import platform,random,string
    browser = ''
    Browser = ''

    def plateform_check(self):
        from robobrowser import RoboBrowser
        if str(self.platform.system()).lower().startswith('linux'):
            browser = RoboBrowser(
                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                multiplier=True,
                allow_redirects=True, history=True, parser='lxml')
            self.browser = browser
        elif str(self.platform.system()).lower().startswith('windows'):
            browser = RoboBrowser(
                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                multiplier=True,
                allow_redirects=True, history=True, parser='html.parser')
            self.browser = browser
        else:
            browser = RoboBrowser(
                user_agent='Mozilla/5.0 (Macintosh; PPC Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0',
                multiplier=True,
                allow_redirects=True, history=True, parser='lxml')
            self.browser = browser
    UserAgents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                  'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100409 Firefox/3.6.3 CometBird/3.6.3']

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
        for proxy in proxy_info:
            open('proxies.list', 'a+').write(str(proxy)+"\n")

TPCT_PROXY_GENE()
