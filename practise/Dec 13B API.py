import requests
#to download the image
#get scenarios
r = requests.get("http://imgs.xkcd.com/comics/python.png")
print(r)
print(r.status_code)
#print(r.text)
f = open("D:\\sample2.png","wb")
f.write(r.content)
print(r.content)
f.close()