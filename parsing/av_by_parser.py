from bs4 import BeautifulSoup
import requests
import lxml


def get_html(url):
    # передаваемые заголовки
    headers = {"Accept": "*/*",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/112.0.0.0 Safari/537.36"}
    req = requests.get(url, verify=False, headers=headers)
    # print(req.text)
    return req


# print(get_html("https://av.by"))

def parse(html):
    soup = BeautifulSoup(get_html(html).text, "html.parser")
    # link_tag = soup.link
    # print(link_tag)
    # print(link_tag["href"])

    # title_tag = soup.title
    # print(title_tag)
    # print(title_tag.string)  # .string убирает <тег> в консоли

    # print(soup.find_all("p"))

    # head_tag = soup.head
    # print(head_tag)
    # print(head_tag.contents)
    # head_tag_contents = soup.head
    # for tags in head_tag_contents.descendants:
    #     print(tags.name)
    """
    .descendants - атрибут, который позволяет рекурсивно проходить по вложенным тегам.
    .children - благодаря .children мы получаем генератор, через который сможем сразу проходить циклом по всем вложенным тегам.
    .parent – атрибут, который позволяет получить информацию о теге, в котором содержится тег, который который мы проверяем.
    .parents – атрибут, который позволяет получить информацию о всех тегах верхнего уровня, в котором находится проверяемый тег.
    """

    # print(soup.find_all("title"))
    # p_tag_list = soup.find_all("p")
    # for item in p_tag_list:
    #     print(item)
    # return soup

    # catalog_list = soup.find_all("li", "catalog__item")
    # for item in catalog_list:
    #     print(item.a.attrs.get("href"))
    # return soup

    # links_soup = soup.find_all("a", "catalog__link")
    # links_list = [a_tag.attrs.get("href") for a_tag in links_soup]
    # print(links_list)

    # manufacturers_soup = soup.find_all("span", "catalog__title")
    # manufacturers_list = [span_tag.text for span_tag in manufacturers_soup]
    # print(manufacturers_list)

    price_byn = soup.find_all("div", "listing-item__price")
    price_list = []
    for price in price_byn:
        price_encode = price.text.encode("ascii", errors="ignore")
        price_decode = price_encode.decode("utf-8")
        price_list.append(int(price_decode[:price_decode.index(".")]))
    print(f"Средняя цена Альфа-Ромео: {sum(price_list) // len(price_list)}")
    print(f"Максимальная цена Альфа-Ромео: {max(price_list)}")
    print(f"Минимальная цена Альфа-Ромео: {min(price_list)}")
    return soup


# parse("https://av.by")
parse("https://cars.av.by/alfa-romeo")
