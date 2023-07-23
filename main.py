import io
import os
import re
import shutil

from bs4 import BeautifulSoup
import nest_asyncio
from requests_html import HTMLSession


def main():
    # create pictures folder if not exists
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
    # read bookmarks.html
    with io.open("bookmarks.html", "r", encoding="utf8") as f:
        bookmarks = f.read()
        # find all links
        links = re.findall(
            "http://prntscr.com/[a-zA-z0-9]+|http://prnt.sc/[a-zA-z0-9]+", bookmarks
        )

        i = 0
        for link in links:
            i += 1
            # apply nest_asyncio to avoid RuntimeError: This event loop is already running
            nest_asyncio.apply()

            # get html
            session = HTMLSession()
            r = session.get(link)

            # parse html for a link to image
            html_str = r.text
            soup = BeautifulSoup(html_str, "html.parser")
            img_link = re.findall(
                "i.imgur.com/[a-zA-z0-9]+.png|i.imgur.com/[a-zA-z0-9]+.jpg|image.prntscr.com/image/[a-zA-z0-9]+.png|image.prntscr.com/image/[a-zA-z0-9]+.jpg",
                str(soup),
            )
            # if link found, get image
            if len(img_link) > 0:
                print(i, img_link[0])
                image_url = "http://" + img_link[0] + "?"

                filename = "pictures/" + str(i) + ".png"

                session = HTMLSession()
                r = session.get(image_url, stream=True)

                # save image
                if r.status_code == 200:
                    r.raw.decode_content = True

                    with open(filename, "wb") as f:
                        shutil.copyfileobj(r.raw, f)


if __name__ == "__main__":
    main()
