from bs4 import BeautifulSoup

with open('E:\\dev\\html_css_intro\index.html', 'r') as html:
    html_string_value = html.read()

# print(html_string_value)

# html_string = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Web Development</title>
#     <style>
#         h1{
#             color: blue;
#         }
#
#         #CSS{
#
#             color: chartreuse;
#         }
#         .porgs{
#             color: cornflowerblue;
#         }
#     </style>
# </head>
# <body>
#     <h1 class="green">Web Development</h1>
#     <h3>Programming language</h3>
#     <ol>
#         <li class="green">HTML</li>
#         <li id="CSS">CSS</li>
#         <li class="green bold siski">JavaScript</li>
#         <li>Python</li>
#
#     </ol>
#
# </body>
# </html>
# """

parsed_html = BeautifulSoup(html_string_value, 'html.parser')
# print(parsed_html.prettify())
# print(parsed_html)
# print(type(parsed_html))
# print(parsed_html.body)
# print(parsed_html.find_all('li'))
# parsed_li = parsed_html.find_all(class_='porgs')
# print(parsed_li)

# html_elem = parsed_html.select('.porgs')[1]
# print(html_elem.get_text())

# html_elem_list = parsed_html.select('li')
# for elem in html_elem_list:
#
#     print(elem.get_text())

html_elem_list = parsed_html.select('li')
for elem in html_elem_list:

    print(elem.attrs)