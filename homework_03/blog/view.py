from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/ping/",
    response_model=dict,
)
def pong() -> dict:
    return {
        "message": "pong"
    }
