## Superset-Solr-Issues

Here I got the error at the Time of running Query when I am using alises
json()["fields"]

1. Alises mandatored in case of fields otherwise it would not be working.
2. With top level table alises it would not be working. 

select productId as productID from `local-enterpriseSearch`


# There is problem with AS virtual_table

SELECT `productID` AS `productID`,
       brand AS brand,
       `carrierParty` AS `carrierParty`,
       `categoryHierarc` AS `categoryHierarc`,
       `City` AS `City`,
       `companyIDS` AS `companyIDS`
FROM
  (select productId as productID,
          brandName as brand,
          carrierPartyId as carrierParty,
          categoryHierarchy as categoryHierarc,
          city as City,
          companyIds as companyIDS
   from `local-enterpriseSearch`) AS virtual_table
WHERE `productID` IS NOT NULL
  AND `productID` IS NOT NULL
ORDER BY `productID` ASC
LIMIT 1000;

String urlPath ="/solr/"+request.getRequestURI().substring( request.getRequestURI().indexOf("/",1));
//        String urlPath =  request.getRequestURI().replaceFirst("/search","/solr");


"authorization":{
    "class":"solr.RuleBasedAuthorizationPlugin",
    "permissions":[{"name":"security-edit",
       "role":"admin"}],
    "user-role":{"hotwax":"admin"}
}
 

String regexPattern1 = "(?i)\\bfrom\\s+"+coreName+"\\b";
Pattern regexPattern = Pattern.compile(regexPattern1);
matcher = regexPattern.matcher(queryParam);


---------------------------------------------------------------------------------------------------------------------------------
## FEB 21 2024

1. Avi sir can we just change the default indexing style, or can we remove this support also. : its done
2. Test-cases running thing. so I can make it good
3. Reports work I can make oms PR with necceary changes: and Here a question came that CSRF is I have to make it enable or not I think I have to for security reasons it must be.
4. VUE shikhna hai.
5. SSO dekhna in superset tasks.
6. How to manage the changes in the tathya patch efficently.

1. Chart ki naming instance-host ke according kara and give it tag like:brokering,JobManager and further sub-classification

sm-uat:Brokering:mainPage, sm-uat:Brokering:lastpage

2. Through superset-permission we will give only instance-level reportPermission and then just search the generic report name if exists then send its data.

we have to manage different-different superset-user

With frontend api we can send the request frame like what report asked for.

Generic-Naming we would invent like BrokeringCountFacilityID
3.


1. Maintain Instance level user.
2. Provide permission for the chart that we want to utilize in apps.
3. Superset Reports/Charts should have some generic-nameing pattern like SMUAT-Brokering:FacilityOrderCount,SMUAT-JOBManager:JOBCount

4. Now from frontend hit oms-api featchTathyaReport, here it takes params `reportName` (contain requested report name like appname:reportPurposeName)

5. Oms has api which fullfills frontend apps request and send the data from superset chart
	- In api first featch all chart
	- Filter the chart with `reportName` param and out the {result:[]}
----------------------------------------------------------------------------------------------------------
Droools tickets

- https://app.clickup.com/t/85ztug4w4
- https://app.clickup.com/t/2dezr5g

----------------------------------------------------------------------------------------------------------
Queries - 12/17
DBMS -7/10
DataModel- 7/10

Independently runnig solr zookeeper
Logging Monitoring
TLS
Clustering
Capicity needded for perticular number of docs in solr
Soft-Commit and Hard-Commit.
High availability
matrix points


prometeus-statusD-exporter: can we have to use it alone or It needs StatusD server also.
StatusD-> check for installation
