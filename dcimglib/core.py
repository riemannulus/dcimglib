import requests


class Downloader:

    def __init__(self, gall_url):
        self.headers = {
            'Host': 'image.dcinside.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Sec-Fetch-Site': 'same-site',
            'Referer': gall_url,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6,en;q=0.5,es;q=0.4',
        }

        self.session = requests.Session()
        self.session.get(gall_url)

    def download(self, url, file_path, is_raw=False):
        r = requests.get(url,
                         headers=self.headers,
                         cookies=self.session.cookies.get_dict())

        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(r.content)

        return r.status_code
