from .connection import get_connection
from mysql.connector import Error

# ====================== Users CRUD ======================
def create_user(email: str, password: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )
        user_id = cursor.lastrowid
        conn.commit()
        
        # Получаем созданного пользователя
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def update_user(user_id: int, email: str = None, password: str = None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        updates = []
        params = []
        
        if email:
            updates.append("email = %s")
            params.append(email)
        if password:
            updates.append("password = %s")
            params.append(password)
            
        if not updates:
            return None
            
        query = "UPDATE users SET " + ", ".join(updates) + " WHERE id = %s"
        params.append(user_id)
        
        cursor.execute(query, params)
        conn.commit()
        
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        return cursor.fetchone()
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

# ====================== Projects CRUD ======================
def create_project(name: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO projects (name) VALUES (%s)",
            (name,)
        )
        project_id = cursor.lastrowid
        conn.commit()
        
        cursor.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
        return cursor.fetchone()
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_project_by_id(project_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM projects WHERE id = %s", (project_id,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

# ====================== Tasks CRUD ======================
def create_task(title: str, description: str, column_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """INSERT INTO tasks (title, description, column_id) 
            VALUES (%s, %s, %s)""",
            (title, description, column_id)
        )
        task_id = cursor.lastrowid
        conn.commit()
        
        cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        return cursor.fetchone()
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_tasks_by_column(column_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tasks WHERE column_id = %s ORDER BY created_at", (column_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

# ====================== User Projects ======================
def add_user_to_project(user_id: int, project_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO user_projects (user_id, project_id) 
            VALUES (%s, %s)""",
            (user_id, project_id)
        )
        conn.commit()
        return True
    except Error as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def get_user_projects(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """SELECT p.* FROM projects p
            JOIN user_projects up ON p.id = up.project_id
            WHERE up.user_id = %s""",
            (user_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
