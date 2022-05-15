import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from search_in_site import SearchInSite
from slugify import slugify

class SearchTickets:


    def __init__(self, from_city, from_state, to_city, to_state, day, month, year):
        self.from_city = unidecode(slugify(str(from_city)).strip().lower()) or None
        self.to_city = unidecode(slugify(str(to_city)).strip().lower()) or None
        self.from_state = self.get_state_choice(from_state)
        self.to_state = self.get_state_choice(to_state)
        self.day = day
        self.month = month
        self.year = year

    def get_state_choice(self, state):
        state_formatted = state.strip().lower()
        state_formatted = unidecode(state_formatted)

        ufs = ['ac','al','ap','am','ba','ce','df','es','go','ma','mt','ms','mg',
               'pa','pb','pr','pe','pi','rj','rn','rs','ro','rr','sc','sp','se','to']
        
        states = {
            'acre': 'ac',
            'alagoas': 'al',
            'amapa': 'ap',
            'amazonas': 'am',
            'bahia': 'ba',
            'ceara': 'ce',
            'distrito federal': 'df',
            'espírito santo': 'es',
            'goias': 'go',
            'maranhao': 'ma',
            'mato grosso': 'mt',
            'mato grosso do sul': 'ms',
            'minas gerais': 'mg',
            'para': 'pa',
            'paraiba': 'pb',
            'parana': 'pr',
            'pernambuco': 'pe',
            'piaui': 'pi',
            'rio de janeiro': 'rj',
            'rio grande do norte': 'rn',
            'rio grande do sul': 'rs',
            'rondonia': 'ro',
            'roraima': 'rr',
            'santa catarina': 'sc',
            'sao paulo': 'sp',
            'sergipe': 'se',
            'tocantins': 'to'
        }

        if state_formatted in ufs:
            return state_formatted
        return states.get(state_formatted, None)

    def get_url(self):
        if self.day and self.month and self.year:
            return f"https://www.clickbus.com.br/onibus/{self.from_city}-{self.from_state}/{self.to_city}-{self.to_state}?departureDate={self.year}-{self.month}-{self.day}"
        return f"https://www.clickbus.com.br/onibus/{self.from_city}-{self.from_state}/{self.to_city}-{self.to_state}"

    def get_request(self, attempts):
        for attempt in range(attempts):
            url = self.get_url()
            request = requests.get(url)
            if request.status_code == 200:
                return request
            elif attempt == 0 and request.status_code != 200:
                self.from_state = f'{self.from_state}-todos'
            elif attempt == 1 and request.status_code != 200:
                self.to_state = f'{self.to_state}-todos'
            elif attempt == 2 and request.status_code != 200:
                self.from_state = self.from_state.replace('-todos', '')

    def search(self):
        resultado = {
            'resultado': '',
            'sucesso': False,
            'objects': [],
        }

        if self.from_city and self.from_state and self.to_city and self.to_state:
            request = self.get_request(4)
            if request and request.status_code == 200:
                soup = BeautifulSoup(request.text, 'html.parser')
                search_in_site = SearchInSite(soup)
                return search_in_site.get_date_and_time()
            else:
                resultado.update({
                    'resultado': 'Ops! A requisição não foi atendida, por favor, verifique os dados e tente novamente!',
                    })
                return resultado
        else:
            resultado.update({
                'resultado': 'Você precisa fornecer os dados: CIDADE-ESTADO de origem e destino, DIA/MÊS/ANO são opcionais.'
                })
            return resultado


if __name__ == "__main__":
    from_city = input("Please, type it: from city: \n")
    from_state = input("Please, type it: from state: \n")
    to_city = input("Please, type it: to city: \n")
    to_state = input("Please, type it: to state: \n")
    day = input("Please, type it: day: \n")
    month = input("Please, type it: month: \n")
    year = input("Please, type it: year: \n")
    search_ticket = SearchTickets(from_city, from_state, to_city, to_state, day, month, year)
    search_ticket.search()