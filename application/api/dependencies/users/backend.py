from fastapi_users.authentication import AuthenticationBackend

from api.dependencies.users.strategy_db import get_database_strategy
from .transport import bearer_transport

authentication_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
