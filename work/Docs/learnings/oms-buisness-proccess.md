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


 
 

ShopifyFullfillmentEvents 

 try {
        chain.doFilter(req, resp);
        
        } catch (SAMLAuthnInstantException saie) {
            if (saie.getMessage().toString().equals("Authentication issue instant is too old or in the future")) {
            
                Saml2SSOEvent.saml2CheckCentralLogout(req,resp);
            }
            else {
                throw saie;
            }
        }
        
   
 gatewayRateRequestWrapper -> getShippingRate  
   
        
## With Rollup function :
        
- With Rollup:  clause helps in including and working over aggregated data, what chunks we have create we can further apply operation and include into existing set of rows.

- The with rollup option allows you to include extra rows that represent subtotals and grand totals.


Like total-cost, totalscore, totalcount.

Question: we want the payment of the year per year and per store.
         
## Ranking in sql : 

Dense Rank


aditi@786

https://git.hotwax.co/devops/grafana-monitoring/-/tree/develop/setup-documentation?ref_type=heads

There are 3 sections inside setup-documentation

1. Monitoring : It contains the intials information about the setup of monitoring patterns in grafana.
2. import_export.md : It contains the details about how we would importing the templated in grafana.
3. monitoring-setup : It contains information about the Local monitoring setup.
4. setup monitoring for new instances : This contains details about how we can configure the built in alert for new instances in one shot.


ServiceFields={shipToAddress={destinationAddressCountryCode=US, destinationAddressLine1=2198 Riverside Avenue, destinationAddressStateCode=WA, destinationAddressToName=Jake Paul, residentialAddress=true, destinationAddressPostalCode=99201, destinationAddressCity=Paso Robles, destinationAddressLine2=null}, productStoreShipMethId=10000, facilityId=STORE_1, packages=[{packageCode=YOUR_PACKAGING, length=15.000000, width=10.000000, dimensionUnit=in, weight=0.661400, weightUnits=lb, weightUomId=WT_lb, shipmentPackageSeqId=00001, height=5.000000}], shippableTotal=1.000000, userLogin=[GenericEntity:UserLogin][createdStamp,2023-11-21 15:05:42.874(java.sql.Timestamp)][createdTxStamp,2023-11-21 15:05:42.766(java.sql.Timestamp)][currentPassword,$SHA$UyRieCXGA1nZ6v$KYIotRGt-LPjDbqAJiT-VEUiH18(java.lang.String)][disabledBy,null()][disabledDateTime,null()][enabled,Y(java.lang.String)][externalAuthId,null()][hasLoggedOut,N(java.lang.String)][isExternal,null()][isSystem,null()][lastCurrencyUom,null()][lastLocale,en-US(java.lang.String)][lastTimeZone,Asia/Calcutta(java.lang.String)][lastUpdatedStamp,2024-07-02 15:24:46.786(java.sql.Timestamp)][lastUpdatedTxStamp,2024-07-02 15:24:46.779(java.sql.Timestamp)][partyId,HOTWAX_USER(java.lang.String)][passwordHint,null()][requirePasswordChange,N(java.lang.String)][successiveFailedLogins,0(java.lang.Long)][userLdapDn,null()][userLoginId,hotwax.user(java.lang.String)], carrierPartyId=FEDEX, shipmentRouteSegmentId=00001, currencyUomId=null, shipFromAddress={originAddressLine2=null, originAddressStateOrProvinceCode=UT, originAddressToName=null, originAddressCountryCode=US, originAddressCity=Salt Lake City, originAddressPostalCode=84101, originAddressLine1=1110 S 300 W}, shipmentId=10060, totalWeight=0.661400, weightUomId=WT_lb, productStoreId=STORE, shipmentMethodTypeId=STANDARD}


