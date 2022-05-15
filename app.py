import search
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

@app.get("/tickets/")
async def tickets(
		from_city, from_state, to_city, to_state, day=None, month=None, year=None
	):
	day = day or ""
	month = month or ""
	year = year or ""
	#print(from_city, from_state, to_city, to_state, day, month, year)
	robot = search.SearchTickets(from_city, from_state, to_city, to_state, day, month, year)
	response = robot.search()

	return {'result': response} 

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Buscar Passagens de ônibus",
        version="1.0",
        description="Essa API tem o objetivo de listar passagens disponíveis de ônibus e as suas informações",
        routes=app.routes,
        contact={
           "name": "Pedro Henrique",
           "url": "http://pedro.pythonanywhere.com/",
           "email": "henriquevic012@gmail.com"
       	},
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi