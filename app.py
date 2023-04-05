from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Params(BaseModel):
    github_access_token: str
    vercel_access_token: str
    source_url: str
    target_name: str
    github_repo_url: str
    vercel_project_name: str
    vercel_team_id: str


@app.post("/submit")
async def submit_params(params: Params):
    # Process the submitted parameters (e.g., clone the GitHub repository, deploy to Vercel, etc.)
    # For now, just return a success message
    return {"message": "123 Parameters received successfully", "params": params}


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
