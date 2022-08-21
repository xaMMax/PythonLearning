import os
import qrcode


def createQR(url: str):
    img = qrcode.make(url)
    url = url.replace(".", "_").replace("/", "_").replace(":", "_").replace("_", "")
    print(url)
    img.save(f"{url}.png", "PNG")
    return


createQR("https://youtu.be/cFE7rjsL6r4")
