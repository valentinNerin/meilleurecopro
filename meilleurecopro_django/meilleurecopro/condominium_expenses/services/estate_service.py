
from meilleurecopro.condominium_expenses.enums.location_type_enum import LocationTypeEnum
from meilleurecopro.condominium_expenses.dto.condominium_expenses import CondominiumExpenses
from meilleurecopro.models import Estate
from meilleurecopro.condominium_expenses.repository.estate_repository import EstateRepository

import numpy as np
import requests

class EstateService:

    def get_condominium_expenses(self, location: str, location_type: LocationTypeEnum) -> list[float]:
        condominium_expenses: list[CondominiumExpenses] = []
        estates = self.get_estate_by_location_and_location_type(location, location_type)

        if len(estates) != 0:
            for estate in estates:
                condominium_expenses.append(estate.condominium_expenses)

            return self._calculate_condominium_expenses(condominium_expenses)
        else: 
            return None
        
    def get_estate_by_location_and_location_type(self, location: str, location_type: LocationTypeEnum) -> list[Estate]:
        estate_repository = EstateRepository()

        match location_type:
            case "city":
                estates = estate_repository.get_estates_by_city(location)
                return estates
            case "department":
                return estate_repository.get_estates_by_department_code(location)
            case "zip_code":
                return estate_repository.get_estates_by_zip_code(location)
            case _:
                return 
    
    def get_estate_by_url(self, api_url: str) -> Estate:
        try:
            response = requests.get(api_url, timeout=10)  
            response.raise_for_status()  
            data = response.json()

            return Estate(city=data['city'], zip_code=data['postalCode'], dept_code=data['departmentCode'], condominium_expenses=data['annualCondominiumFees'], ad_url=api_url)
        except requests.RequestException as e:
            data = None
            print("API call failed:", e)

        

    def add_estate(self, estate: Estate) -> None:
        EstateRepository().add_estate(estate)

    def _calculate_condominium_expenses(self, condominium_expenses: list[float]) -> CondominiumExpenses:
         mean: float = self._calculate_mean(condominium_expenses)
         quantile_10: float = self._calculate_quantile_10(condominium_expenses) 
         quantile_90: float = self._calculate_quantile_90(condominium_expenses)

         return CondominiumExpenses(mean, quantile_10, quantile_90)
    
    def _calculate_mean(self, condominium_expenses: list[float]) -> float:
        return np.mean(condominium_expenses)

    def _calculate_quantile_10(self, condominium_expenses: list[float]) -> float:
        return np.quantile(condominium_expenses, 0.1)

    def _calculate_quantile_90(self, condominium_expenses: list[float]) -> float:
        return np.quantile(condominium_expenses, 0.9)


