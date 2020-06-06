
def handle_order_cancellation(request_method, order):
    if order.amount_paid >= order.outstanding:
        order.order_status = 'CANCELLED'
        order.save()
        order.outstanding = 0
        order.save()
        return True
    else:
        try:
            pay = float( request_method.get('amount_paid') )
        except:
            return False
        else:
            order.amount_paid = float( order.amount_paid ) + pay
            order.save()
            if order.amount_paid >= order.outstanding:
                order.order_status = 'CANCELLED'
                order.save()
                order.outstanding = 0
                order.save()
                return True
            else:
                return False

def handle_order_payments(request_method, order):
    try:
        pay = float( request_method.get('amount_paid') )
    except:
        order.order_status = 'CANCELLED'
        order.save()
        order.outstanding = 0
        order.save()
        return False
    else:
        order.amount_paid = pay
        order.save()
        
        order.outstanding = float( order.outstanding ) - pay
        order.save()
        
        if float( order.outstanding ) > 1:
            order.payment_status = 'PART-PAID'
            order.save()
        else:
            order.payment_status = 'FULLY-PAID'
            order.save()

        return True
    
