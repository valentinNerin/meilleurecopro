from meilleurecopro.models import Estate
from meilleurecopro.condominium_expenses.enums.location_type_enum import LocationTypeEnum

class EstateRepository:

    def get_estates_by_city(self, location: str) -> list[Estate]:
        return Estate.objects.filter(city=location)

    def get_estates_by_department_code(self, location: str) -> list[Estate]:
        return Estate.objects.filter(dept_code=location)

    def get_estates_by_zip_code(self, location: str) -> list[Estate]:
        return Estate.objects.filter(zip_code=location)
