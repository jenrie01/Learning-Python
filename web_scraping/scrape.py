import requests
from bs4 import BeautifulSoup
import pprint
import itertools

# res = requests.get('https://news.ycombinator.com/')
# res2 = requests.get('https://news.ycombinator.com/news?p=2')
# soup = BeautifulSoup(res.text, 'html.parser')
# soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup)
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a')
# print(soup.title)
# print(soup.a)
# print(soup.find(id='score_23933879'))
# print(soup.select('.score'))
# print(soup.select('#score_23933879'))
# links = soup.select('.storylink')
# links2 = soup2.select('.storylink')
# subtext = soup.select('.subtext')  # votes = soup.select('.score')
# print(votes[0].get('id'))
# subtext2 = soup2.select('.subtext')

# combined_links = links + links2
# combined_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['upvotes'], reverse=True)


def create_custom_hn(links, subtext):  # votes
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # points = votes[idx].getText()
            # rp = points[:-6]
            if points > 100:  # int(rp)
                hn.append({'title': title, 'link': href, 'upvotes': points})
    # return sorted(hn, key=lambda i: i['upvotes'], reverse=True)
    return sort_stories_by_votes(hn)


def page_combiner(num_pages):
    res_list = ['https://news.ycombinator.com/']
    combined_links = []
    combined_subtext = []

    for l in range(2, num_pages):
        res_list.append(f'https://news.ycombinator.com/news?p={l}')
    for index, link in enumerate(res_list):
        res = requests.get(f'{link}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        combined_links.append(links)
        combined_subtext.append(subtext)

    li_links = itertools.chain(*combined_links)
    li_subtext = itertools.chain(*combined_subtext)
    return create_custom_hn(list(li_links), list(li_subtext))


pprint.pprint(page_combiner(9))
