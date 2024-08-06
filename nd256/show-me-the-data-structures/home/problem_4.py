from typing import List

class Group:
    def __init__(self, _name: str) -> None:
        self.name: str = _name
        self.groups: List[Group] = []
        self.users: List[str] = []

    def add_group(self, group: 'Group') -> None:
        self.groups.append(group)

    def add_user(self, user: str) -> None:
        self.users.append(user)

    def get_groups(self) -> List['Group']:
        return self.groups

    def get_users(self) -> List[str]:
        return self.users

    def get_name(self) -> str:
        return self.name


def is_user_in_group(user: str, group: Group) -> bool:
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is None:
        return False

    # Use a stack to implement an iterative depth-first search
    stack = [group]

    while stack:
        current_group = stack.pop()
        # Check if the user is directly in this group
        if user in current_group.get_users():
            return True

        # Add all subgroups to the stack for further exploration
        stack.extend(current_group.get_groups())

    return False

if __name__ == "__main__":
    # Testing the implementation

    # Creating groups and users
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User is in a nested subgroup
    print("Test Case 1")
    print(is_user_in_group("sub_child_user", parent))  # Expected output: True

    # Test Case 2: User is directly in the parent group
    print("Test Case 2")
    parent.add_user("parent_user")
    print(is_user_in_group("parent_user", parent))  # Expected output: True

    # Test Case 3: User is not in any group
    print("Test Case 3")
    print(is_user_in_group("non_existent_user", parent))  # Expected output: False

    # Test Case 4: Check with a null user
    print("Test Case 4")
    print(is_user_in_group(None, parent))  # Expected output: False

    # Test Case 5: Check with an empty string as user
    print("Test Case 5")
    print(is_user_in_group("", parent))  # Expected output: False

    # Test Case 6: Very large group structure with deeply nested subgroups
    print("Test Case 6")
    large_group = Group("large_group")
    deep_group = large_group
    # Create a deep hierarchy
    for i in range(1000):
        new_group = Group(f"group_{i}")
        deep_group.add_group(new_group)
        deep_group = new_group
    # Add a user at the last level
    deep_group.add_user("deep_user")
    print(is_user_in_group("deep_user", large_group))  # Expected output: True
    