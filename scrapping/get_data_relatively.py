from bs4 import BeautifulSoup

with open('E:\\dev\\html_css_intro\index.html', 'r') as html:
    html_string_value = html.read()


parsed_html = BeautifulSoup(html_string_value, 'html.parser')

# data = parsed_html.body.contents[2].next_sibling.next_sibling
# print(data)

# data = parsed_html.find(id="CSS-li").parent.previous_sibling.previous_sibling

# data = parsed_html.find(id="CSS-li").find_next_sibling().find_previous_sibling()
#
data = parsed_html.body.findChildren()[2].find_next_sibling()
print(data)