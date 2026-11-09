from fastapi import APIRouter, Request
from apps.webhook_api.services.event_service import process_event

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/payment")
async def receive_payment_webhook(request: Request):

    # Receive JSON payload from the sender
    payload = await request.json()

    # Pass the event to the event handler
    result = process_event(payload)

    # Send acknowledgement to the sender
    return {
        "status": "success",
        "message": "Webhook received successfully",
        "result": result
    }