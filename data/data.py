from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    email: str
    current_address: str
    permanent_address: str
