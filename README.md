## Project Title:
## Pawsome Kingdom

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Softwares Used](#ssoftwares-used)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [User Story](#user-story)
- [Pushing in Github](#pushing-in-github)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description:
Welcome to Pawsome Kingdom.This is an ecommerce website dedicated to the pet-lovers. This website allows the users to purchase any pet or any pet-related products of their interest.

The search option allows the user to search any pet items available in the website.Upon searching , users can view the details of any product .

A new unregistered user first have to register an account in order to make any purchases.
Creating an account will allow the user to add any product to their cart for purchase.Also the user is allowed to add any product of their interest into the wishlist.If the user wants, they can move any product directly 
from the wishlist to the cart for purchase.If any product is no longer of their interest, that item can be removed from the wishlist as well. Furthermore, any items which was added to the cart previously can be removed
as well if payment has not been made yet.If the order made was successful, the user can visit the **"View order"**  to view all the orders they have made so far.Any details related to the account of the user can be found in 
**"View Profile"** option.

After confirming the order, the user will be asked to proceed with the payment process where they are asked to enter the necessary credentials to make successful money transaction.If the payment was successful,the order has 
been successfully placed and the delivery will be made soon to the address provided by the user.

Furthermore, the user can learn about the process of how to use the website or about the website itself from the **"About Us"** page.If by any chance , the user wishes to file a complaint regarding an issue related to their
website or their order, they can visit the **"Contact Us"** page to fill out the complaint form.ALso for contacting the Customer Support team, necessary contact information is provided in that page.


## Features:
**1.Managing Cart Items:**
- Add,View or Delete any item from their Cart
- Users can add an product to their cart by searching the name of the product as well as by directly clicking on the **add to cart** button

**2.Managing Wishlist:**
- Add an item to the wishlist
- Remove an item from the wishlist
- An item can be added to wishlist by searching the name of the product or by directly clicking ont the **wishlist** button
- An item can be moved to cart directly from wishlist for purchase by clicking on **move to cart** button
- Can view all the items currenlty added in the Wishlist

**3.Payment:**
- User is asked to enter their payment details such as credit card or debit card number or even bKach number
- User enters the address for the order to be delivered at
- If credentials matches with the information in the database in Mysql, **Payment is successful** message is displayed
- If credentials do not match, **Payment Failed** message is displayed
- Ensures a secure payment transaction between the user and the system
- If payment is successful,order has been confirmed

**4.View Profile:**
- User can view details of their account including username
- User is allowed to change the password if forgotten
- Can edit any personal information of their account

**5.View Orders:**
- Users can view the history of all orders made so far
- Any details of any specific order can be found from here
- Can check the status of their order whether **Delivered** or **Pending**

**6.Search Product:**
- User can search any product details by entering the name of the product in the search bar

**7.View Products:**
- User can view the details of any product available in the website.

**8.About Us:**
- If user wants to learn any information related to the website,they can find the information in this page

**9.Contact Us:**
- User can file any complaint regarding any issue with their order or the website by filling out the complaint form in this page
- User can reach out to **Customer Support Team** for any kind of queries using the contact information(contact number,email address) provided in the website

## Software Used:
- **FrontEnd:** HTML,CSS
- **Backend:** Python,Django
- **Database:** MySQL
- **Communication Purpose:** Discord
- **Update Work:** Trello
- **Code Submission and Backup:** GitHub,Wiki

## Getting started
## Requirement:
- Python 3.12.4 or latest version
- Django 5.0.7 or latest version

## Installation:
To run the Pawsome Kingdom Project in your local machine,please follow the following steps:


**1.Clone The Repository**
Clone the repository to your local machine using the command:
```bash
git clone https://github.com/subahmantaka/Pawsome-Kingdom-Ecommerce-Website.git
```


**2.Navigate to your Project Folder**
```bash
cd H:\ecomm
```

**3.Set Up a Virtual Environment:**
create and activate a virtual environment for the dependencies

***For Windows***

```bash
python -m venv env
.\env\Scripts\activate
```

**4.Install Project Dependencies**
Install the python packages
```bash
winget install --id Python.Python.3.12 -e
```

Install MySql
```bash
pip install mysqlclient
```

```bash
pip install django mysqlclient
```

Install Django
```bash
pip install django
```
**5. Start a New Django Project**

```bash
django-admin startproject ec
```
**6.Create a Django App**
```bash
python manage.py startapp app
```

**7.Set Up Database**
Use MySQL for maintaining the Database
```bash
CREATE DATABASE pawsome_kingdom;
```

**8.Configure Django Settings**
Configure the Settings in your django settings to change the databse into MySQL
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pawsome_kingdom',  
        'USER': 'root',            
        'PASSWORD': 'helloworld',  
        'HOST': 'localhost',       
        'PORT': '3306',             
    }
}
```
**9.Appy Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**10.Create SuperUser**
This SuperUser is created to operate the Django Admin.The username and password of SuperUser can be found in **superuser.TXT** file
```bash
python manage.py createsuperuser
```

**11.Run The Django Server**
Run the django default server to start the server.Then use the specific urls in **urls.py** to access your desired webpages
```bash
python manage.py runserver
```

**12.Project Structure Overview**
```bash
ecomm/
├── ec/  # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── app/  # Django app folder
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── static/
│   ├── images/
│   │   └── ...
├── test/  # Unit tests folder
│   └── test_cart.py
└── ...
```
## Dependencies:

- Python
- Django
- MySQL

## User Story

1. Managing Cart Items
2. Managing Wishlist
3. Search and View Products
4. View Order
5. Contact Us
6. Make Payment
7. View Profile

## Pushing in GitHub

-Fork the repository
-create a branch for each user story function
- commit changes
  ```bash
  git checkout -b feature-name
  ```
- add
 ```bash
  git add.
  ```
- push to your branch
 ```bash
  git commit -m "Description of changes"
```

- Submit pull request
  ```bash
  git push origin feature-name
  ```
  
- Merge the branch with master branch


## Licence
This project is licensed under the MIT License. See the **LICENSE** file for more details.

## Acknowledgement

We would like to thank our faculty for guiding us thoughout the project and also our team members who were assigned the following parts:

**Suhana Islam**- Managing Cart Items ,Managing Wishlist

**Nusaiba Sharifeen**-Payment,View profile,View order

**Subah Mantaka**-View and Search product,Contact Us

We also took the help of the tools to complete our project:

-**Django** : Frameowork of our project

-**Python** : Programming Lnaguage we used

-**MySQL**: Database we used

-**Discord**: Used it for all commmunication process

-**Trello**: Used to update our work progress efficiently


 
