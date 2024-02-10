from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

async def not_found(request, exc):
    return templates.TemplateResponse("404.html", context={"request":request})

async def server_error(request, exc):
    return templates.TemplateResponse("500.html", context={"request":request})