# DOCUMENTATION

## P2P Lending 

base url : https://loanendpoint.onrender.com/

Endpoint: /loan/borrow

Methods: POST, GET
POST Example:
You can create a new loan request by sending a POST request with JSON data. Here's an example JSON request to create a new loan request:

json
Copy code
POST /loan/borrow
{
    "BorrowerId": 2,
    "LoanAmount": 12000,
    "Interest": 16,
    "LoanTimeFrame": 4
}
GET Example:
To retrieve all existing loan requests, send a GET request to /loan/borrow with no request body.

Endpoint: /loan/lender

Methods: POST, GET
POST Example:
You can create a new lend request by sending a POST request with JSON data. Here's an example JSON request to create a new lend request:

json
Copy code
POST /loan/lender
{
    "LenderId": 1,
    "LendAmount": 12000,
    "Interest": 16,
    "LoanTimeFrame": 4
}
GET Example:
To retrieve all existing lend requests, send a GET request to /loan/lender with no request body.

Endpoint: /loan/MergeLoan

Methods: POST, GET
POST Example:
You can merge a loan request by sending a POST request with JSON data. Here's an example JSON request to merge a loan:

json
Copy code
POST /loan/MergeLoan
{
    "BorrowerId": 2,
    "LenderId": 1,
    "LoanAmount": 12000,
    "Interest": 16,
    "DueDate": 4
}
GET Example:
To retrieve all existing merged loans, send a GET request to /loan/MergeLoan with no request body.

Endpoint: /loan/user

Methods: POST, GET, PUT
POST Example:
You can create a new user by sending a POST request with JSON data. Here's an example JSON request to create a new user:

json
Copy code
POST /loan/user
{
    "UserId": 4,
    "Balance": 50000
}
GET Example:
To retrieve all existing users, send a GET request to /loan/user with no request body.

PUT Example:
You can update the balance of an existing user by sending a PUT request with JSON data. Here's an example JSON request to update the balance of an existing user:

json
Copy code
PUT /loan/user
{
    "UserId": 4,
    "Balance": 60000
}

## Customer Chat App

base url : https://chatbot-i79l.onrender.com/bot

There is only one request method which is post

post the username and the message in json format to the api
