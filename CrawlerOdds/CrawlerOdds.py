from selenium import webdriver
from bs4 import BeautifulSoup
import csv

url = "https://1xbet.cm/en/live/Football/"

csv_columns = ['match', 'casa', 'empate', 'fora', 'casa_marca', 'ambos_marcam', 'fora_marca', '1tempo_casa', '1tempo_empate', '1tempo_fora', 'placar_exato', 'num_gols_partida', 'num_gols_casa', 'num_gols_fora', 'placar_exato1t', 'placar_extato2t', '2tempo_casa', '2tempo_empate', '2tempo_fora']
csv_file = open("crawodds.csv", "w", encoding = "utf-8", newline = "")
writer = csv.DictWriter(csv_file, fieldnames = csv_columns)
writer.writeheader()

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

def listtodict(listaA, listaB):
    zippedlist = zip(listaA, listaB)
    op = dict(zippedlist)
    return op

containers = soup.findAll("div", {"class": "c-events__item_col"})
for container in containers:
    teams = [x.get_text() for x in container.findAll("span", {"class": "c-events__teams"})]
    odds = [x.attrs.get('data-coef') for x in container.findAll("a", {"class": "c-bets__bet"})]
       
    match_columns = ['match']
    odds_columns = [ 'casa', 'empate', 'fora', 'casa_marca', 'ambos_marcam', 'fora_marca', '1tempo_casa', '1tempo_empate', '1tempo_fora', 'placar_exato', 'num_gols_partida', 'num_gols_casa', 'num_gols_fora', 'placar_exato1t', 'placar_extato2t', '2tempo_casa', '2tempo_empate', '2tempo_fora']
      
    d_teams = listtodict(match_columns, teams)
    d_odds = listtodict(odds_columns, odds)
   
    d_teams.update(d_odds)
    
    writer.writerow(d_teams)
    
csv_file.close()
print("Concluído!")
driver.close()