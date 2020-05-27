import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

# <title>
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# <singer>
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis


# <rank>
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

# <td class="number">2
#          <span class="rank">
#               <span class="rank">
#                   <span class="rank-up">2
#                       <span class="hide">상승
#                       </span>
#                   </span>
#               </span>
#           </span>
# </td>




trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:

    title = tr.select_one('td.info > a')
    singer = tr.select_one('td.info > a.artist.ellipsis')
    rank = tr.select_one('td.number')

    if title is not None:
        song = title.text.strip() 
        singers = singer.text.strip()
        ranks = rank.text.strip()

        print(ranks, song, singers)