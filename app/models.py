from sqlalchemy import Column ,Integer,String,Table
from app.config import metadata

tasks  = Table(
    "tasks",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("title",String(100), nullable=False),
    Column("description",String(255)),
)