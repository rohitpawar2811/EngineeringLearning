1. Iterated in a manageble entity configs.
2. Now Iterate on the files /dataset /database /chart /dashboard
3. I have to just record the UUID while traversing and replace the random uuid on top of that
4. and I have to append the Instance-name as prefix whome I had to replace.


Picker is empty for

def generate_id():
    return uuid.uuid4().hex[:8]
    
    def init_job(self, channel_id: str, user_id: Optional[int]) -> dict[str, Any]:
        job_id = str(uuid.uuid4())
        return build_job_metadata(
            channel_id, job_id, user_id, status=self.STATUS_PENDING
        )
        
        def shortid() -> str:
    return f"{uuid.uuid4()}"[-12:]
    
    
 self._connection_id = uuid.uuid4().hex
 
 def generate_id():
    return uuid.uuid4().hex[:8]

 slots

Here we have to check which way is used to generate the uuid while generating Dashboard.
 
 ----------------------------------------------------------------------------------------------
 
 Ran 1 Service Jobs starting 2024-03-20T06:07:14.358049-04:00[America/New_York] - active: 12, paused: 33; on this server using 1 of 12 job slots
--- 2024-03-20 06:07:14.396 [oquiScheduled-1] INFO           org.moqui.impl.service.ScheduledJobRunner []
 Running job send_ProducedBulkOperationSystemMessage_ShopifyBulkQuery run 236746 (last run 2024-03-20 06:02:14.358, schedule 2024-03-20T06:07-04:00[America/New_York])



--- 2024-03-20 06:07:14.389 [oquiScheduled-1] INFO           org.moqui.impl.service.ScheduledJobRunner []
 Not retrying job Order_Routing_Group_100153 after error, before 5 min retry minutes (error run at 2024-03-20T06:02:14.393-04:00[America/New_York])
 
 
 1. In dashabord -> dashboard_title and there is slice_name to which we have to replace
 dashboard_title: ' ADOC SV logInsights API Records'
 sliceName: ADOC SV Postal Address Update API Report : Here the hipens becomes gone why don't know.
 
 2. In charts slice_name: ADOC SV - Manual Slip API Report
 	slice_name: ADOC SV - Order To Invoice API Report
 
 3. In Dataset there is name like that
 table_name: ADOC SV - MANUAL SLIP API REPORT
 
 4. In Database Table there is name that is like this
 database_name: Adoc-sv-uat Oms Solr logInsights
sqlalchemy_uri: solr://adoc-sv-uat.hotwax.io:443/search/logInsights?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyTG9naW5JZCI6InRhdGh5YS5pbnRlZ3JhdGlvbiIsInB1cnBvc2UiOiJ0YXRoeWEgaW50ZWdyYXRpb24iLCJpc3N1ZWRCeSI6IktodXNoYWxpIER1YmUiLCJpc3MiOiJhZG9jLXN2LXVhdCIsImV4cCI6MTg2NDg4NDgyOCwiY2F0ZWdvcnkiOiJJTlRFR1JBVElPTiIsImlhdCI6MTcwNzIwNDgyOH0.nP1W8LcAvxhsTLwt1Z75Jc7wtFJaE5Bgn_oHFxJq4RJ6bqhgTscZjRHd_PuVvKa_QQhuv6hqF-EhNOJCxrDiug&use_ssl=true
cache_timeout: 10000



Shopify-Connectore related failure



# Pending task 1 :

# "datasourceUid":"b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5","model":{"datasource":{"type":"loki","uid":"b1fec0d3-9e02-4e4a-8635-1a6503ebd1c5"},"editorMode":"code","expr":"sum by(errorMessage) (count_over_time({job=\"sm-uat.hotwax.io\"}
# Extract logs of any instance using promtail and configure locally and then test moving datasourceId and then replacing loki uid 
# It will work or not

# Pending 2: 
# - If  There is multiple Rule-Group then we have used .group[0] we have to make these things dynamic. and we have to write logic to iterate on multiple-rule group

# Pending: In notification policy we have prefreablely do the work manually, we can only make PUT call which updates there whole policy which is already existing no way to add. 
# policy enside everything
 
 # improvements
# - I can remove the logs silent part as we are not able to detect if api failed then what happend.
# - Only one contact point inserted as we are also making instance-level templates.
# - Notification policy only allow PUT operation : we have to do it manually as it restricts that contact-point is must ,
#  and we can't add single policy we would update all,so if already 10 exists and
#  we try to add one throw put all gone just one will exists


1. Prepare the document for Best Practices to provisioning the import file
while explaining full flow realted to import export.

2. Check for the documents where we have writed about import/export there we have to check for the changes realted to it. 

3. Relace the template via it and try how can we do that.


feature within the application.

https://sushruthan.medium.com/grafana-smtp-configuration-gmail-a01854ae0469

1 hour whole testing
1 hour doc preparation max 

then MR stuff it just takes around 10-20 minute


1. For Whole Backup

/api/v1/provisioning/alert-rules/export	

Export all alert rules in provisioning file format.

2. Contact points	
GET 
/api/v1/provisioning/contact-points/export	

Export all contact points in provisioning file format.

3. Notification policy tree	
GET 
/api/v1/provisioning/policies/export	

Export the notification policy tree in provisioning file format.

4. We can export alert-group also and perticular-rule by id

GET /api/v1/provisioning/folder/:folderUid/rule-groups/:group/export	

Export an alert rule group in provisioning file format.



curl --location 'http://localhost:3000/api/v1/provisioning/alert-rules/export?download=true' \
--header 'Authorization: Basic YWRtaW46QHJvaGl0MTI=' \
--header 'Cookie: OFBiz.Visitor=21101'




https://grafana.com/docs/grafana/latest/alerting/set-up/provision-alerting-resources/export-alerting-resources/


https://grafana.com/docs/grafana/latest/alerting/set-up/provision-alerting-resources/http-api-provisioning/#edit-resources-in-the-grafana-ui


Only we can delete policies from here 

DELETE /api/v1/provisioning/policies


GET /api/v1/provisioning/folder/:folderUid/rule-groups/:group/export

GET /api/v1/provisioning/alert-rules/export

docs cheked
community : partially checked
Brut-force try the pass the data
manually check the code what type of data it wanted. 
anything else we can do no.



Added: document for findings related to provisioning grafan-templates by terraform




/api/ruler/grafana/api/v1/rules/folder-name







- Now I want the api


Ht5#nrohit



Edit resources in the Grafana UI
By default, you cannot edit API-provisioned alerting resources in Grafana. To enable editing these resources in the Grafana UI, add the X-Disable-Provenance header to the following requests in the API:

POST /api/v1/provisioning/alert-rules
PUT /api/v1/provisioning/folder/{FolderUID}/rule-groups/{Group} (calling this endpoint will change provenance for all alert rules within the alert group)
POST /api/v1/provisioning/contact-points
POST /api/v1/provisioning/mute-timings
PUT /api/v1/provisioning/policies
PUT /api/v1/provisioning/templates/{name}
To reset the notification policy tree to the default and unlock it for editing in the Grafana UI, use the DELETE /api/v1/provisioning/policies endpoint.


GET /api/v1/provisioning/folder/:folderUid/rule-groups/:group/export

Now I just have to extract the information from the json and use the api to post on the grafana-instance.



@Passwd2811

1. Which will featch the data from which there is 3 things alert, contact point, policy
2. For alert part my code is ready
3. for contact-point
4. for policy

I can talk to them about this.

{
    "name": "SMUSj",
    "type": "email",
    "settings": {
        "addresses": "rohit.pawar@hotwax.co;arvind.tomar@hotwaxsystems.com",
        "singleEmail": false
    },
    "disableResolveMessage": false,
    "provenance": "file"
}


{
    "apiVersion": 1,
    "contactPoints": [
        {
            "orgId": 1,
            "name": "SM-UAT Monitoring",
            receivers": [
                {
                    "uid": "ee81af31-fbe4-44c2-962d-b1738c598094",
                    "type": "email",
                    "settings": {
                        "addresses": "rohit.pawar@hotwax.co;arvind.tomar@hotwaxsystems.com;",
                        "singleEmail": false
                    },
                    "disableResolveMessage": true
                }
            ]
        }
    ]
}

iterate on the recievers and then


tree is buetifull

on cristmas moring find what santa left for us , and also we cooked sweet food, we collect food and money , potrey , It was good felling to share who has not much and my parents said christmas is the time of giving not recieving.

There are tiny bugs, my mother tried to get rid of them, they eat sunflowers , I sometime see robin and blue-dart, I usally watched as hard-workers work for the food.

We have so many tomatos in garden, My fav veg was tomatoo, wheats also grow in the garden , wheat chocks the good plants so we would not plant them.

Pat Store 

they have everything they would need, for cats they have food, 
bols there are some fish some of are gold and normal
In the cage there was some parraotes and when I wave they said hello

In the next cage they were 2 kitten, I remeber my first day of my school I would not let her hold my hand.

they all looked very good I felt very small.

played some games I even 
I like school i

Transportation

There many ways for doing that
Some places I would like to be a truck driver.
There was special meter in truck and by looking on it they charge us
horse tarnsportation rearly someone use it. generally now it was used for events and races.

world becomes smaller because of transportation but that was not it just it makes easy to travel.



some people not like to watch the shows instead they would prefer to real news papers and novels.
the people who leave, it can be very cold in the 


Canada is made up of diffrent athenic cultures and peoples, 
Food in canada 

I would also like food chinese and
I eat a lot 
fish

was past contxt some time shows that thing is died at current time
In canda there is a lot food to choose. 

They say the lion is king of the jungle 
there are monkey they are swinging in the branches of the tree.
we spoke to parrates and there were so much exautic animale there we saw slippery snakes. some snakes has bright skin.
they work carefull when working with snakes.

The museum was so much interesting, I don't how people wore 
so many things 

there were so many clothes 

wars I don't think wars is good we should have to remember who dies for us. there were some room setup where 
There werer mummies from the egypt 
The polies my mother always tolds me. what my mother told me 
Deal with people effectively 
some people needs to be arrested for to safe us

The dog was very smart 


beneath my feet
my heart begins pounded in my heart
I

-------------------------------------------------------------------------------------------------------
APR 18

1. Reason behind what we opt 
2. We are taking inputs from the script so that history would not be saved in the ssh thing, and other one would not be able to do so.
4.Response should have to come of failure :done
3.Multiple contact points testing. Other we would include multiple in git. : Just make a iteration enable in the script that's it

Restarting docker-container would not be good thing.
And terraform would be a bad enginnering practice.

Upgarde changes

/admin/luke
solr://adoc-sv-oms.hotwax.io:443/search/logInsights?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyTG9naW5JZCI6InRhdGh5YS5pbnRlZ3JhdGlvbiIsInB1cnBvc2UiOiJzb2xyIHJlcG9ydHMiLCJpc3N1ZWRCeSI6IktodXNoYWxpIER1YmUiLCJpc3MiOiJhZG9jLXN2LW9tcyIsImV4cCI6MTg2NzI0MzE2MCwiY2F0ZWdvcnkiOiJJTlRFR1JBVElPTiIsImlhdCI6MTcwOTU2MzE2MH0.yXOQ9vVKrEya18TtOax1EpdaHvlqH4jjM1mQUvjgVt8Mya4iT6r1A8RrS9XPIn5O4MIfqnUopaaF-FZ3lbF5pA&use_ssl=true

- Authorization disabled hai
- cluster shift hua
- other api working as is except the one \sql endpoint.

---------------------------------------------------------------------------------------------

Adoc-GT

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyTG9naW5JZCI6InRhdGh5YS5pbnRlZ3JhdGlvbiIsInB1cnBvc2UiOiJOQSIsImlzc3VlZEJ5IjoiZGVlcGFrIGRpeGl0IiwiaXNzIjoiYWRvYy1ndC1vbXMiLCJleHAiOjE4NzEwOTgwNTUsImNhdGVnb3J5IjoiSU5URUdSQVRJT04iLCJpYXQiOjE3MTM0MTgwNTV9.3JSoSDi7OGapiSM2agIONuoznAVfbfmGN0CXEyQWFyRvnyt8SDKvc5IEduyixtznuTifkr-mr5ulgD5nWd-wSQ





Error parsing and check it is parsing or not.









Testing Parts in superset what we leavraging currently

Project Idea:
1.
saml2sso : Enabled  
React: Totally Rest Enabled 
Solr : for fast searching lucene based, 
SpringBoot : Backend part will sorted here.

2. I can do write those backed microservice programme hit.

5k Kuhoo
20K pending: shubham and abhishek
10k pending for next month
10K mridul sir
-----------------
45k : to give
25k
Remaning would be 25K 

------------------------------------------------------------------------------------------

- I would always use the subject in first place and then over details which makes the framing quite difficult.

so that frameing I have to imporove

@rohit12


--------------------------------------------------------------------------------

### Points to Note

1. Contact points should contain only one recipient.
3. Multiple rule-group feature yet not provided, only 1 user gp is provided.
2. Notification policy should be manually updated. Although `processNotificationPolicies` is included, you can simply comment it out without affecting other aspects.
3. Promethus datasource support.


------------------------------------------------------------------------------------------------------------------------------------------
Aprail 24 2024

1. Each time you hit contact point if there is existing same contact point then a duplicate-receiver will be added.
: Solution first check in target and then if exists delete and re-configure if you wanted to.
Or Just Skip The process


2. Group already exits there in the same dir you just added extra one in template then what happend.

we do not though of these cases.


https://hc.stevemadden.com/webtools/control/main

https://hc.stevemadden.com/webtools/control/main


#    # Extract group inside folder_name and name
#    # folder_name="SM-PROD-MAIN"
#    local folder_name=$(jq -r '.groups[0].folder' input.json)
#    local rule_group_name=$(jq -r '.groups[0].name' input.json)
#    folder_name=$custom_folder


For eatch nifi-instance we have to configure a NO-DATA alert setup, where we have to check if there is no log came then throw error in the duration of past 3h.

before that 

3h
0 evalution period NoData 



5m evaluation thing we had setup currently.

1. No Data thing setup on the logs or grafan-uat.
2. Configure the template on the git.
3. and after that create a temprory branch/master branch for grafana-instance level from where we would maintain the PROD, we have to change from 
uat->prod
name from uat->prod
and the urls related to it.
from error name we have to change.
Annotation type
alert-type :error
Team
instance-url

notification policy and alert bind bow should be a generic one.

sum by(errorMessage) (count_over_time({job="nifi-uat.hotwax.io"} |~ `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} ERROR.*` | pattern `<_> <errorMessage> duration<_>` [5m]))

Note All kind of replacements we are going to do list out.
branch change.
 
- NO DATA I will take as pending task and done it after some time.
-
----------------------------------------------------------------------------------
Apr 25 2024


# Define variables
#https://grafana-oms.hotwax.io/alerting/list
 grafana_host="https://grafana-oms.hotwax.io:443"
 grafana_username="rohit.pawar"
 grafana_password="Ht5@nadmin"
 folder_path="adoc-sv-maarg-prod-templates"
 loki_datasource_uuid=
# custom_folder="Adoc-sv-prod-main"

## Define variables
# grafana_host="http://localhost:3000"
# grafana_username="admin"
# grafana_password="@rohit12"
# folder_path="adoc-sv-maarg-prod-templates"
# loki_datasource_uuid=
# custom_folder="Adoc-sv-prod-main"


#read -p "Enter the grafana_host : " grafana_host
#read -p "Enter the grafana_username : " grafana_username
#read -sp "Enter the grafana_password : " grafana_password
#read -p "Enter the folder_path to read templates : " folder_path
#read -p "Enter the loki_datasource_uuid Optional bydefault fetch default-loki UUID : " loki_datasource_uuid
#read -p "Enter the name of custom_folder which contains Rules by default pick from json: " custom_folder

----------------------------------------------------------------------------------------------------------------------
## Backup of logs.hotwax.co

count_over_time({job="sm-prod-main-10-0-3-14"} |= `Picker is empty for` [1h])


stevemadden@hotwax.co
sm-prod-logs-alert
--------------------------------------------------------------------------------------
sum by(errorMessage) (count_over_time({job="sm-nifi.hotwax.io"} |~ `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} ERROR.*` | pattern `<_> <errorMessage> duration<_>` [5m]))

Error Encountered while running workflows on SM Nifi instance.

https://sm-nifi.hotwax.io/nifi

sm-nifi-error-alert



moqui-dev@hotwax.co;sm-internal-notfications@hotwax.co;arvind.tomar@hotwaxsystems.com
nifi-prod-alert-sm
-------------------------------------------------------------------------

sm-prod-main-4-240 Transaction has timed out
count_over_time({job="sm-prod-main-10-0-4-240"} |= `Transaction has timed out` [1h])

--------------------------------------------------------------------------

Napita Prod 

nifi-prod-alert-napita

delivery@hotwax.co;moqui-dev@hotwax.co;arvind.tomar@hotwaxsystems.com

--------------------------------------------------------

Napita NoData Monitoring

rohit.pawar@hotwax.co

--------------------------------------------------------------------------------------------------------------------------------------------------------------

	
Caused by: com.mysql.cj.exceptions.CJCommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 23 common frames omitted
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:649)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.validateConnectionFactory(BasicDataSource.java:106)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:374)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.DriverConnectionFactory.createConnection(DriverConnectionFactory.java:52)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:197)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:246)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:456)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:836)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:64)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLError.createCommunicationsException(SQLError.java:174)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 20 common frames omitted
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:232)Caused by: java.sql.SQLException: unable to get a connection from pool of a PoolingDataSource containing an XAPool of resource transactional_DS with 5 connection(s) (5 still available) -failed-
	at bitronix.tm.resource.jdbc.PoolingDataSource.getConnection(PoolingDataSource.java:332)
	at org.moqui.impl.entity.EntityFacadeImpl.getConnection(EntityFacadeImpl.groovy:2051)
	at org.moqui.impl.entity.EntityFacadeImpl.getConnection(EntityFacadeImpl.groovy:2034)
	at org.moqui.impl.entity.EntityFacadeImpl.fastFindOneExtended(EntityFacadeImpl.groovy:1579)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.getConnection(BasicDataSource.java:731)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createDataSource(BasicDataSource.java:531)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:653)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: java.sql.SQLException: Cannot create PoolableConnectionFactory (Communications link failure
2024-05-02 10:02:15	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:15	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:15	
	at org.apache.nifi.processors.standard.AbstractExecuteSQL.onTrigger(AbstractExecuteSQL.java:257)
2024-05-02 10:02:15	
	at com.sun.proxy.$Proxy189.getConnection(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:105)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:254)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedMethodAccessor580.invoke(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.DBCPService.getConnection(DBCPService.java:55)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:222)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:245)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
org.apache.nifi.processor.exception.ProcessException: java.sql.SQLException: Cannot create PoolableConnectionFactory (Communications link failure
2024-05-02 10:02:15	
  AND oh.order_type_id = 'SALES_ORDER';]. No FlowFile to route to failure
2024-05-02 10:02:15	
  oh.status_id = 'ORDER_CREATED' 
2024-05-02 10:02:15	
WHERE 
2024-05-02 10:02:15	
  AND oisga.ship_group_seq_id = oisg.ship_group_seq_id 
2024-05-02 10:02:15	
  INNER JOIN order_item_ship_group oisg ON oisga.order_id = oisg.order_id 
2024-05-02 10:02:15	
  AND oi.order_item_seq_id = oisga.order_item_seq_id 
2024-05-02 10:02:15	
  INNER JOIN order_item_ship_group_assoc oisga ON oi.order_id = oisga.order_id 
2024-05-02 10:02:15	
  AND oi.product_id = '13436' 
2024-05-02 10:02:15	
  INNER JOIN order_item oi ON oh.order_id = oi.order_id 
2024-05-02 10:02:15	
  order_header oh 
2024-05-02 10:02:15	
FROM 
2024-05-02 10:02:15	
  oisg.ship_group_seq_id AS shipGroupSeqId 
2024-05-02 10:02:15	
  DISTINCT oi.order_id AS orderId, 
2024-05-02 10:02:15	
2024-05-02 04:22:16,312 ERROR [Timer-Driven Process Thread-5] o.a.n.p.standard.ExecuteSQLRecord ExecuteSQLRecord[id=dfe064c8-560f-3386-4572-3314a36508f1] Unable to execute SQL select query [SELECT 
2024-05-02 10:02:15	
	... 33 common frames omitted
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:65)
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.StandardSocketFactory.connect(StandardSocketFactory.java:155)
2024-05-02 10:02:15	
	at java.base/java.net.Socket.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.SocksSocketImpl.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.connectToAddress(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.doConnect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.PlainSocketImpl.socketConnect(Native Method)
2024-05-02 10:02:15	
Caused by: java.net.SocketException: Network is unreachable (connect failed)
2024-05-02 10:02:15	
	... 30 common frames omitted
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:826)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:956)
2024-05-02 10:02:15	
	at com.mysql.cj.NativeSession.connect(NativeSession.java:144)
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:91)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createCommunicationsException(ExceptionFactory.java:167)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:151)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:105)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:61)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Constructor.newInstance(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedConstructorAccessor338.newInstance(Unknown Source)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: com.mysql.cj.exceptions.CJCommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 23 common frames omitted
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:649)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.validateConnectionFactory(BasicDataSource.java:106)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:374)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.DriverConnectionFactory.createConnection(DriverConnectionFactory.java:52)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:197)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:246)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:456)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:836)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:64)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLError.createCommunicationsException(SQLError.java:174)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 20 common frames omitted
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:232)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.getConnection(BasicDataSource.java:731)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createDataSource(BasicDataSource.java:531)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:653)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: java.sql.SQLException: Cannot create PoolableConnectionFactory (Communications link failure
2024-05-02 10:02:15	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:15	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:15	
	at org.apache.nifi.processors.standard.AbstractExecuteSQL.onTrigger(AbstractExecuteSQL.java:257)
2024-05-02 10:02:15	
	at com.sun.proxy.$Proxy633.getConnection(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:105)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:254)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedMethodAccessor580.invoke(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.DBCPService.getConnection(DBCPService.java:55)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:222)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:245)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
org.apache.nifi.processor.exception.Proces



====================================================================================

		2024-05-02 10:02:15	
Caused by: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 20 common frames omitted
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:232)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.getConnection(BasicDataSource.java:731)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createDataSource(BasicDataSource.java:531)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:653)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: java.sql.SQLException: Cannot create PoolableConnectionFactory (Communications link failure
2024-05-02 10:02:15	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:15	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:15	
	at org.apache.nifi.processors.standard.AbstractExecuteSQL.onTrigger(AbstractExecuteSQL.java:257)
2024-05-02 10:02:15	
	at com.sun.proxy.$Proxy633.getConnection(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:105)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:254)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedMethodAccessor580.invoke(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.DBCPService.getConnection(DBCPService.java:55)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:222)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:245)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)

============================================================================================

	... 33 common frames omitted
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:65)
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.StandardSocketFactory.connect(StandardSocketFactory.java:155)
2024-05-02 10:02:15	
	at java.base/java.net.Socket.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.SocksSocketImpl.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.connect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.connectToAddress(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.AbstractPlainSocketImpl.doConnect(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.net.PlainSocketImpl.socketConnect(Native Method)
2024-05-02 10:02:15	
Caused by: java.net.SocketException: Network is unreachable (connect failed)
2024-05-02 10:02:15	
	... 30 common frames omitted
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:826)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:956)
2024-05-02 10:02:15	
	at com.mysql.cj.NativeSession.connect(NativeSession.java:144)
2024-05-02 10:02:15	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:91)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createCommunicationsException(ExceptionFactory.java:167)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:151)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:105)
2024-05-02 10:02:15	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:61)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Constructor.newInstance(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedConstructorAccessor338.newInstance(Unknown Source)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: com.mysql.cj.exceptions.CJCommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 23 common frames omitted
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:649)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.validateConnectionFactory(BasicDataSource.java:106)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:374)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.DriverConnectionFactory.createConnection(DriverConnectionFactory.java:52)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:197)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.getInstance(ConnectionImpl.java:246)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.<init>(ConnectionImpl.java:456)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:836)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:64)
2024-05-02 10:02:15	
	at com.mysql.cj.jdbc.exceptions.SQLError.createCommunicationsException(SQLError.java:174)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure
2024-05-02 10:02:15	
	... 20 common frames omitted
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:232)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.getConnection(BasicDataSource.java:731)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createDataSource(BasicDataSource.java:531)
2024-05-02 10:02:15	
	at org.apache.commons.dbcp2.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:653)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	
2024-05-02 10:02:15	
Caused by: java.sql.SQLException: Cannot create PoolableConnectionFactory (Communications link failure
2024-05-02 10:02:15	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:15	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:15	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:15	
	at org.apache.nifi.processors.standard.AbstractExecuteSQL.onTrigger(AbstractExecuteSQL.java:257)
2024-05-02 10:02:15	
	at com.sun.proxy.$Proxy633.getConnection(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:105)
2024-05-02 10:02:15	
	at org.apache.nifi.controller.service.StandardControllerServiceInvocationHandler.invoke(StandardControllerServiceInvocationHandler.java:254)
2024-05-02 10:02:15	
	at java.base/java.lang.reflect.Method.invoke(Unknown Source)
2024-05-02 10:02:15	
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(Unknown Source)
2024-05-02 10:02:15	
	at jdk.internal.reflect.GeneratedMethodAccessor580.invoke(Unknown Source)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.DBCPService.getConnection(DBCPService.java:55)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:222)
2024-05-02 10:02:15	
	at org.apache.nifi.dbcp.AbstractDBCPConnectionPool.getConnection(AbstractDBCPConnectionPool.java:245)
2024-05-02 10:02:15	
The last packet sent successfully to the server was 0 milliseconds ago. The driver has not received any packets from the server.)
2024-05-02 10:02:15	

============================================================================================

3	
org.apache.nifi.processors.standard.socket.ClientConnectException: SSH Client connection failed [ucg-uat.hotwax.io:235]
2024-05-02 10:02:13	
2024-05-02 04:10:00,014 ERROR [Timer-Driven Process Thread-10] o.a.nifi.processors.standard.ListSFTP ListSFTP[id=c387c627-6197-3a40-42f4-9deb9694a735] Processing failed
2024-05-02 10:02:13	
	... 19 common frames omitted
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ssh.StandardSSHClientProvider.getClient(StandardSSHClientProvider.java:113)
2024-05-02 10:02:13	
	at net.schmizz.sshj.SocketClient.connect(SocketClient.java:68)
2024-05-02 10:02:13	
	at java.base/java.net.Socket.connect(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.SocksSocketImpl.connect(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.AbstractPlainSocketImpl.connect(Unknown Source)
2024-05-02 10:02:13	
Caused by: java.net.UnknownHostException: ucg-oms.hotwax.io
2024-05-02 10:02:13	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:13	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.util.list.AbstractListProcessor.onTrigger(AbstractListProcessor.java:526)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.util.list.AbstractListProcessor.listByTrackingTimestamps(AbstractListProcessor.java:758)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListFileTransfer.performListing(ListFileTransfer.java:112)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListSFTP.performListing(ListSFTP.java:154)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListFileTransfer.performListing(ListFileTransfer.java:120)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getListing(SFTPTransfer.java:271)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getListing(SFTPTransfer.java:309)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getSFTPClient(SFTPTransfer.java:616)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ssh.StandardSSHClientProvider.getClient(StandardSSHClientProvider.java:116)
2024-05-02 10:02:13	
org.apache.nifi.processors.standard.socket.ClientConnectException: SSH Client connection failed [ucg-oms.hotwax.io:235]
2024-05-02 10:02:13	
2024-05-02 04:10:00,014 ERROR [Timer-Driven Process Thread-5] o.a.nifi.processors.standard.ListSFTP ListSFTP[id=b2e2b8ff-bad3-3bcc-e410-23666f8141fd] Processing failed
2024-05-02 10:02:13	
	... 19 common frames omitted
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ssh.StandardSSHClientProvider.getClient(StandardSSHClientProvider.java:113)
2024-05-02 10:02:13	
	at net.schmizz.sshj.SocketClient.connect(SocketClient.java:68)
2024-05-02 10:02:13	
	at java.base/java.net.Socket.connect(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.SocksSocketImpl.connect(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.AbstractPlainSocketImpl.connect(Unknown Source)
2024-05-02 10:02:13	
Caused by: java.net.UnknownHostException: ucg-oms.hotwax.io
2024-05-02 10:02:13	
	at java.base/java.lang.Thread.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.FutureTask.run(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.util.concurrent.Executors$RunnableAdapter.call(Unknown Source)
2024-05-02 10:02:13	
	at org.apache.nifi.engine.FlowEngine$2.run(FlowEngine.java:110)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.scheduling.QuartzSchedulingAgent$2.run(QuartzSchedulingAgent.java:130)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.tasks.ConnectableTask.invoke(ConnectableTask.java:247)
2024-05-02 10:02:13	
	at org.apache.nifi.controller.StandardProcessorNode.onTrigger(StandardProcessorNode.java:1361)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.AbstractProcessor.onTrigger(AbstractProcessor.java:27)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.util.list.AbstractListProcessor.onTrigger(AbstractListProcessor.java:526)
2024-05-02 10:02:13	
	at org.apache.nifi.processor.util.list.AbstractListProcessor.listByTrackingTimestamps(AbstractListProcessor.java:758)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListFileTransfer.performListing(ListFileTransfer.java:112)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListSFTP.performListing(ListSFTP.java:154)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ListFileTransfer.performListing(ListFileTransfer.java:120)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getListing(SFTPTransfer.java:271)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getListing(SFTPTransfer.java:309)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.util.SFTPTransfer.getSFTPClient(SFTPTransfer.java:616)
2024-05-02 10:02:13	
	at org.apache.nifi.processors.standard.ssh.StandardSSHClientProvider.getClient(StandardSSHClientProvider.java:116)
2024-05-02 10:02:13	
org.apache.nifi.processors.standard.socket.ClientConnectException: SSH Client connection failed [ucg-oms.hotwax.io:235]
2024-05-02 10:02:13	
2024-05-02 04:10:00,013 ERROR [Timer-Driven Process Thread-4] o.a.nifi.processors.standard.ListSFTP ListSFTP[id=dbd5242b-363d-1e83-3eb9-03f6658ffbfa] Processing failed
2024-05-02 10:02:13	
	... 34 common frames omitted
2024-05-02 10:02:13	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:65)
2024-05-02 10:02:13	
	at com.mysql.cj.protocol.StandardSocketFactory.connect(StandardSocketFactory.java:132)
2024-05-02 10:02:13	
	at java.base/java.net.InetAddress.getAllByName(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.InetAddress.getAllByName(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.InetAddress.getAllByName0(Unknown Source)
2024-05-02 10:02:13	
	at java.base/java.net.InetAddress$CachedAddresses.get(Unknown Source)
2024-05-02 10:02:13	
Caused by: java.net.UnknownHostException: ucg-oms-prod.cyps810k3u3o.us-east-1.rds.amazonaws.com
2024-05-02 10:02:13	
	... 31 common frames omitted
2024-05-02 10:02:13	
	at com.mysql.cj.jdbc.ConnectionImpl.createNewIO(ConnectionImpl.java:826)
2024-05-02 10:02:13	
	at com.mysql.cj.jdbc.ConnectionImpl.connectOneTryOnly(ConnectionImpl.java:956)
2024-05-02 10:02:13	
	at com.mysql.cj.NativeSession.connect(NativeSession.java:144)
2024-05-02 10:02:13	
	at com.mysql.cj.protocol.a.NativeSocketConnection.connect(NativeSocketConnection.java:91)
2024-05-02 10:02:13	
	at com.mysql.cj.exceptions.ExceptionFactory.createCommunicationsException(ExceptionFactory.java:167)
2024-05-02 10:02:13	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:151)
2024-05-02 10:02:13	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:105)
2024-05-02 10:02:13	
	at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:61)
2024-05-02 10:02:13	
	at java.base/java.lang.reflect.Constructor.newInstance(Unknown Source)
2024-05-02 10:02:13	
	at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(Unknown Source)
2024-05-02 10:02:13	
	at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance(Unknown Source)
2024-05-02 10:02:13	
	at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)

=============================================================================================

branch latest 

1. Okay
2. contact-point email copuping
3. NoData 1 hour and commit in  repo.



{instance="napita.hotwax.io"}

{instance="tathya.hotwax.io"} 



    @classmethod
    def execute_with_cursor(
            cls, cursor: Any, sql: str, query: Query, session: Session
    ) -> None:
        """
        Trigger execution of a query and handle the resulting cursor.

        For most implementations this just makes calls to `execute` and
        `handle_cursor` consecutively, but in some engines (e.g. Trino) we may
        need to handle client limitations such as lack of async support and
        perform a more complicated operation to get information from the cursor
        in a timely manner and facilitate operations such as query stop
        """
        print("=============Query in base 2engine spec=")
        print(query)
        print(cls)
        logger.debug("Query %d: Running query: %s", query.id, sql)
        cls.execute(cursor, sql, async_=True)
        logger.debug("Query %d: Handling cursor", query.id)
        cls.handle_cursor(cursor, query, session)
        
        
    # An owner of the model. If the last modifier is in the owners list, returns that
    # user. If the modifier is not found, returns the creator if found in the owners
    # list. Finally, if neither are present, returns the first user in the owners list.
    OWNER = "owner"
    
    
    
    Caused by: java.sql.SQLException: unable to get a connection from pool of a PoolingDataSource containing an XAPool of resource transactional_DS with 5 connection(s) (5 still available) -failed-
	at bitronix.tm.resource.jdbc.PoolingDataSource.getConnection(PoolingDataSource.java:332)
	at org.moqui.impl.entity.EntityFacadeImpl.getConnection(EntityFacadeImpl.groovy:2051)
	at org.moqui.impl.entity.EntityFacadeImpl.getConnection(EntityFacadeImpl.groovy:2034)
	at org.moqui.impl.entity.EntityFacadeImpl.fastFindOneExtended(EntityFacadeImpl.groovy:1579)
	
	
	 IOException occurred when talking to server at: https://search.hotwax.io:8983/solr/adoc-sv-oms-enterpriseSearch
	 
	  |W| In getSetRollbackOnlyCause no stack placeholder was in place, here is the current location: 



2024-05-10 15:13:19.554	
2024-05-10 03:43:18,738 |0.0.0.0-8009-exec-10 |GroovyBaseScript              |E| Search server returned error : null
2024-05-10 15:13:19.554	
2024-05-10 03:43:18,737 |0.0.0.0-8009-exec-10 |SolrQuery                     |E| Connect to search.hotwax.io:8983 [search.hotwax.io/54.85.235.246] failed: Connection timed out (Connection timed out)
2024-05-10 15:13:14.544	
2024-05-10 03:43:14,171 |Catalina-utility-2   |ControlEventListener          |I| Destroying session:  hidden sessionId by default.
    


2024-05-10 15:39:08.167	
2024-05-10 04:09:07,664 |Catalina-utility-1   |ControlEventListener          |I| Could not find visit value object in session [ hidden sessionId by default.] that is being destroyed
2024-05-10 15:39:03.156	
2024-05-10 04:09:02,165 |0.0.0.0-8009-exec-22 |GroovyBaseScript              |E| IOException occurred when talking to server at: https://search.hotwax.io:8983/solr/adoc-gt-oms-enterpriseSearch



2024-01-14 13:30:49,942 |jsse-nio-8443-exec-2 |GroovyBaseScript              |E| IOException occurred when talking to server at: https://search-uat.hotwax.io:8983/solr/krewe-uat-enterpriseSearch
2024-01-14 13:31:05,364 |jsse-nio-8443-exec-2 |GroovyBaseScript              |E| IOException occurred when talking to server at: https://search-uat.hotwax.io:8983/solr/krewe-uat-enterpriseSearch
2024-01-14 13:33:15,020 |jsse-nio-8443-exec-2 |SolrQuery                     |E| Connect to search-uat.hotwax.io:8983 [search-uat.hotwax.io/172.20.20.6] failed: Connection timed out (Connection timed out)
2024-01-14 13:33:15,023 |jsse-nio-8443-exec-2 |GroovyBaseScript              |E| Search server returned error : null

"Fix: patched file in tathya-uat, missing import statements."
------------------------------------------------------------------------

Building jar: /home/rohit/Downloads/springboot/springboot/target/springboot-0.0.1-SNAPSHOT.jar

PCI report

PCI test  that pass. 
PCI complaint pass and we again enable the ssh for product import.

Order document api transaction. brium not commited and make changes it counts as transaction. editing more once the document comes in out system alawara.


Semaphore one error



    |I| Job  [Import Approve Sales Order] Id [964811] -- Next runtime: Fri May 10 04:10:00 CST 2024
2024-05-10 15:35:00.703	
2024-05-10 04:05:00,672 |OFBiz-JobQueue-13    |TransactionUtil               |I| Transaction rolled back
2024-05-10 15:35:00.703	
2024-05-10 04:05:00,671 |OFBiz-JobQueue-13    |ServiceSemaphore              |E| Cannot obtain unique transaction for semaphore logging
2024-05-10 15:35:00.703	
2024-05-10 04:05:00,671 |OFBiz-JobQueue-13    |TransactionUtil               |I| Transaction rollback only not set, rollback only is already set.
2024-05-10 15:35:00.703	
2024-05-10 04:05:00,671 |OFBiz-JobQueue-13    |GenericDelegator              |E| Failure in create operation for entity [ServiceSemaphore]: org.apache.ofbiz.entity.GenericEntityException: Error while inserting: [GenericEntity:ServiceSemaphore][createdStamp,2024-05-10 04:05:00.667(java.sql.Timestamp)][createdTxStamp,2024-05-10 04:05:00.667(java.sql.Timestamp)][lastUpdatedStamp,2024-05-10 04:05:00.667(java.sql.Timestamp)][lastUpdatedTxStamp,2024-05-10 04:05:00.667(java.sql.Timestamp)][lockThread,OFBiz-JobQueue-13(java.lang.String)][lockTime,2024-05-10 04:05:00.65(java.sql.Timestamp)][lockedByInstanceId,ofbiz1(java.lang.String)][serviceName,processPendingDataManagerJob(java.lang.String)] (SQL Exception while executing the following:INSERT INTO SERVICE_SEMAPHORE (SERVICE_NAME, LOCKED_BY_INSTANCE_ID, LOCK_THREAD, LOCK_TIME, LAST_UPDATED_STAMP, LAST_UPDATED_TX_STAMP, CREATED_STAMP, CREATED_TX_STAMP) VALUES (?, ?, ?, ?, ?, ?, ?, ?) (Duplicate entry 'processPendingDataManagerJob' for key 'service_semaphore.PRIMARY')). Rolling back transaction.
2024-05-10 15:35:00.703	
	at java.lang.Thread.run(Thread.java:750) ~[?:1.8.0_362]
2024-05-10 15:35:00.703	
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) ~[?:1.8.0_362]
2024-05-10 15:35:00.703	
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) ~[?:1.8.0_362]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.job.AbstractJob.run(AbstractJob.java:87) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.job.GenericServiceJob.exec(GenericServiceJob.java:70) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.GenericDispatcherFactory$GenericDispatcher.runSync(GenericDispatcherFactory.java:88) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.ServiceDispatcher.runSync(ServiceDispatcher.java:232) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.ServiceDispatcher.runSync(ServiceDispatcher.java:276) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.semaphore.ServiceSemaphore.acquire(ServiceSemaphore.java:70) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.semaphore.ServiceSemaphore.checkLockNeedToWait(ServiceSemaphore.java:137) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.service.semaphore.ServiceSemaphore.dbWrite(ServiceSemaphore.java:172) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.GenericValue.create(GenericValue.java:76) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.GenericDelegator.create(GenericDelegator.java:879) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.datasource.GenericHelperDAO.create(GenericHelperDAO.java:65) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.datasource.GenericDAO.insert(GenericDAO.java:112) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.jdbc.SQLProcessor.rollback(SQLProcessor.java:185) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
	at org.apache.ofbiz.entity.transaction.TransactionUtil.setRollbackOnly(TransactionUtil.java:359) ~[ofbiz.jar:?]
2024-05-10 15:35:00.703	
java.lang.Exception: rollback called in Entity Engine SQLProcessor

---------------------------------------------------------------------------------------------------------------------------------
MessageSource spring object we have used and defined the properties we wanted to convert based the user language.

message.properties 
Here we defined properties for default lanuguage 
And then defined other lanuguage properties\
message_nl.properties

and on client-side you just have set header lanugage and set to nl-> the response come according its propertie file.
Accept-language=nl

MessageSource is class defined by spring to access the message.properties 



Task completions today
1

2 High priority wa


   `systemInfo.serverTimezone`,
       `systemInfo.serverTimezone` AS `systemInfo.serverTimezone`,


https://buypartsnow.auth0.com/login?state=hKFo2SBVdVgyQTBSWmR1SDJXX2VsSWxuUHFiVXdtcGNUcjRZbaFupWxvZ2luo3RpZNkgTGNGY0lRY2txc01qU2lRbFVtSVFEdE1GdEdzSjFyaUmjY2lk2SBNYTZPUDlTN0RtWXFreEFEdFFrSGUxQjlrd1pqTnI3ag&client=Ma6OP9S7DmYqkxADtQkHe1B9kwZjNr7j&
protocol=oauth2&
response_type=code&
redirect_uri=https%3A%2F%2Fstaging.buyautopartsnow.com%2Fcommerce%2Fcontrol%2Fmain


https://staging.buyautopartsnow.com/commerce/control/main?code=oE3P64LAtGeCaicPXXYlu-aCcP-ooiTKgTEHhU-ip59dF

https://buypartsnow.auth0.com/v1/token

https://buypartsnow.auth0.com/oauth2/v1/token


https://buypartsnow.auth0.com/oauth2/v1/authorize?
   client_id=Ma6OP9S7DmYqkxADtQkHe1B9kwZjNr7j&
   response_type=code&scope=openid&
   redirect_uri=https://staging.buyautopartsnow.com/commerce/control/main&
   code_challenge_method=S256&
   code_challenge=qjrzSW9gMiUgpUvqgEPE4_-8swvyCtfOVvg55o5S_es
   
curl --request POST \
  --url https://buypartsnow.auth0.com/oauth2/v1/token \
  --header 'accept: application/json' \
  --header 'cache-control: no-cache' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=authorization_code&client_id=Ma6OP9S7DmYqkxADtQkHe1B9kwZjNr7j&redirect_uri=yourApp%3A%2Fcallback&code=BLh7k1G87BCxbqgcppdr87rvi_xm-7HV-Wf96l1TfZ1o0'
  
  
  &code_verifier=M25iVXpKU3puUjFaYWg3T1NDTDQtcW1ROUY5YXlwalNoc0hhakxifmZHag'
   



   https://buypartsnow.auth0.com/authorize?response_type=code&client_id=Ma6OP9S7DmYqkxADtQkHe1B9kwZjNr7j&redirect_uri=https://staging.buyautopartsnow.com/commerce/control/main


code=BLh7k1G87BCxbqgcppdr87rvi_xm-7HV-Wf96l1TfZ1o0


disable grouping in notification policy if not enabled if your 


1. You can get some information that where we got info that alert sent or not.
2. And find where it is blocked on smtp side or something else.
3. Or its all about group fault but currently only one alert is present inside the group.
4. There is large number of count in the log, That might cause this issue

- Logs check and replicate the situation on the uat.
- I am not able to saw mail-sending emails in the grafana instances.
- I should have to check for the lokie or external service for checking the email issue.
- No external services are there, It might be thing that for all services of grafana we have not enable logging.

- Grouping is an important feature of Grafana Alerting as it allows you to batch relevant alerts together into a smaller number of notifications.

5m
4h

Todo: We need to update the documentaion for grafan-alert setup 


https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/
https://grafana.com/docs/grafana/latest/alerting/fundamentals/notifications/notification-policies/
https://community.grafana.com/t/including-full-log-error-message-in-alert-notification-using-loki/87113/4

XAER_RMERR: Fatal error occurred in the transaction branch
XAER_RMERR: Fatal error occurred in the transaction branch



sadhana.deshmukh@hotwax.co;yamini.bhagat@hotwaxsystems.com;bhavna.gawhade@hotwaxsystems.com;janvi.talreja@hotwax.co;nidhi.pal@hotwax.co

Rohit 

PutSFTP, FeachSFTP, LISTSFTP




{errorMessage="09:28:14,837 ERROR [Timer-Driven Process Thread-7] o.a.n.c.s.StandardControllerServiceNode StandardControllerServiceNode[service=CSVRecordSetWriter[id=7ab17b9b-a8ed-3990-5cd6-ad1212824244], name=CSVRecordSetWriter For Adding Headers, active=true] Encountering difficulty enabling. (Validation State is INVALID: ['Schema Text' is invalid because Property references Parameter 'avro.schema' but the currently selected Parameter Context does not have a Parameter with that name]). Will continue trying to enable."}

---------------------------------------------------------------------------------------------------------------------------------------

Facilty type
Facility Group
Fulfillment group

Brokering
warehouse
Physicalstore

preorder
backorder
Bopis Rejected
------------------------------------------------------------------------------------
Sync order from shopify to oms
-job
-file

as Shipping we would accept the inventory 
oms get and then we send to shopify

-----------------------------------------
## JUN 4
Hello, this is Rohit Pawar. It's good to connect with you.

Ht5@nrohit


REs


878585

ETL 3 flows we have to create

- Create Tenante API-> create db , table , user
- ETL tenate wise 
- Tenate wise db 

I have to create tennate-wise

API hit would doing this task.
1. which create table.
2. multi-tenante way to build up flow which reads the data from the tenate db and process here.
3. process part : I have to create the connections and auto create the table .


Requesting Mysql setup for data-warehousing

sum by(errorMessage) (count_over_time({instance="adoc-sv-oms-hotwax-io"} |~ `Caused by: java\.lang\.NullPointerException(?:\n\s+.*)*` !~ `\|\s*I\s*\|` | pattern `<_> <errorMessage> duration<_>` [5m]))
----------------------------------------------------------------------------------------------
I am messing with HR rounds, and not able to go in next round.
Always create hesitation, please anser questions clearly by properly thinking and smartly.


- I have to write a block of code which stops full process group and then sets the param.

1. Blocks parallel execution,not scallable clients wait for other.
2. Because jo exection context start hota hai prame start-stop karna it is an afford

-------------------------------------------------------------------------------------------------------


 --->Run the below query to remove job WITH Name Import customers from Shopify


SELECT *
FROM job_sandbox
WHERE 
    system_job_enum_id = 'JOB_IMP_CSTMR'
    AND status_id IN ('SERVICE_DRAFT','SERVICE_PENDING');



update job_sandbox set status_id="SERVICE_CANCELLED", cancel_date_time =NOW(), run_by_instance_id="ofbiz1" 
WHERE 
    system_job_enum_id = 'JOB_IMP_CSTMR'
    AND status_id In ('SERVICE_DRAFT', 'SERVICE_PENDING');


select * from Facility where postal_code is null;

SELECT *
FROM Facility_Contact_Detail_By_Purpose AS fcdp
INNER JOIN Facility AS f ON fcdp.FACILITY_ID = f.FACILITY_ID
WHERE f.postal_code IS NULL;


SELECT facility
FROM facility AS f
NATURAL JOIN facility_contact_mech AS fcm
INNER JOIN postal_address AS pa ON pa.contact_mech_id = fcm.contact_mech_id;

Software Engineer 2 - 53401 - 53401


git commit -m "Fix: Type mismatch in lat and long columns in Geo_Point entity."




2024-06-17 11:39:49,394 |.0.0.0-8009-exec-276 |RequestHandler                |E| Request createOrderAttribute caused an error with the following message: Value found (with ids ADOC20418::customerId), cannot create a new one

2024-06-17 11:39:49,391 |.0.0.0-8009-exec-276 |ServiceDispatcher             |E| Error in Service [createOrderAttribute]: Value found (with ids ADOC20418::customerId), cannot create a new one


updateShippingAddressOfRerouteOrder

    <request-map uri="updateOrderItemShipToAddress">
        <security auth="true" https="true"/>
        <event type="service" invoke="updateOrderItemShipToAddress"/>
        <response name="success" type="request" value="json"/>
        <response name="error" type="request" value="json"/>
    </request-map>	
    
Expedited orders and standard orders .

    
Uneccearly we are logging errors know one is tracking them not usefull for users/client.



Debug.logError("Incomplete order Phone details", MODULE);

 - Implemented kafka-client in app side. 
 - Converting batch job based PL/SQL application to real time event driven application using Apache Kafka.
 - Reduced Kafka Lag by increasing partitions, consumer groups.