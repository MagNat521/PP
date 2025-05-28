from database import create_user, create_project, add_user_to_project

if __name__ == "__main__":
    # Пример создания пользователя
    new_user = create_user("test@example.com", "securepassword")
    print(f"Created user: {new_user}")
    
    # Пример создания проекта
    new_project = create_project("My First Project")
    print(f"Created project: {new_project}")
    
    # Добавление пользователя в проект
    success = add_user_to_project(new_user['id'], new_project['id'])
    print(f"User added to project: {success}")
