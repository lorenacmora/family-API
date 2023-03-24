from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "id":self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]},
            {
            "id":self._generateId(),
            "first_name": "Jane", 
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]},
            {
            "id":self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]}
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self,id,first_name,age,lucky_numbers):
        self._members.append({
            "id": id,
            "first_name": first_name,
            "age": age,
            "lucky_numbers":lucky_numbers
            })

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"done": True}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members