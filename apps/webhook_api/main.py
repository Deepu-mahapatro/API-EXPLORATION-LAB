from fastapi import FastAPI
from apps.webhook_api.routes.webhook_routes import router

# Create FastAPI application
app = FastAPI(
    title="Webhook API",
    description="Simple Payment Webhook Receiver",
    version="1.0.0"
)

# Register webhook routes
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Webhook API is running"
    }