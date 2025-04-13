from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    first_name: str
    last_name: str
    email: str
    age: str
    salary: str
    department: str
    current_address: str
    permanent_address: str
