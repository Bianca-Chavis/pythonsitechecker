#import urllib
#use urllib.request to get data from the url
#write a function that takes a url and returns a response


import urllib.request as urllib

def main(url):
    print("Checking connectivity ")
    response = urllib.urlopen(url)
    print("Connected to ", url, "successfully")
    print("Status code: ", response.getcode())


print("This is a site connectivity checker programme")
input_url = input("input a url to check if it is reachable: ")
main(input_url)

