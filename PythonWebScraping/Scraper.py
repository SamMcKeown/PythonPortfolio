import requests
from bs4 import BeautifulSoup
# To send email
from smtplib import SMTP

## Product URL: assign desired amazon product
product_url = ''
desired_product = product_url

## Desired price: assign desired price
desired_price = 0
desired_price = desired_price

## User agent: characteristic string that enables servers & network peers to identify 
## the application, operating-system, vendor, & version of the requesting user agent
headers = {''}

def check_price():
    '''Sends email if product price matches the desired product price'''
    
    # Returns data
    page = requests.get(url=desired_product, headers=headers) 
    # Parses data
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Returns 'title' tag of product
    title = soup.find(id='productTitle').get_text()
    # Prints 'title' : removes whitespace
    print('Item: %s' %(title.strip()))
    
    # Returns 'price' tag of product
    price = soup.find(id='priceblock_ourprice').get_text() 
    # Prints price : removes whitespace
    print('Price: %s' %(price.strip()))

    # Converts price to float
    converted_price = float(price[:3]) 

    # Calls send_mail() : if price of amazon product <= desired price
    if(converted_price <= desired_price):
        send_mail()

def send_mail():
    '''Establishes a connection to server, logs into email account & sends an email to desired address''' 

    ## Launches an SMTP session : default mail submission port = 587
    server = SMTP(host='smtp.gmail.com', port=587) 

    ## Identifies application to an ESMTP server
    server.ehlo()

    ## Encrypts the connection
    server.starttls()

    ## Identifies application to an ESMTP server : post-encryption
    server.ehlo()

    ## Enables SMTP server authentication 
    server.login(user='email_address@gmail.com', password='login/password')

    ## Email composition
    subject = 'Amazon price drop!'
    body = 'Click the Amazon link: ', desired_product 
    custom_message = f'Subject: {subject}\n\n{body}'
    
    ## Sends email
    server.sendmail(from_addr='email_address@gmail.com', 
                    to_addrs='email_address@gmail.com', 
                    mes=custom_message)

    ## NOTE: only prints if email is successfully sent
    print('Email Sent')

    ## Terminates SMTP session & closes connection
    server.quit()

## Execute amazon price check
check_price()