##Daily Store Activity : 73

${params.productStoreId} -> STORE
${params.startDate} TO ${params.endDate} -> 2023-01-01T00:00:00Z TO 2023-12-31T23:59:59Z

SELECT
    facilityId as fid,
    shipmentMethodTypeDesc as smtd,
    reservedDatetime as rdt,
    orderIdentifications as oi,
    orderName as oname,
    orderId as oid,
    virtualProductName as vpn,
    productName as pn,
    goodIdentifications as gid,
    isPicked as ip,
    fulfillmentStatus as fs
FROM
    `dev-oms-enterpriseSearch`
WHERE
    docType = 'OISGIR'
    AND orderTypeId = 'SALES_ORDER'
    AND shipmentMethodTypeId <> 'STOREPICKUP'
    AND facilityTypeId IN ('RETAIL_STORE', 'OUTLET_STORE')
    AND reservedDatetime IS NOT NULL
    AND productStoreId = 'STORE'
    AND (
        fulfillmentStatus IN ('Created', 'InProgress')
        OR (fulfillmentStatus = 'Completed' AND itemShippedDate BETWEEN '2023-01-01T00:00:00Z' AND '2023-12-31T23:59:59Z')
        OR ((fulfillmentStatus = 'Rejected' OR fulfillmentStatus = 'Cancelled') AND rejectDatetime BETWEEN '2023-01-01T00:00:00Z' AND '2023-12-31T23:59:59Z')
    )
ORDER BY
    reservedDatetime DESC
LIMIT
    10000;
==============================================================================================================================================================

##Daily Store Completed Orders

95
${params.productStoreId} -> STORE
${params.startDate} TO ${params.endDate} -> 2023-01-01T00:00:00Z TO 2023-12-31T23:59:59Z


SELECT
    facilityId as fid,
    WAREHOUSE_PICKER_picklist_role as wppr,
    orderIdentifications as oids,
    orderName oname,
    orderId oid,
    parentProductName as ppn,
    productName as pn,
    goodIdentifications as gids,
    itemCompletedDate as icd
FROM
    `dev-oms-enterpriseSearch`
WHERE
    docType = 'ORDER'
    AND orderTypeId = 'SALES_ORDER'
    AND orderItemStatusId = 'ITEM_COMPLETED'
    AND shipmentMethodTypeId <> 'STOREPICKUP'
    AND facilityTypeId IN ('RETAIL_STORE', 'OUTLET_STORE')
    AND itemCompletedDate BETWEEN '2023-01-01T00:00:00Z' AND '2023-12-31T23:59:59Z'
    AND productStoreId = 'STORE'
ORDER BY
    itemCompletedDate DESC
LIMIT 100

==============================================================================================================================================================

##Daily Store Cancelled Orders
1. ${params.productStoreId} -> STORE
2. ${params.startDate} TO ${params.endDate} -> 2023-01-01T00:00:00Z TO 2023-12-31T23:59:59Z
Count -> 0

SELECT
    facilityId as fid,
    WAREHOUSE_PICKER_picklist_role as wppr,
    orderIdentifications as oids,
    orderName as oname,
    orderId as oid,
    parentProductName as ppn,
    productName as pn,
    goodIdentifications as gids,
    itemCancelledDate as icd
FROM
    `dev-oms-enterpriseSearch`
WHERE
    docType = 'ORDER'
    AND orderTypeId = 'SALES_ORDER'
    AND orderItemStatusId = 'ITEM_CANCELLED'
    AND shipmentMethodTypeId <> 'STOREPICKUP'
    AND facilityTypeId IN ('RETAIL_STORE', 'OUTLET_STORE')
    AND itemCancelledDate BETWEEN '2023-01-01T00:00:00Z' AND '2023-12-31T23:59:59Z'
    AND productStoreId = 'STORE'
ORDER BY
    itemCancelledDate DESC
LIMIT 10000;


{
      "params": {
        "rows": 10000,
        "wt": "csv",
        "sort": "itemCancelledDate desc",
        "csv.header": false
      },
      "query": "docType:ORDER",
      "filter": ["orderTypeId: SALES_ORDER","orderItemStatusId: ITEM_CANCELLED",
      "-shipmentMethodTypeId : STOREPICKUP","facilityTypeId:(RETAIL_STORE OR OUTLET_STORE)",
       "itemCancelledDate:[2023-01-01T00:00:00Z TO 2023-12-31T23:59:59Z]",
        "productStoreId:STORE"],
   "fields": "facilityId,WAREHOUSE_PICKER_picklist_role,orderIdentifications,orderName,orderId, parentProductName,productName,goodIdentifications,' ',itemCancelledDate"
}

=========================================================================================================================

    "CURRENT_DATE" : It will work in the case of Interval 1 day, Year
    "CURRENT_TIME" ... : It will work with only of Interval 1 hour , minute
    "CURRENT_TIMESTAMP" ... : Here both day,hour year, minute working
    "LOCALTIME" ...
    "LOCALTIMESTAMP"
CURRENT_TIMESTAMP
CURRENT_TIME
CURRENT_DATE
LOCALTIME
LOCALTIMESTAMP

https://calcite.apache.org/docs/reference.html

=====================================================================================================================================================
