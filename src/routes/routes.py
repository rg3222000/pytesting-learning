from fastapi import APIRouter

router: APIRouter = APIRouter(
    prefix='/testing-service'
)


@router.get("/health-check")
def HealthCheck():
    return {"message": "service working fine"}
