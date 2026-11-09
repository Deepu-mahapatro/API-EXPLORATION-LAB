def process_event(payload):

    # Extract event information
    event_type = payload.get("event")

    # Identify the incoming event
    if event_type == "payment.success":

        payment = payload.get("data", {})

        payment_id = payment.get("payment_id")
        amount = payment.get("amount")
        currency = payment.get("currency")

        print("\nPayment Successful!")
        print("Payment ID:", payment_id)
        print("Amount:", amount)
        print("Currency:", currency)

        return {
            "event": event_type,
            "payment_id": payment_id,
            "message": "Payment processed successfully"
        }

    elif event_type == "payment.failed":

        print("\nPayment Failed!")

        return {
            "event": event_type,
            "message": "Payment failure event received"
        }

    else:

        print("\nUnknown Event Received!")

        return {
            "event": event_type,
            "message": "Event type not recognized"
        }