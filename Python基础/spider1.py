import requests
from bs4 import BeautifulSoup


def crawl_tieba_posts(tieba_url, num_pages=1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    for page in range(1, num_pages + 1):
        page_url = f"{tieba_url}&pn={page}"
        response = requests.get(page_url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            post_list = soup.find_all('div', class_='threadlist_title')

            for post in post_list:
                title = post.a.get_text(strip=True)
                link = "http://tieba.baidu.com" + post.a['href']
                print(f"标题: {title}\n链接: {link}\n{'-' * 50}")

        else:
            print(f"获取第 {page} 页失败，状态码: {response.status_code}")


if __name__ == "__main__":
    # 替换为你要爬取的贴吧 URL，如 "http://tieba.baidu.com/f?kw=python"
    tieba_url = 'https://tieba.baidu.com/p/8867933306?frwh=index'

    # 设置要爬取的页数，这里设置为1页，你可以根据需要调整
    num_pages = 1

    crawl_tieba_posts(tieba_url, num_pages)
