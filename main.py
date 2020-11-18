import mechanicalsoup
import pandas as pd

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://responsavel.agendaedu.com/")
browser.select_form('form[action="/responsibles/sign_in"]')
browser["responsible[login]"] = ""
browser["responsible[password]"] = ""
browser.submit_selected()

for date in pd.date_range(start=pd.Timestamp('2020-09-14', tz='America/Fortaleza'), end=pd.Timestamp.today(tz='America/Fortaleza'), freq='B', tz='America/Fortaleza'):
    print('Buscando informações da data %s' % date.strftime('%Y-%m-%d'))
    browser.open(
        "https://responsavel.agendaedu.com/responsibles/daily_summaries/%s" % date.strftime('%Y-%m-%d'))
    page = browser.get_current_page()
    browser.launch_browser()
    break
