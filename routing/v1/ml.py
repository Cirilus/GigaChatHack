from fastapi import APIRouter, HTTPException, status
from schemas.ml import MlResponse, MlRequest

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/",
    response_model=MlResponse,
)
async def post(req: MlRequest):
    if req.description == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is not description")

    return MlResponse(
        economy=
        """- Много расти\n- Сильно расти\n- Широко расти""",
        business_model=
        """- продавать за дорого\n- покупать за дешево""",
        competitors=
        """- ООО Рога и копыта\n- ООО Тест Сибирь""",
        development_plan=
        """- много покупать\n- много продовать""",
        team=
        """- дизайнер\n- бог""",
        value_proposition=
        """- Хз что тут написать :)""",
    )


@router.get(
    "/",
    response_model=MlResponse,
)
async def get(desc: str):
    if desc == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is not description")

    return MlResponse(
        economy=
        """- Много расти\n- Сильно расти\n- Широко расти""",
        business_model=
        """- продавать за дорого\n- покупать за дешево""",
        competitors=
        """- ООО Рога и копыта\n- ООО Тест Сибирь""",
        development_plan=
        """- много покупать\n- много продовать""",
        team=
        """- дизайнер\n- бог""",
        value_proposition=
        """- Хз что тут написать :)""",
    )
