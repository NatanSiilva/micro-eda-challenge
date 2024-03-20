import uvicorn

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="Challenge microservice EDA",
)

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
    return JSONResponse("service balance is ok!")


app.include_router(root_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
