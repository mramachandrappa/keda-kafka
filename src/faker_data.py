from faker import Faker

fake = Faker()


def generate_user_data():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }


if __name__ == "__main__":
    print(generate_user_data())