from fastapi import FastAPI
from models import userModel, awsModel
from database import engine
from routes import user, awsRoute

import uvicorn

app = FastAPI()
userModel.Base.metadata.create_all(bind=engine)
awsModel.Base.metadata.create_all(bind=engine)

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

app.include_router(user.router,prefix='/user')
app.include_router(awsRoute.router, prefix='/aws')

if __name__ == '__main__':
    uvicorn.run(app,port=8080)