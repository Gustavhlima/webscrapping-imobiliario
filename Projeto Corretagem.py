import pymysql
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# conexao = pymysql.connect(host='mysql-135933-0.cloudclusters.net',
#                           user='gustavo_lima',
#                           password='Glima@acction',
#                           database='DB_GUSTAVO_LIMA',
#                           port=10003)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.apolar.com.br/alugar/apartamento/curitiba?mensal&city=Curitiba&property_type=Apartamento&property_type=Casa&price_max=R%24%203.000,00&price_min=R%24%200,00')
sleep(10)

bloco_casas = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section/div/div[2]/div[2]')
lista_casas = bloco_casas.find_elements(By.TAG_NAME, 'a')
print(len(lista_casas))
casas = []
for casa in lista_casas:
    try:
        link = casa.get_attribute('href')
        casas.append(link)
    except:
        continue
cont = 0
for url in set(casas):
    print('-' * 50)
    cont += 1
    print(cont)
    driver.get(url)
    sleep(12)
    endereco = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/div/div/div[1]/div/div/a').text
    endereco = endereco.split(',')
    rua = endereco[0].strip()
    numero = endereco[1].strip()
    regiao = endereco[2].split('-')
    bairro = regiao[0].strip()
    cidade = regiao[1].strip()
    tabela_valores = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/div/div/div[2]/section/div/div/div/div[1]/table')
    valores = tabela_valores.find_elements(By.TAG_NAME, 'tr')
    print(endereco)

    for valor in valores:
        viptu = 0
        vseguro = 0
        vcondo = 0
        print('-' * 50)
        #print(valor.text)
        if 'IPTU' in valor.text:
            viptu = valor.find_elements(By.TAG_NAME, 'td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            print(f'IPTU', viptu)
        elif 'Aluguel' in valor.text:
            valuguel = valor.find_elements(By.TAG_NAME, 'td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            print(f'Aluguel', valuguel)
        elif 'Seguro Incêndio' in valor.text:
            vseguro = valor.find_elements(By.TAG_NAME, 'td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            print(f'Seguro', vseguro)
        elif 'Condomínio' in valor.text:
            vcondo = valor.find_elements(By.TAG_NAME, 'td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            print(f'Condomínio', vcondo)
        elif 'Total' in valor.text:
            vtotal = valor.find_elements(By.TAG_NAME, 'td')[1].text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            print(f'Total', vtotal)
        print('-' * 50)
    lista_highlights = driver.find_element(By.CLASS_NAME, 'property-highlights').find_elements(By.TAG_NAME, 'li')
    for item in lista_highlights:
        print(item.text)
