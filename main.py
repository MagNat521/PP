from database import create_user, get_user_by_id

# Создание пользователя
new_user = create_user('test@example.com', 'securepassword')
print(f"Created user: {new_user}")

# Получение пользователя
user = get_user_by_id(1)
print(f"User with id 1: {user}")