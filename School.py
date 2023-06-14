class School:
    def __init__(self, id: int, title: str, name: str, address: str, real_address: str, department: str, country: str,
                 tel: str, email: str):
        self.id = id
        self.title = title
        self.name = name
        self.address = address
        self.real_address = real_address
        self.department = department
        self.country = country
        self.tel = tel
        self.email = email

    def get_id(self) -> int:
        return self.id

    def get_title(self) -> str:
        return self.title

    def set_title(self, value: str):
        self.title = value

    def get_name(self) -> str:
        return self.name

    def set_name(self, value: str):
        self.name = value

    def get_address(self) -> str:
        return self.address

    def set_address(self, value: str):
        self.address = value

    def get_real_address(self) -> str:
        return self.real_address

    def set_real_address(self, value: str):
        self.real_address = value

    def get_department(self) -> str:
        return self.department

    def set_department(self, value: str):
        self.department = value

    def get_country(self) -> str:
        return self.country

    def set_country(self, value: str):
        self.country = value

    def get_tel(self) -> str:
        return self.tel

    def set_tel(self, value: str):
        self.tel = value

    def get_email(self) -> str:
        return self.email

    def set_email(self, value: str):
        self.email = value
