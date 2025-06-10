from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.scraper import get_stock_data
from app.portfolio import optimize_portfolio, high_dividend_portfolio
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/optimize", response_class=HTMLResponse)
def optimize(request: Request, tickers: str = Form(...)):
    tickers_list = tickers.upper().split(',')
    df = get_stock_data(tickers_list)
    optimized, fig = optimize_portfolio(df)
    dividends, div_fig = high_dividend_portfolio(df)
    return templates.TemplateResponse("result.html", {
        "request": request,
        "optimized": optimized,
        "dividends": dividends,
    })

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
  
