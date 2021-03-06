

class SearchInSite:


	def __init__(self, soup):
		self.soup = soup

	def _get_element(self, tag, class_element):
		tag = tag or None
		return self.soup.find_all(tag, class_=class_element)

	def get_date_and_time(self):
		passagens = 0
		resultado = {
			'message': 'Nenhuma passagem foi encontrada, tente outra data',
			'sucess': False,
			'objects': [],
		}
		
		for departure, arrival, company, from_city, to_city, price in zip(
			self._get_element("time", "departure-time"), self._get_element("time", "return-time"),
			self._get_element("div", "company"), self._get_element("p", "station-departure"),
			self._get_element("p", "station-arrival"), self._get_element("div", "price")
		):
			passagens += 1
			departure_date_and_time = departure.get("content")
			arrival_date_and_time = arrival.get("content")
			travel_company = company.get("content")
			from_city = from_city.text
			to_city = to_city.text
			price = price.get("data-price")
			if (departure_date_and_time, arrival_date_and_time, travel_company, from_city, to_city):
				resultado['sucess'] = True
				resultado['objects'].append({
					"departure": from_city,
					"arrival": to_city,
					"departure_date": departure_date_and_time,
					"arrival_date": arrival_date_and_time,
					"company": travel_company,
					"price": price,
				})

		if resultado['sucess']:
			message = f'{passagens} passagens' if passagens > 1 else f'{passagens} passagem'
			resultado['message'] = f'A sua busca resultou em: {message}'

		return resultado


"""
Trate os dados!
Tente prever erros caso o site mude os dados que você busca para a api?
Se o usuário digitar números ou caracteres no lugar de Palavras, você vai retornar algum erro para o usuário saber o que precisa fazer? OK
"""
		
