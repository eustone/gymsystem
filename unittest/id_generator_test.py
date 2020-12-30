from uuid import uuid4


def generate_id():
    return uuid4().hex[:8]

print(generate_id())