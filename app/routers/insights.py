import io
import pandas as pd
from fastapi import APIRouter, File, UploadFile, Depends
from ..models.schemas import InsightSummary
from ..utils.security import get_current_user
from ..services.forecast import moving_average_forecast

router = APIRouter()

@router.post("/upload", response_model=InsightSummary)
async def upload(file: UploadFile = File(...), user=Depends(get_current_user)):
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    cols = df.columns.tolist()
    num_rows = len(df)
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    forecast_col = numeric_cols[0] if numeric_cols else None
    forecast_preview = None
    if forecast_col:
        forecast_preview = moving_average_forecast(df[forecast_col])
    summary = f"Rows: {num_rows}. Columns: {cols}. "
    if forecast_col:
        summary += f"Forecast (moving average) for '{forecast_col}': {forecast_preview[:3]} ..."
    return InsightSummary(
        summary=summary,
        columns=cols,
        num_rows=num_rows,
        forecast_column=forecast_col,
        forecast_preview=forecast_preview[:3] if forecast_preview else None
    )
