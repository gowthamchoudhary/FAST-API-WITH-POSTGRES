from fastapi import FastAPI,HTTPException,Depends,Query
from databases import Database
from sqlalchemy import select
from app.models import tasks


app = FastAPI()


@app.post("/tasks/")
async def create_tasks(title:str,description:str=""):
    query  = tasks.insert().values(title=title,description=description)
    await database.execute(query)
    return {
        "message":"Put GOd first"
    }
@app.put("/tasks/{task_id}/")
async def update_task(task_id:int,
                      title:str,
                      description:str=""):
    query = tasks.update().where(tasks.c.id==task_id).values(title=title,description=description)
    await database.execute(query)
    return {
        "message":"Put God first"
    }
@app.get("/tasks/task_id/")
async def get_task(task_id:int):
    query = select([tasks]).where(tasks.c.id==task_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404,detail="Put God First")
    return result
@app.get("/tasks/")
async def get_tasks():
    query = tasks.select([tasks])
    result = await database.fetch_all(query)
    return result
@app.delete("/task_id/")
async def delete_task(task_id:int):
    query = tasks.delete().where(tasks.c.id==task_id)
    result = await database.execute(query)
    return {"message":"Put God First"}
