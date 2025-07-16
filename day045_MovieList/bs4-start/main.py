from bs4 import BeautifulSoup

with open(file="website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())

all_anchor_tag = soup.findAll(name="a")
print(all_anchor_tag)
for tag in all_anchor_tag:
    # print(tag.getText())
    print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.getText())

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())

# using tags as css selector
company_url = soup.select_one(selector="p a")
# print(company_url)
print(company_url.get("href"))

# using the id as css selector
name = soup.select_one(selector="#name")
print(name.getText())

# using class as a css selector
heading = soup.select_one(".heading")
print(heading.getText())
