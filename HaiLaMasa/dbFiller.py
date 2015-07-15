import urllib.request
from bs4 import BeautifulSoup
import json
import os
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
ROOT_URL = "http://restaurantebrasov.ro/{}"
def scrape_restaurante_brasov():

    url = "http://restaurantebrasov.ro/lista-restaurante-oras.php?oras=&idOras=1&page={0}"

    results = dict()
    for i in range(9):

        req = urllib.request.Request(
            url.format(i),
            data=None,
            headers={
                'User-Agent': USER_AGENT
            }
        )
        resp = urllib.request.urlopen(req)

        soup = BeautifulSoup(str(resp.read()), "html.parser")
        for list_index in soup.find_all("ul", class_="recipes"):
            for child in list_index.children:
                nav_string = child.find('a')

                if not isinstance(nav_string,int):
                    current_restaurant_url = ROOT_URL.format(nav_string['href'])
                    results[current_restaurant_url] = dict()
                    results[current_restaurant_url]["image_link"]= nav_string.find('img')['src']
                    results[current_restaurant_url].update(get_data_for_restaurant(current_restaurant_url))
    return results

def get_data_for_restaurant(resto_url):
    req = urllib.request.Request(
        resto_url,
        data=None,
        headers={
            'User-Agent': USER_AGENT
            }
        )
    resp = urllib.request.urlopen(req)
    soup = BeautifulSoup(str(resp.read()), "html.parser")
    result = dict()
    for table_data in soup.find_all(class_="blueSpan"):
        field = str(table_data.string)

        father = table_data.parent
        father.span.decompose()
        father.br.decompose()

        father = str(father)
        text = father[father.index(">")+1:father.rindex("<")]
        result[field] = text
    for additional_info in soup.find_all('p',class_="index"):
        result["additional_info"] = ' '.join(string for string in additional_info.contents if isinstance(string, str))
    return result

def save(result_dict):
    with open("scrape_data.json", "w") as fout:
        fout.write(json.dumps(result_dict))

def download_images(result_dict):
    directory = "images"
    if not os.path.exists(directory):
        os.makedirs(directory)
    for link,v in result_dict.items():
        urllib.request.urlretrieve(ROOT_URL.format(v['image_link'][3:]),directory+"/"+v['image_link'][v['image_link'].rindex("/"):])

def load():
    return json.loads(open("scrape_data.json").read())

def populate_db(result_dict):
    from visitor.models import Restaurant,Contact,Address,Gallery
    for k,v in result_dict.items():
        tmp = k[k.rindex("/")+1:].split("-")
        resto_name, resto_city = ' '.join(tmp[:-1]), tmp[-1]
        r = Restaurant(name=resto_name, city=resto_city)
        r.save()
        phone = v['Rezervari:']
        c = Contact(phone = phone,mail="",website="", restaurant = r)
        c.save()
        a = Address(address = v['Adresa:'],restaurant=r)
        a.save()
        img_dir = 'images'+ v['image_link'][v['image_link'].rindex("/"):]
        gallery = Gallery(picture=img_dir,restaurant=r)
        gallery.save()


if __name__ == '__main__':
    pass