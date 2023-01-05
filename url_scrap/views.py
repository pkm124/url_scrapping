from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd

def url_scrap(request):

    try:
        url = request.GET['url']
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        page_title = soup.title.text

        text = page.text
        status = page.status_code

        page_head = soup.head
        page_body = soup.body

        set_url=set()
        for i in soup.select('a'):
            if i.get('href')[0] == '/' and i.get('href') != '/':
                set_url.add(i.get('href'))

        # print(set_url)

        for i in list(set_url):
            print(i)
            
        df = pd.DataFrame({'Domain Name':url, 'Url Links':list(set_url)})
        writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=False)

        writer.close()
        return render(request,"url_scrap.html")
    except:
        return render(request,"url_scrap.html")
