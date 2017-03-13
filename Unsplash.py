page_url = 'https://api.unsplash.com/napi/feeds/home'
Header = {
    'authorization': 'Client-ID d69927c7ea5c770fa2ce9a2f1e3589bd896454f7068f689d8e41a25b54fa6042',
    'accept-version': 'v1',
    'Host': 'unsplash.com',
    'x-unsplash-client': 'web',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36',
    'Referer': 'https://unsplash.com/',
    'Connection': 'keep-alive',
    'Accept': '*/*'
}
import json
import sys
import urllib.request
from multiprocessing import Pool

import requests

images_bianhao = []
for i in range(10):
    req = requests.get(url=page_url, headers=Header)
    content = json.loads(req.text)
    image_bianhao = content['photos']
    bianhaos = [bianhao['id'] for bianhao in image_bianhao]
    images_bianhao.extend(bianhaos)
    page_bianhao = content['next_page'].split('=')[1]
    page_url = 'https://api.unsplash.com/napi/feeds/home?after={}'.format(page_bianhao)


def _print_download_progress(count, block_size, total_size):
    pct_complete = float(count * block_size) / total_size
    msg = "Download progress: {0:.1%}".format(pct_complete)
    print(msg)


def download(image_url):
    urllib.request.urlretrieve(image_url, filename=image_url.split('/')[4] + '.jpg',
                               reporthook=_print_download_progress)


if __name__ == '__main__':
    base_download_url = 'http://unsplash.com/photos/{}/download?force=true'
    image_url = [base_download_url.format(bianhao) for bianhao in images_bianhao]
    pool = Pool()
    pool.map(download, image_url)
