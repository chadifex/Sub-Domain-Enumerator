import requests
import sys

sub_list = open("subdomains.txt").read() # reads subdomain list
subdoms = sub_list.splitlines() # splits subdomains into lines

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}"  # gets input fro command line

    try:
        requests.get(sub_domains) # makes get request to sub_domains variable

    except requests.ConnectionError: # if connect error pass
        pass # makes nothing happen

    else:
        print("Valid domain: ",sub_domains)