from bs4 import BeautifulSoup

html_string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Development</title>
    <style>
        h1{
            color: blue;
        }

        #CSS{

            color: chartreuse;
        }
        .porgs{
            color: cornflowerblue;
        }
    </style>
</head>
<body>
    <h1>Web Development</h1>
    <h3>Programming language</h3>
    <ol>
        <li class="porgs">HTML</li>
        <li id="CSS">CSS</li>
        <li class="porgs">JavaScript</li>
        <li>Python</li>

    </ol>
    
</body>
</html>
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html.prettify())
# print(parsed_html)
# print(type(parsed_html))
# print(parsed_html.body)
# print(parsed_html.find_all('li'))
# parsed_li = parsed_html.find_all(class_='porgs')
# print(parsed_li)

print(
    parsed_html.select('.porgs')[0])