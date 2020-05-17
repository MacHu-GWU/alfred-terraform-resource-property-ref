import bs4
import json
from pathlib_mate import PathCls as Path

html = Path(__file__).change(new_basename="aws.html").read_text(encoding="utf-8")

resources_data = list()

soup = bs4.BeautifulSoup(html, "html.parser")
ul = soup.find(class_="nav docs-sidenav")
for li in ul.find_all("li", recursive=False):
    if li.a.text not in ["Data Sources", "Resources"]:
        service_name = li.a.text
        for a in li.find_all("a"):
            href = a["href"]
            if href.startswith("/docs/providers/aws/"):
                if href.startswith("/docs/providers/aws/d"):
                    type = "Data Source"
                elif href.startswith("/docs/providers/aws/r"):
                    type = "Resource"
                else:
                    break
                name = a.text.replace("_", " ")
                title = "{}: {}".format(type, name)
                url = "https://www.terraform.io" + href
                dct = {
                    "arg": url,
                    "subtitle": "Open: {}".format(url),
                    "title": title
                }
                resources_data.append(dct)

with open("ref.json", "wb") as f:
    f.write(json.dumps(resources_data, indent=4, sort_keys=True).encode("utf-8"))
