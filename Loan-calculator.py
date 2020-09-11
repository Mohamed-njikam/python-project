import argparse
import math

parser = argparse.ArgumentParser(description="Calculator which can compute annual payment and differentiated payment")
parser.add_argument('--type', type=str, help="Which type of loan payment do you want to calculate?")
parser.add_argument('--payment', type=float, help="Enter the annual monthly payment")
parser.add_argument('--principal', type=float, help="Enter the credit principal")
parser.add_argument('--periods', type=float, help="Enter the number of month")
parser.add_argument('--interest', type=float, help="Enter the credit interest")

parameters = parser.parse_args()

#  Variables present all through the code

calculation_type = parameters.type
principal = parameters.principal
payment = parameters.payment
interest = parameters.interest
periods = parameters.periods
years = 0
months = 0
dif_payment = 0
nom_interest = 0
overpayment = 0  # amount of interest paid over the lifetime of the loan
dif_payment_lst = []


def diff_payment(cred_principal, num_period, cred_interest):
    global dif_payment, nom_interest, overpayment
    nom_interest = (cred_interest / 100) * 1 / 12
    for m in range(1, int(num_period) + 1):
        dif_payment = math.ceil(cred_principal / num_period + nom_interest *
                                (cred_principal - cred_principal * (m - 1) / num_period))
        dif_payment_lst.append(dif_payment)
        overpayment = sum(dif_payment_lst) - cred_principal
        print(f"Month {m}: payment is {dif_payment}")


def num_monthly_payment(ann_payment, cred_principal, cred_interest):
    global periods, years, months, nom_interest, overpayment
    nom_interest = (cred_interest / 100) * (1 / 12)
    period = math.log(ann_payment / (ann_payment - nom_interest * cred_principal), 1 + nom_interest)
    if period > 12:
        years = math.floor(period / 12)
        months = math.ceil(period % 12)
        if years == 0:
            overpayment = (ann_payment * round(period)) - cred_principal
            print(f'It will take {months} months to repay this loan!')
            print(f"Overpayment = {int(overpayment)}")
        elif months == 12:
            years += 1
            if years < 2:
                overpayment = (ann_payment * round(period)) - cred_principal
                print(f'It will take {years} year to repay this loan!')
                print(f"Overpayment = {int(overpayment)}")
            else:
                overpayment = (ann_payment * round(period)) - cred_principal
                print(f'It will take {years} years to repay this loan!')
                print(f"Overpayment = {int(overpayment)}")
        else:
            overpayment = (ann_payment * round(period)) - cred_principal
            print(f'It will take {years} years and {months} months to repay this loan!')
            print(f"Overpayment = {int(overpayment)}")
    elif period == 12:
        overpayment = (ann_payment * round(period)) - cred_principal
        print(f'It will take {years} year to repay this loan!')
        print(f"Overpayment = {int(overpayment)}")
    else:
        overpayment = (ann_payment * round(period)) - cred_principal
        print(f'It will take {period} months to repay this loan')
        print(f"Overpayment = {int(overpayment)}")


def credit_principal(ann_payment, num_period, cred_interest):
    global principal, nom_interest, overpayment
    nom_interest = (cred_interest / 100) * (1 / 12)
    principal = math.floor(ann_payment / ((nom_interest * math.pow(1 + nom_interest, num_period)) /
                                     (math.pow(1 + nom_interest, num_period) - 1)))
    overpayment = (ann_payment * num_period) - principal
    print(f"Your loan principal = {principal}!")
    print(f'Overpayment = {int(overpayment)}')


def ann_monthly_payment(cred_principal, num_period, cred_interest):
    global payment, nom_interest, overpayment
    nom_interest = (cred_interest / 100) * (1 / 12)
    payment = math.ceil(cred_principal * ((nom_interest * math.pow((1 + nom_interest), num_period)) /
                                          (math.pow(1 + nom_interest, num_period) - 1)))
    overpayment = (payment * num_period) - cred_principal
    print(f"Your annuity payment = {payment}!")
    print(f"Overpayment = {int(overpayment)}")


if calculation_type == "diff":
    if payment is not None:
        print("Incorrect parameters.")
    else:
        diff_payment(cred_principal=principal, num_period=periods, cred_interest=interest)
        print(f'\nOverpayment = {int(overpayment)}')

elif calculation_type == "annuity":
    if payment is not None and principal is not None and interest is not None and periods is None:
        num_monthly_payment(ann_payment=payment, cred_principal=principal, cred_interest=interest)
    elif payment is not None and periods is not None and interest is not None and principal is None:
        credit_principal(ann_payment=payment, num_period=periods, cred_interest=interest)
    elif principal is not None and periods is not None and interest is not None and payment is None:
        ann_monthly_payment(cred_principal=principal, num_period=periods, cred_interest=interest)
    else:
        print("Incorrect parameters.")