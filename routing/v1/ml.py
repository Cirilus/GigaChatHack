from fastapi import APIRouter, HTTPException, status
from schemas.ml import MlResponse, MlRequest
from langchain.chat_models.gigachat import GigaChat

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/",
)
async def post(req: MlRequest):
    if req.description == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There is not description")

    # chat = GigaChat(credentials="", verify_ssl_certs=False)

    return {
        "Экономика": "- Много расти\n- Сильно расти\n- Широко расти",
        "Бизнес модель": "- продавать за дорого\n- покупать за дешево",
        "Конкуренты": "- ООО Рога и копыта\n- ООО Тест Сибирь",
        "План развития": "- много покупать\n- много продовать",
        "команда": "- дизайнер\n- бог",
        "ценностное предложение": "- Хз что тут написать :)",
    }
