from fastapi import APIRouter, Depends
from ..utils.security import get_current_user
from ..connectors import google_sheets, quickbooks, hubspot

router = APIRouter()

@router.get("/sheets")
def get_sheet(user=Depends(get_current_user)):
    return google_sheets.fetch_sheet("demo", "A1:B10")

@router.get("/quickbooks/invoices")
def invoices(user=Depends(get_current_user)):
    return quickbooks.fetch_invoices()

@router.get("/hubspot/deals")
def deals(user=Depends(get_current_user)):
    return hubspot.fetch_deals()
