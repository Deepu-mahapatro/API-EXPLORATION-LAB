
import asyncio
from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI(
    title="SSE API",
    description="Server-Sent Events Learning Implementation",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "SSE API is running successfully"
    }


@app.get("/api/v1/sse/stream")
async def sse_stream(request: Request):

    async def event_generator():
        counter = 1

        try:
            while True:

                # Check client disconnection
                if await request.is_disconnected():
                    print("Client disconnected")
                    break

                current_time = datetime.now(timezone.utc).isoformat()

                # Send SSE event
                yield (
                    f"id: {counter}\n"
                    f"event: counter\n"
                    f"data: Counter: {counter}\n"
                    f"data: Time: {current_time}\n\n"
                )

                counter += 1

                # Wait before sending next event
                await asyncio.sleep(2)

        except asyncio.CancelledError:
            print("SSE connection cancelled")
            raise

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )
