from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from models import awsModel
from schemas.awsSchema import Tenant, Costs



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]


# create the tenant data
@router.post('/create-tenant')
def create_tenant(tenant:Tenant , db:db_dependency):
    create_tenant = awsModel.Tenant(**tenant.dict())
    db.add(create_tenant)
    db.commit()
    db.refresh(create_tenant)
    return {
        'success':True,
        'message':'Tenant created successfully'
    }
    

# get all tenants data
@router.get('/get-tenants')
def get_tenants(db:db_dependency):
    tenants = db.query(awsModel.Tenant).all()
    return tenants


# create cost
@router.post('/create-cost')
def create_cost(costs:Costs,db:db_dependency):
    create_cost = awsModel.Costs(**costs.dict())
    db.add(create_cost)
    db.commit()
    db.refresh(create_cost)
    return {
        'success':True,
        'message':'Cost added successfully'
    }

# get cost
@router.get('/get-costs')
def get_costs(db:db_dependency):
    costs = db.query(awsModel.Costs).all()
    return costs