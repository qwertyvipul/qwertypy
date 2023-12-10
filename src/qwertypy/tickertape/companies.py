from bs4 import BeautifulSoup
import requests

def getCompanyInfo(tt_name):
    """Returns company info of the tt_name"""
    res = requests.get("https://www.tickertape.in/stocks/{}".format(tt_name))
    soup = BeautifulSoup(res.content, "html.parser")
    ticker = soup.find("span", {"class":"ticker"}).text
    name = soup.find("h1", {"class":"security-name"}).text
    return {
        "tt_name": tt_name,
        "name": name,
        "ticker": ticker
    }

def getTopCompanies():
    """Returns the list of tt_name of top companies"""
    res = requests.get("https://www.tickertape.in/stocks?filter=top")
    soup = BeautifulSoup(res.content, "html.parser")
    
    pageDiv = soup.find("div", {"class":"page"})
    lis = pageDiv.find_all("li")
    
    topCompanies = []
    for li in lis:
        tt_name = li.find("a").get("href").split("/stocks/")[-1]
        topCompanies.append(tt_name)
    return topCompanies

def getAllCompanies():
    """Returns the list of tt_name of all companies"""
    res = requests.get("https://www.tickertape.in/stocks")
    soup = BeautifulSoup(res.content, "html.parser")
    links_div = soup.find("div", {"class":"link-list"})
    alinks = links_div.find_all("a")
    
    allCompanies = []
    temp_names = []
    for alink in alinks:
        ares = requests.get("https://www.tickertape.in/stocks?filter={}".format(alink.text))
        asoup = BeautifulSoup(ares.content, "html.parser")
        
        pageDiv = asoup.find("div", {"class":"page"})
        if not pageDiv:
            continue
        lis = pageDiv.find_all("li")
    
        for li in lis:
            tt_name = li.find("a").get("href").split("/stocks/")[-1]
            if not tt_name in temp_names:
                try:
                    temp_names.append(tt_name)
                    allCompanies.append(tt_name)
                except:
                    continue
    return allCompanies