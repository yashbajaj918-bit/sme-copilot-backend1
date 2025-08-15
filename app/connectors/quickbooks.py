# Placeholder for QuickBooks Online connector
def fetch_invoices(limit: int = 10):
    return [{"id": i, "amount": 100 + i} for i in range(limit)]
