import os
import requests
# URL 소스 : http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1015&weekday=tue # - 덴마. 3-12화 1. 다이크(12)
image_urls = [
    'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_1.jpg',
    'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_2.jpg',
    'http://imgcomic.naver.net/webtoon/119874/1015/20170528204207_6e9df8e618b97520233bbb35e7d4eaaf_IMAG01_3.jpg',
]
for image_url in image_urls:
    headers = {
        'Referer': 'http://comic.naver.com/webtoon/detail.nhn?titleId=119874&no=1015&weekday=tue',
    }
    response = requests.get(image_url, headers=headers)
    image_data = response.content
    filename = os.path.basename(image_url)
    with open(filename, 'wb') as f:
        print('writing to {} ({} bytes)'.format(filename, len(image_data)))
        f.write(image_data)