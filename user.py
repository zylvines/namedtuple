# from os import name
# from typing import NamedTuple
#
# class User(NamedTuple):
#     name: str
#     age: int
#     email: str
#     id: str
#     phone_number: str
#
#     def get_info(self):
#         return(f"Name: {self.name}, age: {self.age}, email: {self.email}, id: {self.email}, phone_number: {self.phone_number}")
#
#     @classmethod
#     def create_from_email(cls, email: str):
#         name = email.split('@')[0]
#         return cls(name=name, email=email)
#
#
# user = User(name="john_doe", email="john@example.com", age=20, id=28973, phone_number="+998931024020")
#
# new_user = User.create_from_email("jane_doe@gmail.com")\
