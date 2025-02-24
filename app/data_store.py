from typing import Dict
import uuid

receipt_store: Dict[str, dict] = {}

def save_receipt(receipt_data):
    receipt_id = str(uuid.uuid4())
    receipt_store[receipt_id] = receipt_data
    return receipt_id

def get_receipt(receipt_id):
    return receipt_store.get(receipt_id)
