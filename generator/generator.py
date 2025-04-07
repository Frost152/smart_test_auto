from data.data import UserProfile
from faker import Faker


def user_generate():
    fake = Faker("ru_RU")
    yield UserProfile(name=fake.name(), email=fake.email(), current_address=fake.address(),
                      permanent_address=fake.address())
