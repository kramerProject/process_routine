
import re

class Parser():

    def parse_line(self, line):
        purchase = {
            "cpf": self._parse_document(line[0]).strip(),
            "private": self._parse_to_boolean(line[1]),
            "incomplete": self._parse_to_boolean(line[2]),
            "lastPurchase": line[3].strip(),
            "averagePurchasePrice": self._parse_to_float(line[4]),
            "lastPurchasePrice": self._parse_to_float(line[5]),
            "mostFrequentStore": self._parse_document(line[6]).strip(),
            "lastPurchaseStore": self._parse_document(line[7]).strip()
        }
        return purchase

    def _parse_to_boolean(self, value):
        return value == '1'

    def _parse_document(self, document):
        parsed_doc = re.sub(r'[^\w\s]','',document)
        return parsed_doc

    def _parse_to_float(self, str_value):
        if str_value == 'NULL':
            return 0
        str_value = str_value.replace(",", ".")
        return float(str_value)