from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile

from link_gopher.config import Config


def build_driver() -> Firefox:
    profile = _build_profile()
    options = _build_options()

    return Firefox(profile, options=options)


def _build_profile() -> FirefoxProfile:
    profile = FirefoxProfile()
    profile.set_preference('http.response.timeout',
                           Config.HTTP_RESPONSE_TIMEOUT)
    profile.set_preference('dom.max_script_run_time',
                           Config.MAX_SCRIPT_RUN_TIME)

    return profile


def _build_options() -> FirefoxOptions:
    options = FirefoxOptions()
    options.headless = True if Config.HEADLESS == "true" else False
    if Config.TRACING:
        options.log.level = "trace"

    return options
