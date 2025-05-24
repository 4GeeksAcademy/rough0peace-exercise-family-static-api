"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # You have to implement this method
        # Append the member to the list of _members

        # checking if member id dict already has id key
        # if it doesn't, then gives new member random id int 0-10
        if "id" not in member:
            member["id"] = randint(0, 10)
        self._members.append(member)

    def delete_member(self, id):
        # You have to implement this method
        # Loop the list and delete the member with the given id
        updated_members = []
        for member in self._members:
            if member["id"] != id:
                updated_members.append(member)
        self._members = updated_members

        # self._members = list(filter(lambda member:member["id"] != id, self._members))

    def get_member(self, id):
        # You have to implement this method
        # Loop all the members and return the one with the given id
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
