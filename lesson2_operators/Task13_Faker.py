from faker import Faker

fake = Faker(['ru_RU'])
print("1.", fake.name(), " | " , fake.address(), end='\n')
print("2.", fake.name(), " | " , fake.address(), end='\n')
print("3.", fake.name(), " | " , fake.address(), end='\n')
