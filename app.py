# # app.py
# import time
# import random
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse

# app = FastAPI()

# INFER_COUNT = 0

# def run_ai_inference():
#     global INFER_COUNT
#     INFER_COUNT += 1

#     t0 = time.perf_counter()
#     score = round(random.random(), 4)
#     loss = round(0.2 + random.random() * 0.8, 4)
#     latency_ms = round((time.perf_counter() - t0) * 1000, 2)

#     return {
#         "ts": time.time(),
#         "score": score,
#         "loss": loss,
#         "latency_ms": latency_ms,
#         "count": INFER_COUNT
#     }

# @app.get("/api/metrics")
# def metrics():
#     return JSONResponse(
#         run_ai_inference(),
#         headers={"Cache-Control": "no-store"}
#     )


# app.py
import time
import datetime as dt
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
INFER_COUNT = 0

# 초단기실황조회(getUltraSrtNcst)
BASE_URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
SERVICE_KEY = "7720f7cf9bf6399df12ebb6bdfafd56eed2ad3b1b2b63d92988a146fc702ec71"

# 예: 울산(대략) 격자좌표는 직접 정해야 함 (nx, ny는 위경도가 아니라 '격자'임)  :contentReference[oaicite:2]{index=2}
NX = 101
NY = 84

# 간단 캐시(1초 폴링이면 호출 제한 걸릴 수 있어서 권장)
CACHE_TTL_SEC = 30
_last = {"ts": 0, "data": None}

def _normalize(x, lo, hi):
    if hi == lo:
        return 0.0
    x = max(lo, min(hi, x))
    return (x - lo) / (hi - lo)

def _pick_base_datetime(now=None):
    # 초단기실황은 base_time이 "정시단위"라고 명시되어 있음 :contentReference[oaicite:3]{index=3}
    # 실무적으로는 최신 정시로 맞추되, 만약 데이터가 아직 안 올라왔으면 직전 정시로 fallback
    if now is None:
        now = dt.datetime.now()
    base = now.replace(minute=0, second=0, microsecond=0)
    return base

def fetch_ultra_ncst(nx, ny):
    base = _pick_base_datetime()
    candidates = [base, base - dt.timedelta(hours=1)]  # 1차 시도, 실패시 1시간 전 재시도

    last_err = None
    for b in candidates:
        base_date = b.strftime("%Y%m%d")
        base_time = b.strftime("%H%M")  # 정시: HH00

        params = {
            "serviceKey": SERVICE_KEY,
            "pageNo": 1,
            "numOfRows": 100,
            "dataType": "JSON",
            "base_date": base_date,
            "base_time": base_time,
            "nx": nx,
            "ny": ny,
        }

        r = requests.get(BASE_URL, params=params, timeout=3)
        if r.status_code != 200:
            last_err = f"HTTP {r.status_code}"
            continue

        j = r.json()
        try:
            items = j["response"]["body"]["items"]["item"]
        except Exception:
            last_err = f"bad response shape: {j.get('response', {}).get('header', {})}"
            continue

        # category -> obsrValue  :contentReference[oaicite:4]{index=4}
        m = {it["category"]: it["obsrValue"] for it in items}
        # 필요한 값만 뽑기
        t1h = float(m.get("T1H"))  # 기온(℃)
        reh = float(m.get("REH"))  # 습도(%)
        rn1 = float(m.get("RN1"))  # 강수량(mm)
        return {"base_date": base_date, "base_time": base_time, "T1H": t1h, "REH": reh, "RN1": rn1}

    raise RuntimeError(last_err or "failed to fetch")

@app.get("/api/metrics")
def metrics():
    global INFER_COUNT
    INFER_COUNT += 1

    # 캐시 사용 (폴링 1초여도, 실제 공공데이터 호출은 30초마다 한 번)
    now = time.time()
    if _last["data"] is not None and (now - _last["ts"]) < CACHE_TTL_SEC:
        d = _last["data"].copy()
        d["count"] = INFER_COUNT
        return JSONResponse(d, headers={"Cache-Control": "no-store"})

    t0 = time.perf_counter()
    try:
        w = fetch_ultra_ncst(NX, NY)
        latency_ms = round((time.perf_counter() - t0) * 1000, 2)

        # score/loss는 차트용으로 0~1 정규화(예시)
        score = round(_normalize(w["T1H"], -10, 40), 4)  # -10~40℃를 0~1로
        loss  = round(_normalize(w["REH"], 0, 100), 4)   # 0~100%를 0~1로

        payload = {
            "ts": time.time(),
            "score": score,
            "loss": loss,
            "latency_ms": latency_ms,
            "count": INFER_COUNT,
            # 원본값도 같이 내려주면 UI에서 표시하기 좋음
            "temp_c": w["T1H"],
            "humidity": w["REH"],
            "rain_mm": w["RN1"],
            "base_date": w["base_date"],
            "base_time": w["base_time"],
        }
        _last["ts"] = now
        _last["data"] = payload
        return JSONResponse(payload, headers={"Cache-Control": "no-store"})

    except Exception as e:
        latency_ms = round((time.perf_counter() - t0) * 1000, 2)
        payload = {
            "ts": time.time(),
            "score": None,
            "loss": None,
            "latency_ms": latency_ms,
            "count": INFER_COUNT,
            "error": str(e),
        }
        return JSONResponse(payload, headers={"Cache-Control": "no-store"})
