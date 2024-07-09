SELECT sme.system_message_id,
       sm.product_store_id,
       sm.system_message_type_id,
       smt.description,
       sm.order_id,
       CONVERT(sm.last_attempt_date, CHAR) AS 'LAST_ATTEMPT_DATE',
       CONVERT(sme.error_date, CHAR)       AS 'ERROR_DATE',
       sme.error_text
FROM   system_message_error sme
       LEFT JOIN system_message sm
              ON sme.system_message_id = sm.system_message_id
       LEFT JOIN system_message_type smt
              ON smt.system_message_type_id = sm.system_message_type_id
WHERE order_id IS NOT NULL

3744 has to be run on the email but actually attached one is 3863 -> chinmay edited the connected dataset and limit in 3863 chart

might be the one reason behind this.

The reason behind is that limit reached 1000 default set in the chart
---------------------------------------------------------------------------------------

ADOC SV Maarg- Shopify Fulfillment Error Report : chinmay edited this dataset which is used in emaling flow.

Why we don't know

ADOCSVMaarg- Shopify Fulfilment Error History : There is a dataset which is working right and attached to right one chart

But Here is the cache that in Report the name is attached is

ADOC SV Maarg - Shopify Fulfilment Error History

3744 has to be run on the email but actually attached one is 3863 -> chinmay edited the connected dataset and limit in 3863 chart



-------------------------------------------------------------------------------------------

ADOC SV Maarg - Shopify Fulfilment Error History

ADOC SV Maarg- Shopify Fulfilment Error History
969f9b	2024-04-04 07:15:00 am	2024-04-04 07:15:01 am	00:00:00.00		
969f9b	2024-04-04 07:15:00 am	2024-04-04 07:15:01 am	00:00:00.03		Report Schedule execution failed when generating a csv.
969f9b	2024-04-04 07:15:00 am	2024-04-04 07:15:01 am	00:00:00.15		Notification sent with error
5a9574

1:15

adoc-internal-notifications@hotwax.co 

no it will not runned it

gmt-6

range limit 
replicated dub runnig
email space 
now removing moqui-dev email from the report 
Muskan user is inactive now this is the leading reason for that or not;right

and It was related to permission that mukan user doesn't have the permission to schedule the alerts.

and 2nd thing I have to check was when I make it inactive and it has permission then what happend to them.

must have both thing user must be active and has permission to schedule the all thing

Solution simple after work is finished report assigned to a report specific user or ADMIN


------------------------------------------------------------------------------------------
