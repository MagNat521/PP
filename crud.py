from .connection import get_connection, release_connection

def create_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s) RETURNING *",
            (email, password)  # Здесь была пропущена закрывающая скобка
        )
        user = cursor.fetchone()
        conn.commit()
        return user
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить всех пользователей
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить пользователя по ID
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить пользователя по email
def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def update_user(user_id, email=None, password=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if email and password:
            cursor.execute(
                "UPDATE users SET email = %s, password = %s WHERE id = %s RETURNING *",
                (email, password, user_id))
        elif email:
            cursor.execute(
                "UPDATE users SET email = %s WHERE id = %s RETURNING *",
                (email, user_id))
        elif password:
            cursor.execute(
                "UPDATE users SET password = %s WHERE id = %s RETURNING *",
                (password, user_id))
        
        updated_user = cursor.fetchone()
        conn.commit()
        return updated_user
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s RETURNING *", (user_id,))
        deleted_user = cursor.fetchone()
        conn.commit()
        return deleted_user
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def create_project(name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO projects (name) VALUES (%s) RETURNING *",
            (name,))
        project = cursor.fetchone()
        conn.commit()
        return project
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить все проекты
def get_all_projects():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM projects")
        projects = cursor.fetchall()
        return projects
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить проект по ID
def get_project_by_id(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
        project = cursor.fetchone()
        return project
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def update_project(project_id, name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE projects SET name = %s WHERE id = %s RETURNING *",
            (name, project_id))
        updated_project = cursor.fetchone()
        conn.commit()
        return updated_project
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def delete_project(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM projects WHERE id = %s RETURNING *", (project_id,))
        deleted_project = cursor.fetchone()
        conn.commit()
        return deleted_project
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def create_task(title, description, column_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO tasks (title, description, column_id) 
            VALUES (%s, %s, %s) RETURNING *""",
            (title, description, column_id))
        task = cursor.fetchone()
        conn.commit()
        return task
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить все задачи
def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        return tasks
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить задачу по ID
def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        return task
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

# Получить задачи по column_id
def get_tasks_by_column(column_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM tasks WHERE column_id = %s", (column_id,))
        tasks = cursor.fetchall()
        return tasks
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def update_task(task_id, title=None, description=None, column_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        updates = []
        params = []
        
        if title is not None:
            updates.append("title = %s")
            params.append(title)
        if description is not None:
            updates.append("description = %s")
            params.append(description)
        if column_id is not None:
            updates.append("column_id = %s")
            params.append(column_id)
            
        if not updates:
            return None
            
        query = "UPDATE tasks SET " + ", ".join(updates) + " WHERE id = %s RETURNING *"
        params.append(task_id)
        
        cursor.execute(query, params)
        updated_task = cursor.fetchone()
        conn.commit()
        return updated_task
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tasks WHERE id = %s RETURNING *", (task_id,))
        deleted_task = cursor.fetchone()
        conn.commit()
        return deleted_task
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)
    
def add_user_to_project(user_id, project_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO user_projects (user_id, project_id) 
            VALUES (%s, %s) RETURNING *""",
            (user_id, project_id))
        result = cursor.fetchone()
        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        release_connection(conn)

def get_user_projects(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """SELECT p.* FROM projects p
            JOIN user_projects up ON p.id = up.project_id
            WHERE up.user_id = %s""",
            (user_id,))
        projects = cursor.fetchall()
        return projects
    except Exception as e:
        raise e
    finally:
        cursor.close()
        release_connection(conn)