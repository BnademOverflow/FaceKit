def to_dict_cookies(string_cookies):
    try:
        string_cookies = string_cookies.replace(" ", "")
        return dict(x.split("=") for x in string_cookies.split(";"))
    except:
        return {"datr": ""}


def to_mbasic(url):
    if not url:
        return url
    if "https://mbasic.facebook.com" not in url:
        return "https://mbasic.facebook.com" + url
    return url
