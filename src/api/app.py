from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import numpy as np
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.core.engine import analyze_finances
from src.api.schemas import FinanceResponse
from src.core.reader.budget import load_budget
from src.api.schemas import FinanceResponse, AvailablePeriodsResponse


app = FastAPI(title="Finance AI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/finance", response_model=FinanceResponse)
def get_finance(month: int | None = None, year: int | None = None):
    try:
        result = analyze_finances(month=month, year=year)

        json_result = jsonable_encoder(
            result,
            custom_encoder={
                np.generic: lambda value: value.item(),
                np.ndarray: lambda value: value.tolist(),
            },
        )

        return JSONResponse(content=json_result)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

@app.get(
    "/api/finance/available-periods",
    response_model=AvailablePeriodsResponse,
)
def get_available_periods():
    budget = load_budget()

    periods = (
        budget[["Month", "Year"]]
        .drop_duplicates()
        .sort_values(["Year", "Month"])
    )

    return {
        "periods": [
            {
                "month": int(row["Month"]),
                "year": int(row["Year"]),
            }
            for _, row in periods.iterrows()
        ]
    }

