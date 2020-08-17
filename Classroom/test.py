from bs4 import BeautifulSoup

with open("test.html") as t:
    html = BeautifulSoup(t.read(), features="html.parser")

test = html.test
test.string = "FUNGA"

with open("test.html", "w") as out:
    out.write(str(html))
