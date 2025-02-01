from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from api.v1.authentication import router as auth_router
from api.v1.users import router as users_router


http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(dependencies=[Depends(http_bearer)])

router_list = [auth_router, users_router]

for router_ in router_list:
    router.include_router(router_)
