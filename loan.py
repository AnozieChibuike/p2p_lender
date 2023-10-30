from flask import request,jsonify
from datetime import datetime, timedelta
from main import app
import bson
now = datetime.now
loanRequests = [{
    'id':bson.ObjectId(),
    'UserId':2,
    'LoanAmount': 12000,
    'InterestRate': 16,
    'Active': True,
    'RequestTime': now,
    'LoanTimeFrame': '4 weeks',
    'MatchedTime':  now() + timedelta(minutes=2),
    'MatchedUserId': 1,
    'DueDate': now() + timedelta(weeks=4),
}]

users = [
    {
        'UserId': 1,
        'Balance': 100000,
    },
    {
        'UserId': 2,
        'Balance': 1000,
    },
    {
        'UserId': 3,
        'Balance': 200000,
    }
]

lendRequests = [{
    'id':bson.ObjectId(),
    'UserId':1,
    'LendAmount': 12000,
    'InterestRate': 16,
    'Active': True,
    'LendTime': now + timedelta(minutes=2),
    'ProposedLendTimeFrame': '4 weeks',
    'MatchedTime':  now + timedelta(minutes=2),
    'MatchedUserId': 2,
    'DueDate': now + timedelta(weeks=4),
}]

MergedLoans = [{
    'id':bson.ObjectId(),
    'BorrowerId':2,
    'LenderId': 1,
    'LoanAmount': 12000,
    'InterestRatePayable': 16,
    'Active': True,
    'MergedTime':  now + timedelta(minutes=2),
    'DueDate': now + timedelta(weeks=4),
}]

@app.route('/loan/borrow',methods=['POST','GET'])
def new_loan():
    if request.methods == 'POST':
        data = request.json.get
        id = bson.ObjectId()
        UserId = data('BorrowerId')
        LoanAmount = data('LoanAmount')
        Interest = data('Interest')
        Active = False
        RequestTime = now()
        LoanTimeFrame = now() + timedelta(weeks=data('LoanTimeFrame'))
        MatchedTime = None
        MatchedUserID = data('LenderID') or None
        DueDate = None
        LoanRequest = {
            'id':id,
            'UserId':UserId,
            'LoanAmount': LoanAmount,
            'InterestRate': Interest,
            'Active': Active,
            'RequestTime': RequestTime,
            'LoanTimeFrame': LoanTimeFrame,
            'MatchedTime':  MatchedTime,
            'MatchedUserId': MatchedUserID,
            'DueDate': DueDate,
        }

        loanRequests.append(LoanRequest)
        AvailableToLoan = []
        for i in users:
            if i['Balance'] > LoanAmount:
                AvailableToLoan.append(i)
        return jsonify({'availableLenders': AvailableToLoan,'BorrowerData':LoanRequest})
    return jsonify({'data': loanRequests})
@app.route('/loan/lender',methods=['POST','GET'])
def new_lend():
    if request.method == 'POST':
        data = request.json.get
        id = bson.ObjectId()
        UserId = data('LenderId')
        LendAmount = data('LendAmount')
        Interest = data('Interest')
        Active = False
        RequestTime = data('RequestTime')
        LoanTimeFrame = now() + timedelta(weeks=data('LoanTimeFrame'))
        MatchedTime = data('MatchedTime') or now()
        MatchedUserID = data('MatchedUserID')
        DueDate = None
        LendRequest = {
            'id': id,
            'UserId': UserId,
            'LendAmount': LendAmount,
            'InterestRate': Interest,
            'Active': Active,
            'RequestTime': RequestTime,
            'LoanTimeFrame': LoanTimeFrame,
            'MatchedTime': MatchedTime,
            'MatchedUserId': MatchedUserID,
            'DueDate': DueDate,
        }
        lendRequests.append(LendRequest)
        return jsonify({'LenderData': LendRequest})
    return jsonify({'data': lendRequests})

@app.route('/loan/MergeLoan',methods=['POST','GET'])
def mergedloan():
    if request.method == 'POST':
        data = request.json.get
        id= bson.ObjectId()
        BorrowerId=data('BorrowerId')
        LenderId=data('LenderId')
        LoanAmount=data('LoanAmount')
        InterestRatePayable=data('Interest')
        Active=False
        MergedTime=  now + timedelta()
        DueDate= data('DueDate')

        for i in users:
            if i['UserId'] == LenderId:
                if users[users.index]['Amount'] > LoanAmount:
                    Active = True

        MergedLoan = {
            'id':id,
            'BorrowerId':BorrowerId,
            'LenderId': LenderId,
            'LoanAmount': LoanAmount,
            'InterestRatePayable': InterestRatePayable,
            'Active': True,
            'MergedTime':  MergedTime,
            'DueDate': now + timedelta(weeks=DueDate),
        }
        if Active:
            MergedLoans.append(MergedLoan)
            return jsonify({'data': MergedLoan,'merged': True})
        else:
            return jsonify({'data':MergedLoan,'merged': False,'reason': 'Lender has low Balance'})
    return jsonify({'data': MergedLoans})

@app.route('/loan/user',methods=['POST','GET','UPDATE'])
def user():
    if request.method == 'POST':
        data = request.json.get
        UserId = data('UserId')
        Balance = data('Balance')
        li = [i['UserId'] for i in users]
        if UserId in users:
            return jsonify({'error': 'User exists'})
        users.append({'UserId':UserId,'Balance':Balance})
        return jsonify({'data': users})
    if request.method == 'UPDATE':
        data = request.json.get
        UserId = data('UserId')
        Balance = data('Balance')
        li = [i['UserId']  for i in users]
        if UserId not in users:
            return jsonify('error': 'User does not exist')
        for i,d enumerate(users):
            if d['UserId'] == UserId:
                users[i]['Balance'] = Balance
        return jsonify('data': users,'message':'updated')
    return jsonify('data': users)








