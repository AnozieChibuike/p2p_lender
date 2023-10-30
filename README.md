
P2P Lending API
---------------

### Base URL: [https://loanendpoint.onrender.com/](https://loanendpoint.onrender.com/)

### /loan/borrow

Methods: POST, GET

#### POST Example:

POST /loan/borrow
{
    "BorrowerId": 2,
    "LoanAmount": 12000,
    "Interest": 16,
    "LoanTimeFrame": 4
}
    

#### GET Example:

To retrieve all existing loan requests, send a GET request to /loan/borrow with no request body.

### /loan/lender

Methods: POST, GET

#### POST Example:

POST /loan/lender
{
    "LenderId": 1,
    "LendAmount": 12000,
    "Interest": 16,
    "LoanTimeFrame": 4
}
    

#### GET Example:

To retrieve all existing lend requests, send a GET request to /loan/lender with no request body.

### /loan/MergeLoan

Methods: POST, GET

#### POST Example:

You can merge a loan request by sending a POST request with JSON data. Here’s an example JSON request to merge a loan:

POST /loan/MergeLoan
{
    "BorrowerId": 2,
    "LenderId": 1,
    "LoanAmount": 12000,
    "Interest": 16,
    "DueDate": 4
}
    

#### GET Example:

To retrieve all existing merged loans, send a GET request to /loan/MergeLoan with no request body.

### /loan/user

Methods: POST, GET, PUT

#### POST Example:

You can create a new user by sending a POST request with JSON data. Here’s an example JSON request to create a new user:

POST /loan/user
{
    "UserId": 4,
    "Balance": 50000
}
    

#### GET Example:

To retrieve all existing users, send a GET request to /loan/user with no request body.

#### PUT Example:

You can update the balance of an existing user by sending a PUT request with JSON data. Here’s an example JSON request to update the balance of an existing user:

PUT /loan/user
{
    "UserId": 4,
    "Balance": 60000
}
    

Customer Chat App
-----------------

### Base URL: [https://chatbot-i79l.onrender.com/bot](https://chatbot-i79l.onrender.com/bot)

Request Method: POST

Post the username and the message in JSON format to the API.
