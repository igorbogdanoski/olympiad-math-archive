import os
import qrcode
import io
import base64

# URL-то на апликацијата (смени за продукција)
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://app.mismath.net/check")

def create_qr_code(test_id: str) -> str:
    """
    Враќа base64 string од QR код кој води до решението.
    """
    target_url = f"{FRONTEND_URL}/{test_id}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(target_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return f"data:image/png;base64,{img_str}"
