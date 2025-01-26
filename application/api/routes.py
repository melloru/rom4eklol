from fastapi import APIRouter

from api.v1.users import router as users_router


routers = APIRouter()

router_list = [users_router]

for router in router_list:
    routers.include_router(router)
