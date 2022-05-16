import search
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI()

@app.get("/tickets/")
async def tickets(
		from_city, from_state, to_city, to_state, day=None, month=None, year=None
	):
	day = day or ""
	month = month or ""
	year = year or ""

	robot = search.SearchTickets(from_city, from_state, to_city, to_state, day, month, year)
	response, status = robot.search()

	return JSONResponse(status_code=status, content={'result': response})

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
    get_swagger_ui_html(openapi_url="api/v1/openapi.json", title="docs")
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi