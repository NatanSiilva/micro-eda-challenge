import uvicorn

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.application.composer import StartupComposer

from src.adapters.web.api import balances_router


app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="Challenge microservice EDA",
)


@app.on_event("startup")
async def startup_event():
    await StartupComposer.compose()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


root_router = APIRouter()


@root_router.get("/")
def root():
    return RedirectResponse(url="/docs")


app.include_router(root_router)
app.include_router(balances_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3003)
