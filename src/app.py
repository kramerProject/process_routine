from __utils.parser import Parser
from model.db import DBConnection
from model.purchase import PurchaseModel
from services.purchase import Purchase
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True, slots=True)
class ProcessRoutine():


    output: Any


    def start_processing(self):
        with open("./src/data.txt") as file:
            purchase_list = file.readlines()
        for purchase in purchase_list[1:]:
            item = purchase.split(" ")
            line = list(filter(lambda item: item, item))
            self._parse_lines(line)

    def _parse_lines(self, line):
        purchase = Parser().parse_line(line)
        return self._validate_data(purchase)

    def _validate_data(self, purchase):
        purchase = Purchase(
                cpf=purchase["cpf"],
                private=purchase["private"],
                incomplete=purchase["incomplete"],
                last_purchase=purchase["lastPurchase"],
                average_purchase_price=purchase["averagePurchasePrice"],
                last_purchase_price=purchase["lastPurchasePrice"],
                most_frequent_store=purchase["mostFrequentStore"],
                last_purchase_store=purchase["lastPurchaseStore"]
        )
        
        if purchase.validate():
            return self.dispatch_output(purchase)

    def dispatch_output(self, purchase):
        print("Saving to DB")
        with DBConnection() as db:
            new_purchase = PurchaseModel(
                cpf=purchase.cpf,
                pvt=purchase.private,
                incomplete=purchase.incomplete,
                last_purchase=purchase.last_purchase,
                average_purchase_price=purchase.average_purchase_price,
                last_purchase_price=purchase.last_purchase_price,
                most_frequent_store=purchase.most_frequent_store,
                last_purchase_store=purchase.last_purchase_store
            )
            db.session.add(new_purchase)
            db.session.commit()
        print("Inserted")





if __name__ == '__main__':
    print("START PROCESSING")
    process_routine = ProcessRoutine(output=[])
    process_routine.start_processing()