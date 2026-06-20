from fastapi import APIRouter

router = APIRouter(
    prefix="/role",
    tags=["Account"]
)

@router.get("/")
def read_roles():
    return [{"name": "Admin"}, {"name": "User"}]
