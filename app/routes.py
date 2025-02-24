from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from app.error_validation import validate_receipt
from app.data_store import save_receipt, get_receipt, receipt_store
from app.points_calculation import calculate_points

app = FastAPI()

router = APIRouter()

@router.post("/receipts/process")
async def process_receipt(request: Request):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse(status_code=400, content={"detail": "The receipt is invalid."})
    
    receipt, error = validate_receipt(data)
    if error:
        return JSONResponse(status_code=400, content={"detail": error})
    
    receipt_id = save_receipt(receipt.dict())
    return {"id": receipt_id}

@router.get("/receipts/{id}/points")
async def get_points(id: str):
    receipt = get_receipt(id)
    if not receipt:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    points = calculate_points(receipt)
    return {"points": points}

# Debug API to get list of all receipts
# @router.get("/receipts", summary="Get all receipts")
# async def get_all_receipts():
#     if not receipt_store:
#         return {"message": "No receipts found."}
#     return receipt_store

app.include_router(router)
