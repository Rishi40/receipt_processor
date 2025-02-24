from app.models import Receipt
from pydantic import ValidationError

def validate_receipt(data: dict):
    try:
        receipt = Receipt.model_validate(data)
        return receipt, None
    except ValidationError:
        return None, "The receipt is invalid."
