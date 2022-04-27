import addressbook_pb2


def encode(person):
    print(person.SerializeToString())


def decode(binary: str):
    person_temp = addressbook_pb2.Person()
    person_temp.ParseFromString(binary)
    print(person_temp.name)


if __name__ == '__main__':
    print(dir(addressbook_pb2))
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = "Frank"
    person.email = "test.163.com"
    encode(person)
    decode(b'\n\x05Frank\x10\xd2\t\x1a\x0ctest.163.com')