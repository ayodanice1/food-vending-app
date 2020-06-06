# Using the API's: Form Fields Required


#### GET-POST /api/login/

* Login view. Customer and Vendor users.

#### GET /api/logout/
* Logout view. Customer and Vendor users.

#### GET /api/users/ 
* List of users. Admin user only.

#### GET /api/users/<int:pk>/
* User detail. Admin user only.

#### GET /api/vendors/
* List of vendors. Customer user only.

#### GET /api/vendors/<int:pk>
* Vendor detail. Customer user only.

#### POST /api/vendors/register/
* Register a new vendor. No user resctrictions.

#### GET/api/customers/
* List of customers. Vendor users only.

#### GET /api/customers/<int:pk>/
* Customer detail. Vendor users only.

#### POST /api/customers/register/
* Register a new customer. No user restrictions.

#### GET /api/sales/
* Get daily sales records. Vendor users only.

#### GET /api/menus/
* List of available menus. Vendor and Customer users, no Anonymous.

#### GET /api/menus/<int:pk>/
* Menu detail. Vendor and Customer users, no Anonymous.

#### PUT /api/menus/<int:pk>/update/
* Update a menu item detail. Vendor user only.

#### POST /api/menus/<int:pk>/purchase/
* Purchase a menu item. Customer user only.

#### POST /api/menus/add/
* Add new menu item. Vendor user only.

#### GET /api/orders/
* List of orders. Vendor and Customer users, no Anonymous.

#### GET-POST-DELETE /api/orders/
* View-Update-Cancel an order.
* View. Vendor and Customer users, no Anonymous.
* Update. Vendor user only.
* Cancel. Customer user only.

#### POST /api/orders/<int:pk>/checkout/
* Pay for an order.

#### GET /api/notifications/
* List of notifications received and sent. Vendor and Customer users, no Anonymous.

#### GET /api/notifications/<int:pk>/
* View a notification. Vendor and Customer users, no Anonymous.

#### POST /api/notifications/send/
* Send a notification. Vendor and Customer users, no Anonymous.