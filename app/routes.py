from fastapi import FastAPI, Request, HTTPException, APIRouter, Body
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.error_validation import validate_receipt
from app.data_store import save_receipt, get_receipt, receipt_store
from app.points_calculation import calculate_points
from app.models import Receipt

app = FastAPI()
router = APIRouter()

RECEIPT_EXAMPLE = {
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "total": "6.49",
    "items": [
        {
            "shortDescription": "Mountain Dew 12PK",
            "price": "6.49"
        }
    ]
}

@router.post("/receipts/process")
async def process_receipt(receipt: dict = Body(..., example=RECEIPT_EXAMPLE)): 
    validated_receipt, error = validate_receipt(receipt)
    if error:
        return JSONResponse(status_code=400, content={"detail": "The receipt is invalid."})
    
    receipt_id = save_receipt(validated_receipt)
    return {"id": receipt_id}

@router.get("/receipts/{id}/points")
async def get_points(id: str):
    receipt = get_receipt(id)
    if not receipt:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    points = calculate_points(receipt)
    return {"points": points}

# Debug API to get list of all receipts
@router.get("/receipts", summary="Get all receipts")
async def get_all_receipts():
    if not receipt_store:
        return {"message": "No receipts found."}
    return receipt_store

app.include_router(router)
