from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    Integer,
    PrimaryKeyConstraint,
    Text,
    sql,
)
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from ..config.constants import CASCADE_ALL_DELETE
from .base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    updated_at = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP)
    PrimaryKeyConstraint("id")
