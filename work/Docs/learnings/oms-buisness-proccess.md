## Some Discusstions: 

Parent product and varient : both must be true as in the service they have written to take out parent-product but in my case product is varient and parent product both because of that the condition become false and then index stoped.

## Fulfillment Proccess

Brokering Engine -> WMS feed jati hai about about orders -> Fullfillemnt and then imported to DB-> then inv which store has clearely visible via UI. 

fullfillmentallocation -> inventory reservation

Fullfillment UI

there are diffrent facilty we will process them in batch in picking packing and ship

picklist -> order with store inforamtion

packing slip -> fullfillment , Shipping label

1. Import Brokered order feed and save in DB.
2. Inventory, consumed ,available, allocated apt,quea IMS.
3. ERP provides Inventory reset field which will gives acutal track of inventory.
4. Purchse Order Incoming shipment will come into store, from: loc to: me, from:me ,to :client
Recieving app will tell us hooms-buisness-proccessoms-buisness-proccessw much inv came and gone.
5. Cycle count/ Pysical count : d/m/y, actual and vertuall count we are doing some sort of activity to reconcile the item by using cycle count.

Atually a person will pysically count the item from instore according to our given count, 

Inventory_varience field records the + , - in the inv while 

6. outbound shipment tracking leassing of inv.

7. Shipment recieving ASN : Advance shipment notification -> that some items have come, take those notification and make draft status

from warehouse the store will got the inv and then we got in store and HC got ASN

8. At the day end we have to conclude the final count of inv, source of truth might be : ERP, Pysical person

we have to that for showing money status and for financial planing.

Is there any frequency to generate picklist, and when should customer.

## How workflow works

1. order book from shopify
2. from shopify api we sync order to our end.
3. Map here and do the processing if it is fresh then a order with created status is created.
4. Now you can track the orders on OMS. and a job run to approve all of them.
5. And after that Brokering Engine runs where it will evaluvate the eligibility of order based on brokering rules(which allocates the facility to order which is best suited for buisness senerios decisions based on shipping distance LSA priority availability shop,warehouse,waited one).
6. And then pick, pack, ship from fulfillment
7. it will generate the picklist for the shoppers to search for the orders 
8. And then picklist and shipping labels printed.
9. Carrier configuration maintained on our side like box, box type 
10. Here we maintain the assignies shoppers while generating the picklist so the responsibilty/creadit for work easily maintained.
11. and then pack and slip.     

## OMS Table Whose OutLine I got while doing so

order_header
order_item
order_status

shipment
shipment_group
shipmentGroupAssoc -> orderItem
shipmentStatus

return_header
return_item
return_status

product
productCategory -> parentCategory and inchilds also
productRollover : this will create child and parent hierarchy
(cross cell, less cell,all bougthout)
(product virtual and varient) 
ProductTypeId -> Standard, Scrollable.

good_identification


party 
partyRoleType
ContactMechanism
ContactMechPurpose
UserLogin
UserLoginSecurityGroup
SecurityGroup
SecurityPremission
SecutiyGroupPermission


facillity
facilityStatus

## We in hotwax maintains the multiple OrderType Flags

1. Transaction_Order : here we are talking about the inventory shifts from warehouse to shop.
2. Sales_Order : 
3. Purchase_Order : 

--------------------------------------------------------------------------------------------------------------------------------------------------------
# StoreFullfillmentServices 

and events inside the fulfillment component why we are saying store why not warehouse as in oms we treat all of them as facility and facility-type will distinguish them in store and warehouses.

# Shipping Integration =>
 
 shipping -> gatway ->common->shippingGatewayServices.java
 shipping -> warehouseServices -> shipping.properties throw this warehouseServices run diffrent   services on different scenrios and we can configure it from entity-engine also.
 
 - Carrier store as party and based on roleType it is distinguish that it is an carrier.
-----------------------------------------------------------------------------------------------

 DoRateShopping -> easyPost integration(multiple carrier integration find the best among of them).
 Currently we are just supporting one carrier at a time, from that we just pick the cheaper one.
 
 
 - latelong ke liya default handling ho shakti hai
 - Double click of facility-group assigning will associate multi facility-group to facilityID
 - We can provide support for dummy-carrier, if some brand does not support carrier shipping labels then this would help us a lot.
 - Critical we need to find prevention for the shopify-api failure when making bulk updates.
 - We need to remove that job as it is not needed. For removing we removed its enum but forget to stop that job. We need to remove that job from draftJobs also. 
I need to explore slightly about 1st time setup I think we simply update the upload data. 

------------------------------------------------------------------------------------------------------------------------------------------
There are 2 Types of Aggreator Services

1. RequestShippingAggregator
2. ResponseShippingAggregator

This methods overided by the Shipping plugins like fedex, c807

- When we are building the picklist this flow works, createPicklist-> Picklist entity auto-update this things.

# On shipment click button

updateShipment -> doRateShopping -> updateShipmentRouteSegment -> acceptShipment

# Picking related things are handled by entity realted to

- PickListItem enitity

-> On Pack it is marked as PickItem_PICKED

packStoreFulfillmentOrder


-> On unPack it is marked again in not Picked status

unlockStoreFulfillmentOrder

-> Create Shipment flow `createShipment` 

Running Service ECA Service: setShipmentSettingsFromFacilities, triggered by rule on Service: createShipment

----------------------------------------------------------

Running Service ECA Service: createPicklistStatusHistory, triggered by rule on Service: updatePicklist
2024-06-28 20:09:52,038 |OFBiz-JobQueue-1     |PrimaryKeyFinder              |I| Returning null because found incomplete primary key in find: [GenericEntity:PicklistStatusHistory][createdDate,null()][picklistId,10040(java.lang.String)]


ShipmentServices.xml#setShipmentSettingsFromPrimaryOrder line 630] Cannot find a shipping o

---------------------------------------------------------
performFind -> PrepareFind -> ExecuteFind  and Here Prepared Query would be executing the Query.

and for some process in packing we are using this type of api which directly deals with entity and change there status
Shipment
ShipmentPackageRouteSegement
ShipmentRouteSegment
OrderShipment
------------------------------------------------------------

## On packing this flow triggers
updateShipment and OISG indexing is done here.

updateShipment-> doRateShopping -> updateShipmentRouteSegment -> acceptShipment


-------------------------------------------------------
## on retrying for the shipping labels
retryShippingLabel -> RateShopping service called here -> AcceptShipment
---------------------------------------------------------
## On Marking Shipped the order

1. shipOrder called. -> service-multi and it calles the updateShipment flow.

2. Shipment and ShipmentPackageRouteSegDetails


 
--------------------------------------------------------------------------------------------------------------------------
## Brokering OrderItemMissing case
The Error we are talking about order item missing while brokering, It arise in that situation when all other orders are in brokered state and 1 order has to in NA unfillable parking because it is, partial canceled reason it wents to brokering and return from brokering because it is in cancel or rejected state.


## ShopifyWebhookSubscribe

We subscribe a shopify webhook which triggers whenever there is change in inventory on shopify and update on our side.
- inventoryLevelUpdateFromShopify : resetInventoryByIdentification(product,facility)

## Jobs hourly run for taking sync from the shopify
- updateOrderItems
- updateOrderItemsShippingAddress
- importOrder
- importShipment
- importProduct
- SyncProduct for existings
- importOrderAttributes
- importCanceledOrders

- Brokering
- Fulfillment


## Jobs Vs Webhook

Jobs periordically
Webhook not efficent for bulk.


## DataManager Vs SystemMessageRemote

DataManager Configuration are for using export files and process them and currently we would support the csv,xls,json formate , It will simply pick the data from the Sftp and process the data as configured and execute the service mentioned in the data.  DataManagerConfig config handles and store configuration data about different jobs configured.

SystemMessageRemote is simply entity which holds the 3rd party credentials helps manage them.



# Transfer Orders

- Wharehouse to store 
- Store to Warehouse
- Store to Store

shipments are created with shipment_type -> Transfer_Order

## Product-Store

We can configure the product-store how much the Retailers wanted to deal and manging all throw product-store would help in inventory balancing.
Here Product-Store represents multiple brands 

For each product-store we would associate 
1. Product-catelog :  A product catalog for the newly created product store needs to be created which defines which product will be sold through the created product store.
2. ProductStoreCatelog : Association of catelog to product.

3. ProductCategory : Category help manging back-order,pre-order products
4. ProdCatalogCategory
Add Default Data
- In which you can provide the facility which sells that brand 

Locate the facility page in the Warehouse section
Upload the CSV file for the Facility along with the facility name and location for the WS_STORE product store. You can download the sample CSV to add the data according to the template provided.

These steps create the product store in HotWax Commerce. Ensure facilities that sell products of that brand are linked to the respective store. This association can be accomplished through the following steps:
- Customers wants to manage differently, or we are doing to maintain invenoty balances
- Products are connected throw productStore and there is same facility can be attached to multiple productStore because they sell multiple brands.


In HotWax Commerce, effective product management involves creating product categories, especially for handling pre-order and backorder products. The following attributes are essential for accurately defining product categories:
Make sure to customize all product category IDs and names, and consider adding a company name prefix or suffix to the IDs. It's crucial not to alter any type IDs as specified in the note above. This process ensures accurate and tailored product categorization within HotWax Commerce.

-----------------------------------------------------------------------------------------------------------------------------------
## Logs Configuration
Level : Which define or introduce the another level : we have to use this to create another level. 
Debug : Warraper over LogManger for our custom configuration and management.
log4j.xml : Lib releated and purging and policy management of logs are done here. Here we define what would be the pattern of logs here.
fetchLogs.groovy file which feches the logs and showcase in the webtool screen.

- We still wanted to add the logs in Error category.

Now I need to check the patterns what if we change this logs what problem would occure
And error.log file also created 

In fetchLogs.groovy where I have to change fetchLogs.groovy include B

In some isON() things are written what do we do about it.

