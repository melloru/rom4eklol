from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
async def test_user():
    return {"message": "hello world"}
