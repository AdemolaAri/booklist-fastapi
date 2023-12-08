from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.v1.endpoints import book
from prometheus_client import Counter
from fastapi_versioning import VersionedFastAPI

app = FastAPI(title='Booklist API')

# Include the router from the book endpoint
app.include_router(book.router)

app = VersionedFastAPI(app,
                       version_format='{major}',
                       prefix_format='/api/v{major}')

# Example usage of a custom Counter
APP_VISITS = Counter(
    "app_visits",
    "Number of times the docs were visited",
    ["framework", "type"],
)

# Redirect the root route to the /docs


@app.get('/')
def homepage():
    return RedirectResponse(url="/api/v1/docs")


@app.get('/v{version}')
@app.get('/api/v{version}')
def api_doc(version: str):
    # Add to custom counter
    APP_VISITS.labels(framework="FastAPI", type="example").inc()
    return RedirectResponse(url=f"/api/v{version}/docs")
