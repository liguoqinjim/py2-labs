from faker import Faker

fake = Faker()
fake = Faker('zh_CN')

print(fake.name())
print(fake.phone_number())
