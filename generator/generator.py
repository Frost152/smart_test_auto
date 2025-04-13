from data.data import UserProfile
from faker import Faker


def user_generate():
    fake = Faker("ru_RU")
    yield UserProfile(name=fake.name(), first_name=fake.first_name(), last_name=fake.last_name(),
                      email=fake.email(), age=str(fake.random_int(18, 60)),
                      salary=str(fake.random_int(17000, 150000)),
                      department=fake.job(), current_address=fake.address(),
                      permanent_address=fake.address())
