import imgkit         # refer to the documentation https://pypi.org/project/imgkit/ requires https://wkhtmltopdf.org/downloads.html

options = {
    'format': 'png'
}

config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
# imgkit.from_string(html_string, output_file, config=config)


#imgkit.from_url('https://google.com', 'google.png', options=options)  # from url

imgkit.from_file('test.html', 'test.png', options=options , config=config)   # when supplied from file

# or

# with open('file.html') as f:
#     imgkit.from_file(f, 'out.png')



# body = """
# <html>
#   <head>
#     <meta name="imgkit-format" content="png"/>
#     <meta name="imgkit-orientation" content="Landscape"/>
#   </head>
#   Hello World!
# </html>
# """

# imgkit.from_string(body, 'out.png')    # when use from strings  #instead of body string we can also use curl in linux 


# Single CSS file
# css = 'example.css'               # specified single css file
# imgkit.from_file('file.html', options=options, css=css)

# Multiple CSS files
# css = ['example.css', 'example2.css']     # specified multiple css file
# imgkit.from_file('file.html', options=options, css=css)
