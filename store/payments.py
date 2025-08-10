import requests
from django.conf import settings

SSLC_INIT_URL = "https://sandbox.sslcommerz.com/gwprocess/v4/api.php"

def initiate_sslcommerz_payment(order_id, amount, customer_name, email, phone, address, success_url=None, fail_url=None, cancel_url=None):
    payload = {
        "store_id": settings.SSLC_STORE_ID,
        "store_passwd": settings.SSLC_STORE_PASSWORD,
        "total_amount": f"{amount:.2f}",
        "currency": "BDT",
        "tran_id": str(order_id),
        "success_url": success_url or settings.SSLC_SUCCESS_URL,
        "fail_url": fail_url or settings.SSLC_FAIL_URL,
        "cancel_url": cancel_url or settings.SSLC_CANCEL_URL,
        "cus_name": customer_name,
        "cus_email": email,
        "cus_add1": address,
        "cus_phone": phone,
        "shipping_method": "NO",
        "product_name": "Air Sneaker Order",
        "product_category": "Shoes",
        "product_profile": "general",
    }
    resp = requests.post(SSLC_INIT_URL, data=payload, timeout=15)
    try:
        return resp.json()
    except Exception:
        return {"status": "ERROR", "raw": resp.text}
