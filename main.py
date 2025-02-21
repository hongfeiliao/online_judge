from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'hello': 'world'}


# 备注：这里使用fastapi cli 启动会更好
# 所以没有使用uvicorn手工启动
#  dev   Run a FastAPI app in development mode.
#  run   Run a FastAPI app in production mode.
#  fastapi dev main.py