import unittest
import json

from __utils.parser import Parser
from services.purchase import Purchase


def load_data():
    with open("tests/files/expected_line.json", "r") as f:
            expected = json.loads(f.read())
    return expected

class ParserTests(unittest.TestCase):


    def test_should_parse_line(self):
        line = ['042.098.288-40', '0', '0', '2013-06-12', '161,22', '161,22', '79.379.491/0008-50', '79.379.491/0008-50']
        expected = load_data()

        produced = Parser().parse_line(line)
        
        self.assertEqual(expected, produced)

    def test_should_validate_data(self):
        purchase = load_data()

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
        print("purrrr", purchase.validate())
        self.assertTrue(purchase.validate())




if __name__ == '__main__':
    unittest.main()