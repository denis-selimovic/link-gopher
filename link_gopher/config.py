import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    HTTP_RESPONSE_TIMEOUT = os.environ.get("HTTP_RESPONSE_TIMEOUT") or 30
    MAX_SCRIPT_RUN_TIME = os.environ.get("MAX_SCRIPT_RUN_TIME") or 40
    HEADLESS = os.environ.get("HEADLESS")
    TRACING = os.environ.get("TRACING")
