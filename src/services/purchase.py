from dataclasses import dataclass
from __utils.validators import ValidatorRules


@dataclass(kw_only=True)
class Purchase():
    cpf: str
    private: bool
    incomplete: bool
    last_purchase: str
    average_purchase_price: float
    last_purchase_price: float
    most_frequent_store: str
    last_purchase_store: str

    def validate(self):
        print(f"Validating {self.cpf}")
        return all(
            [
                ValidatorRules.values(self.cpf, "cpf").required().string().is_cpf_valid(),
                ValidatorRules.values(self.private, "private").required().boolean(),
                ValidatorRules.values(self.incomplete, "incomplete").required().boolean(),
                ValidatorRules.values(self.last_purchase, "last_purchase").required().string(),
                ValidatorRules.values(self.average_purchase_price, "average_purchase_price").required().float(),
                ValidatorRules.values(self.last_purchase_price, "last_purchase_price").required().float(),
                ValidatorRules.values(self.most_frequent_store, "most_frequent_store").required().string().is_cnpj_valid(),
                ValidatorRules.values(self.last_purchase_store, "last_purchase_store").required().string().is_cnpj_valid()
            ]
        )
        
    