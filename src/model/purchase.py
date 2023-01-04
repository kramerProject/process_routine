from sqlalchemy import Column, String, Integer, Boolean, Float
from sqlalchemy.sql.expression import true
from model.base import Base

class PurchaseModel(Base):

    __tablename__ = "purchases"

    id = Column(Integer, primary_key=true)
    cpf = Column(String)
    pvt = Column(Boolean)
    incomplete = Column(Boolean)
    last_purchase = Column(String)
    average_purchase_price = Column(Float)
    last_purchase_price = Column(Float)
    most_frequent_store = Column(String)
    last_purchase_store = Column(String)

    def __repr__(self) -> str:
        return f"Users [name={self.cpf}]"