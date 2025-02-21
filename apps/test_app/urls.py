from fastapi import APIRouter

test_app = APIRouter()

@test_app.get('/')
async def root():
    return {'app_name': 'test_app'}


