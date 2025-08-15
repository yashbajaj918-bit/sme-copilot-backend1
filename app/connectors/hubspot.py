# Placeholder for HubSpot connector
def fetch_deals(limit: int = 10):
    return [{"id": i, "stage": "qualified", "amount": 1000 + 50*i} for i in range(limit)]
