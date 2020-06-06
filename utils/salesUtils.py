import datetime


def get_today():
    current_daytime = datetime.datetime.now()
    currnt_date = str(current_daytime)[:10]
    return currnt_date

def get_today_orders(all_orders):
    today_orders = []
    for order in all_orders:
        if str(order.time_created).startswith( get_today() ):
            today_orders.append(order)
    return today_orders
    
def get_today_sales(today_sales):
    total_sales_amount = float(0)
    for sales in today_sales:
        total_sales_amount += float(sales.total_order_cost)
    return total_sales_amount

def get_incomplete_orders(today_sales):
    incomplete_orders = list()
    for order in today_sales:
        if order.outstanding < 1:
            incomplete_orders.append(order.id)
    return incomplete_orders

def get_paid_orders(today_sales):
    paid_orders = list()
    for order in today_sales:
        if order.amount_paid > 1:
            paid_orders.append(order.id)
    return paid_orders

def get_total_amount_paid_on_orders(today_sales):
    total_amount_on_paid_orders = float(0)
    for order in today_sales:
        if order.amount_paid > 0:
            total_amount_on_paid_orders += float(order.amount_paid)
    return total_amount_on_paid_orders

def get_total_outstanding(today_sales):
    total_outstanding = float(0)
    for order in today_sales:
        if order.outstanding > 0:
            total_outstanding += float(order.outstanding)
    return total_outstanding

