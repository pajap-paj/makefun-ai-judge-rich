# Entry for make.fun bounty ai-judge-rich-01 (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt; deterministic, no network.
# Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell AI phone receptionists to US plumbing and HVAC firms that miss after-hours calls.",
        "Day 1: Keep $30 reserve; spend $20 on a Twilio number and Vapi credits; open free Stripe. Via Google Maps, list 40 firms in one metro advertising emergency service with no 24/7 answering; pull each firm's name, services and hours from its site.",
        "Days 2-30: Before pitching, build each firm a live demo line that answers in its name, quotes its services and books a callback. Email the owner a 30-second recording of their demo and its number. Offer: $149 setup to forward missed and after-hours calls to it, plus $49/month, paid by Stripe link before activation. Send 40 demos a day, two follow-ups each.",
        "Math: 800+ demos; just 5 buyers = $745 setup plus first month's fees, minus about $70 of call costs: likely day-30 holding $700-$900. Edge: buyers hear their own business already working before paying, and one saved emergency job repays the fee. Kill any script under 1 sale per 200 demos and switch metros.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
# Bytes, not text mode: text mode would translate line ends and pick a locale encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
