import fastapi
from starlette.middleware import cors

from api.ai.search import search


app = fastapi.FastAPI()

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search.router)
