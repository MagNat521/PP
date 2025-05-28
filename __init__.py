from .connection import get_connection, release_connection, close_all_connections
from .crud import (
    create_user, get_user_by_id, update_user, delete_user,
    create_project, get_project_by_id, update_project, delete_project,
    create_task, get_task_by_id, update_task, delete_task
)

# Можно сделать более удобный экспорт
__all__ = [
    'get_connection', 'release_connection', 'close_all_connections',
    'create_user', 'get_user_by_id', 'update_user', 'delete_user',
    'create_project', 'get_project_by_id', 'update_project', 'delete_project',
    'create_task', 'get_task_by_id', 'update_task', 'delete_task'
]