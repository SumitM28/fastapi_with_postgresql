from fastapi import FastAPI
import model
from database import engine
from routes.user import router as userRoutes
import uvicorn

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return {
        'success':True,
        'message':'API running successfully'
    }


@app.get('/get-health')
def get_health():
    return {
        'success':True,
        'message':'Your application health is good'
    }

app.include_router(userRoutes,prefix='/user')


if __name__ == '__main__':
    uvicorn.run(app,port=8080)