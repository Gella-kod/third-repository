class User:
    def __init__(self, user_id: int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = 'Сотрудник'

    def get_user_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_access_level(self) -> str:
        return self._access_level

    def set_name(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"Сотрудник(ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level})"


class Admin(User):
    def __init__(self, user_id: int, name: str):
        super().__init__(user_id, name)
        self._access_level = 'Админ'
        self._users = []

    def add_user(self, user: User) -> None:
        if user not in self._users:
            self._users.append(user)
            print(f"Сотрудник {user.get_name()} успешно добавлен.")
        else:
            print(f"Сотрудник {user.get_name()} уже в базе.")

    def remove_user(self, user_id: int) -> None:
        user_to_remove = None
        for user in self._users:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break

        if user_to_remove:
            self._users.remove(user_to_remove)
            print(f"Сотрудник {user_to_remove.get_name()} успешно удален.")
        else:
            print(f"Сотрудник с идентификатором ID {user_id} не найден.")

    def list_users(self) -> None:
        if not self._users:
            print("Сотрудник в системе не найден.")
        else:
            print("Список сотрудников:")
            for user in self._users:
                print(user)

if __name__ == "__main__":
    user1 = User(1, "Ирина")
    user2 = User(2, "Дмитрий")

    admin = Admin(100, "Admin")

    admin.add_user(user1)
    admin.add_user(user2)

    admin.add_user(user1)

    admin.list_users()

    admin.remove_user(1)

    admin.list_users()