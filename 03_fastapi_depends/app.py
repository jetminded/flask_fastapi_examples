from fastapi import FastAPI, Depends

app = FastAPI()

# Dependency function
def get_query_token(token: str = None): # токен - query param у функции. Это подставляет сам фастапи.
    if token != "secret":
        return {"error": "Invalid token"}
    return {"token": token}

@app.get("/items/")
def read_items(dep=Depends(get_query_token)):
    return {"message": "Success", "dep": dep}


# аналогично можно устроить пагинацию

def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/products/")
def get_products(paging: dict = Depends(pagination)):
    return {"paging": paging}



# Аналогичная фишка как с декораторами - можем делать зависимость на класс
class CommonQueryParams:
    def __init__(self, q: str = None, limit: int = 10):
        self.q = q
        self.limit = limit

@app.get("/search/")
def search(params: CommonQueryParams = Depends()):
    return {
        "query": params.q,
        "limit": params.limit
    }




# важно! фишка с yield как у фикстур СОХРАНЯЕТСЯ!

def get_db():
    db = "fake-db-session"
    try:
        yield db
    finally:
        print("Closing DB") # почистится после завершения ф-ии db_test

@app.get("/db-test/")
def db_test(db = Depends(get_db)):
    return {"db": db}