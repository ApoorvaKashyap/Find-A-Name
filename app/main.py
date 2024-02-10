from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from app.errors import not_found, server_error
from app.models import FinalResponse
from app.operations import search
import httpx


exceptions = {
    404: not_found,
    500: server_error
}

app = FastAPI(exception_handlers=exceptions)
templates = Jinja2Templates(directory="templates")


limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
timeout = httpx.Timeout(timeout=5.0, read=15.0)
client = httpx.AsyncClient(limits=limits, timeout=timeout)

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down...")
    await client.aclose()


@app.get("/", response_class=HTMLResponse)
async def home(request:Request, projectName: Optional[str] = None):
    if not projectName:
        return templates.TemplateResponse("index.html",context={"request":request})
    response = await search(projectName)
    print(response.model_dump_json)
    return templates.TemplateResponse("index.html", context = {"request":request, "response":response})


if __name__ == "__main__":
    uvicorn.run(app)