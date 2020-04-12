### Funnel ###
# The objective is to find out how many people continue to the next step of a multi-step process.
import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

##### Inspecting the data
print(visits.head())

##### Combining visits and cart.
visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart)

##### How long is the merged DataFrame?
visits_cart_rows = len(visits_cart)

##### How many of the timestamps are null for the column cart_time?
null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()]) 
print(null_cart_times)

##### What percent of users who visited, ended up not placing a t-shirt in their cart?
print((null_cart_times)/(visits_cart_rows))   

##### What percentage of users put items in their cart, but did not proceed to checkout?
cart_checkout = pd.merge(cart, checkout , how='left')
#print(cart_checkout)
cart_checkout_rows = len(cart_checkout)
null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
print((null_checkout_times)/(cart_checkout_rows))

##### What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase = pd.merge(checkout, purchase, how='left')   
checkout_purchase_rows = len(checkout_purchase)          
null_purchase_times =  len(checkout_purchase[checkout_purchase.purchase_time.isnull()]) 
print((null_purchase_times)/(checkout_purchase_rows)) 

##### Merging all four steps of the funnel.
all_data = visits.merge(cart, how='left')               \
                 .merge(checkout, how='left')           \
                 .merge(purchase, how='left')
print(all_data.head())

##### calculating the average time from initial visit to final purchase.
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data.head())

##### Examining the result
print(all_data.time_to_purchase)

##### Calculate the average time to purchase:
print(all_data.time_to_purchase.mean())

#######################################################################################################






