from src.tools.utils import get_url

from bs4 import BeautifulSoup

async def verify_cheater(content):
    url = f"https://tieba.baidu.com/f/search/res?ie=utf-8&qw={content}"
    dt = await get_url(url)
    bs_obj = BeautifulSoup(dt, "html.parser")
    list_ = bs_obj.find(class_ = "s_post_list")
    try:
        objects = list_.find_all(class_ = "s_post")
    except:
        return False
    contents = []
    titles = []
    urls = []
    flag = False
    for i in objects:
        content = i.find(class_ = "p_content").get_text()
        title = i.find(class_ = "bluelink").string
        url = "https://tieba.baidu.com" + i.find(class_ = "bluelink")["href"]
        if content.find("骗子") != -1 or title.find("骗子") != -1:
            return url
    return False