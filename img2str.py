import base64

def pic2str(file, functionName):
    pic = open(file, 'rb')
    content = '{} = {}\n'.format(functionName, base64.b64encode(pic.read()))
    pic.close()

    with open('picstr.py', 'w+') as f:
        f.write(content)

pic2str('./example.jpg', 'img_str')
