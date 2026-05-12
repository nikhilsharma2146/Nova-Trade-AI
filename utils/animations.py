import requests

def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Cool public Lottie URLs for different pages
ANIMATIONS = {
    "dashboard": "https://assets3.lottiefiles.com/packages/lf20_qp1q7mct.json", # Chart/analytics
    "prediction": "https://assets1.lottiefiles.com/packages/lf20_mbiye47k.json", # AI Brain
    "news": "https://assets8.lottiefiles.com/packages/lf20_9wjm14ni.json", # Global connection
    "portfolio": "https://assets4.lottiefiles.com/packages/lf20_q5pk6p1k.json" # Wallet/Coins
}
