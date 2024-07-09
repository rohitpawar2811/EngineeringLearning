Refrence Link

https://solr.apache.org/guide/6_6/collections-api.html
https://solr.apache.org/guide/8_9/configsets-api.html
https://solr.apache.org/guide/8_5/config-sets.html#:~:text=When%20you%20create%20a%20collection,via%20bin%2Fsolr%20zk%20upconfig%20.
https://factorpad.com/tech/solr/reference/solr-create-collection.html
https://solr.apache.org/guide/8_2/cluster-node-management.html

-------------------------------------------------------------------------------------------------------
For Creating the collection

/admin/collections?action=CREATE&name=name&numShards=number&replicationFactor=number&maxShardsPerNode=number&createNodeSet=nodelist&collection.configName=configname

http://localhost:8983/solr/admin/collections?action=CREATE&name=demo&numShards=&replicationFactor=1&collection.configName=ofbiz_configs/enterpriseSearch

--------------------------------------------------------------------------------------------------

For Getting the status of collection

http://localhost:8983/solr/admin/collections?action=CLUSTERSTATUS

-----------------------------------------------------------------------------------------------------

exception": {
        "msg": "Can not find the specified config set: enterpriseSearch",
        "rspCode": 400
    },
    
Not able to find
http://localhost:8983/solr/admin/collections?action=CREATE&name=demo&numShards=1&replicationFactor=1&collection.configName=ofbiz_configs/enterpriseSearch    

--------------------------------------------------------------------------------------------------------

{
    "responseHeader": {
        "status": 0,
        "QTime": 3749
    },
    "success": {
        "127.0.1.1:8983_solr": {
            "responseHeader": {
                "status": 0,
                "QTime": 3204
            },
            "core": "demo_shard1_replica_n1"
        }
    },
    "warning": "Using _default configset. Data driven schema functionality is enabled by default, which is NOT RECOMMENDED for production use. To turn it off: curl http://{host:port}/solr/demo/config -d '{\"set-user-property\": {\"update.autoCreateFields\":\"false\"}}'"
}

----------------------------------------------------------------------------------------------------------

bin/solr create [-c name] [-d confdir] [-n configName] [-shards or -s #]
                      [-replicationFactor or -rf #] [-p port]
                      
./bin/solr create -c demo2 -d ofbiz_configs/enterpriseSearch -n enterpriseSearch  -s 1 -r 1 -p 8983                  

----------------------------------------------------------------------------------------------------------

CurlCommand for uploading config set in solr

 curl -X POST --header "Content-Type:application/octet-stream" --data-binary @myconfigset.zip "http://localhost:8983/solr/admin/configs?action=UPLOAD&name=myConfigSet"
 
 curl -X POST --header "Content-Type:application/octet-stream" --data-binary @myconfigset.zip "http://localhost:8983/solr/admin/configs?action=UPLOAD&name=myConfigSet

curl -X POST --header "Content-Type:application/octet-stream" --data-binary @ofbiz_configs.zip "http://localhost:8983/solr/admin/configs?action=UPLOAD&name=enterpriseSearch

---------------------------------------------------------------------------------------------------------
/bin/solr create -c demo4 -d ofbiz_configs/enterpriseSearch -n enterprisesearch -s 1 -p 8983

curl -X POST --header "Content-Type: application/octet-stream" --data-binary @ofbiz_configs.zip "http://localhost:8983/solr/admin/configs?action=UPLOAD&name=enterpriseSearch"
{
  "responseHeader":{
    "status":400,
    "QTime":6},
  "error":{
    "metadata":[
      "error-class","org.apache.solr.common.SolrException",
      "root-error-class","org.apache.solr.common.SolrException"],
    "msg":"The configuration enterpriseSearch already exists in zookeeper",
    "code":400}}


zip -r archive_name.zip folder_to_zip

## conf folder not included in the zip  

$ (cd solr/server/solr/configsets/sample_techproducts_configs/conf && zip -r - *) > myconfigset.zip

$ curl -X POST --header "Content-Type:application/octet-stream" --data-binary @myconfigset.zip "http://localhost:8983/solr/admin/configs?action=UPLOAD&name=myConfigSet"


----------------------------------------------------------------------------------------------------------
The Reason for core not created with uploaded config set

The configset for this collection was uploaded without any authentication in place, and use of <lib> is not available for collections with untrusted configsets. To use this component, re-upload the configset after enabling authentication and authorization."


{
    "responseHeader": {
        "status": 400,
        "QTime": 609
    },
    "failure": {
        "127.0.1.1:8983_solr": "org.apache.solr.client.solrj.impl.HttpSolrClient$RemoteSolrException:Error from server at http://127.0.1.1:8983/solr: Error CREATEing SolrCore 'demo31_shard1_replica_n1': Unable to create core [demo31_shard1_replica_n1] Caused by: The configset for this collection was uploaded without any authentication in place, and use of <lib> is not available for collections with untrusted configsets. To use this component, re-upload the configset after enabling authentication and authorization."
    },
    "Operation create caused exception:": "org.apache.solr.common.SolrException:org.apache.solr.common.SolrException: Underlying core creation failed while creating collection: demo31",
    "exception": {
        "msg": "Underlying core creation failed while creating collection: demo31",
        "rspCode": 400
    },
    "error": {
        "metadata": [
            "error-class",
            "org.apache.solr.common.SolrException",
            "root-error-class",
            "org.apache.solr.common.SolrException"
        ],
        "msg": "Underlying core creation failed while creating collection: demo31",
        "code": 400
    }
}
----------------------------------------------------------------------------------------------------------------------
Enabling Security in Solr =>

# Runs solr in java security manager sandbox. This can protect against some attacks.
# Runtime properties are passed to the security policy file (server/etc/security.policy)
# You can also tweak via standard JDK files such as ~/.java.policy, see https://s.apache.org/java8policy
# This is experimental! It may not work at all with Hadoop/HDFS features.
SOLR_SECURITY_MANAGER_ENABLED=true

Shared Secret Key
Header
Payload
JWT token

1. SSK: openssl rand -base64 32

Ej8/uIjfapOjLComyXktQbnnGcZugwGMDSwlRIkPJEE=

2. Header:

{
  "alg": "HS256",  # Algorithm used for the signature
  "typ": "JWT"     # Type of the token
}

3. Payload:

{
  "sub": "admin",   # Subject (the user)
  "exp": 1634524799, # Expiration time (Unix timestamp)
  "iss": "solr"     # Issuer
}

{
  "sub": "admin",
  "exp": 1634524799,
  "iss": "solr"
}


JWT token generated: https://jwt.io/#debugger-io?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTYzNDUyNDc5OSwiaXNzIjoic29sciJ9.UfAfHFHUdmrxu__b1DiTW9gjv1K-ZfQi_2kos5_Djp8 


you will need to upload a security.json file to ZooKeeper. The following command writes the file as it uploads it - you could also upload a file that you have already created locally.

  
server/scripts/cloud-scripts/zkcli.sh -cmd put /security.json 'path/file'
 
 Worked
 server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:9983 -cmd put /security.json '{
  "authentication": {
    "class": "solr.JWTAuthPlugin",
    "blockUnknown": true,
    "jwk": {
      "kty": "oct",
      "use": "sig",
      "kid": "k1",
      "k": "Ej8/uIjfapOjLComyXktQbnnGcZugwGMDSwlRIkPJEE=",
      "alg": "HS256"
    },
    "wellKnownUrl": "https://login.microsoftonline.com/d7cd718c-5c18-4f3c-8e4a-2c83274ae9b0/v2.0/.well-known/openid-configuration",
    "clientId": "f18fdd93-422e-4461-99bc-9aa0ce54012b",
    "redirectUri": "http://localhost:8983/solr"
  }
}'

    
      "wellKnownUrl": "https://login.microsoftonline.com/d7cd718c-5c18-4f3c-8e4a-2c83274ae9b0/v2.0/.well-known/openid-configuration",
      "scope": "solr:read solr:write",
      "clientId": "f18fdd93-422e-4461-99bc-9aa0ce54012b",
      "redirectUri": "http://localhost:8983/solr"

Valid one
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6OTk5OTk5OTk5OTksImlzcyI6InNvbHIifQ.foaXiHvhBaC9arib9x0ELzUPPk55smo-Gwr5wo-QXxY'

---------------------------------------------------------------------

Open ID plugin

https://login.microsoftonline.com/d7cd718c-5c18-4f3c-8e4a-2c83274ae9b0/v2.0/.well-known/openid-configuration

New One 

https://login.microsoftonline.com/d7cd718c-5c18-4f3c-8e4a-2c83274ae9b0/v2.0/.well-known/openid-configuration



curl http://localhost:8983/solr/admin/authentication -H 'Content-type:application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6OTk5OTk5OTk5OTksImlzcyI6InNvbHIifQ.foaXiHvhBaC9arib9x0ELzUPPk55smo-Gwr5wo-QXxY' -d '{"set-property": {"wellKnownUrl": "https://login.microsoftonline.com/d7cd718c-5c18-4f3c-8e4a-2c83274ae9b0/v2.0/.well-known/openid-configuration","scope": "solr:read solr:write"}}'


curl http://localhost:8983/solr/admin/authentication -H 'Content-type:application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6OTk5OTk5OTk5OTksImlzcyI6InNvbHIifQ.foaXiHvhBaC9arib9x0ELzUPPk55smo-Gwr5wo-QXxY' -d '{"set-property": {"clientId": "f18fdd93-422e-4461-99bc-9aa0ce54012b","scope": "solr:read solr:write"}}'

curl http://localhost:8983/solr/admin/authentication -H 'Content-type: application/json' -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6OTk5OTk5OTk5OTksImlzcyI6InNvbHIifQ.foaXiHvhBaC9arib9x0ELzUPPk55smo-Gwr5wo-QXxY' -d '{"set-property": {"clientId": "f18fdd93-422e-4461-99bc-9aa0ce54012b"}}'
-------------------------------------------------------------------------------------------------

"Cannot create collection demo34. Value of maxShardsPerNode is 1, and the number of nodes currently live or live and part of your createNodeSet is 1. This allows a maximum of 1 to be created. Value of numShards is 2, value of nrtReplicas is 1, value of tlogReplicas is 0 and value of pullReplicas is 0. This requires 2 shards to be created (higher than the allowed number)",


---------------------------------------------------------------------------





        Boolean deleteIndex = (Boolean) context.get("deleteIndex");
        Boolean deleteDataDir = (Boolean) context.get("deleteDataDir");
        Boolean deleteInstanceDir = (Boolean) context.get("deleteInstanceDir");
        
        
        No need optionals
        
------------------------------------------------------------------------------

HttpSolrClient Client mai header add nahi hota hai it will just execute()


        
        TakeWays

1. Search it
2. indentation do not do if changing in existing code
3. puchna mana nahi but explore karoga sab kuch to maza aayega
4. Strict rules nahi hai

----------------------------------------------------------------------------------

1. Remove solr.config lib mappings
2. upload configset in zookeper
3. enabled security solr
4. security.json upload zk

--------------------------------------------------------------------------------

./gradlew "ofbiz --load-data readers=seed,seed-initial,ext-seed,ext,ext-menu,ext-upgrade,ext-user-uat"
org.apache.solr.client.solrj.SolrClient;


SolrClient = HttpSolrClient(getSolrHost(host,corename));
Map<String, Object> httpResponse = co.hotwax.search.SolrQuery.use(delegator).fromCore("enterpriseSearch").query(jsonObject.toString()).where(paramMap).response();
     http://localhost:8983/solr/core2/select?q=*:*
http://solr-node:8983/solr/mycollection/select?q=*:*
 
        
---------------------------------------------------------------------------------------
For whatching the logs of solr

1. tail -F ../solr-current/server/logs/solr.log
2. ps aux |grep java : we can see process which is using the java  
3. kill -9 18561 : kill by proccess Id

-------------------------------------------------------------------------------------
In security.json they are expecting the secret-key
./bin/solr zk ls / -z localhost:9983
As the encrypted one and then inside it is decoded and then generate token and compare with outside token
base64 encoded secret key


RGhsTUN4MFRoLVhZSUNFREpJd2N6YjJTaExtd0lVWHNOVjVJaHhHaWN3dkNYZFNRd09pZ3E5Tlp1
cldPdkdJcFpfdmtPUTZra3VXeU1LM2ZzWGpFOHNIS3R6MzBBOVBoRW04cld3LVVCNC1NbXlrQlp0
NE9GUDVvS2NRdGNPXzVXOXRmVXVCNlUyUUoxeENMbkNFWUZRSnRJM1JUbzV5a0pSaGExQjduV0d3

--------------------------------------------------------------------------------------------
### Important info about Why to use Schema
If we would not give schema to docs then if will index all docs,  but it will cause the problem when one field comes with different data type it will take as 1 index-doc field as its type and next time you give something else it will give you error.

and for utilizing fields efficiently we are giving schema

and if are specifing schema then doc does not contains the other filed outside from schema.

--------------------------------------------------------------------------------------------
Clean varible I have to add in the url
your_product_store_id
## Zk cmds

1. ./bin/solr zk ls / -z localhost:9983

configs :Here confiset is places
overseer
aliases.json
live_nodes
collections
overseer_elect
security.json
clusterstate.json
autoscaling
autoscaling.json

2. ./bin/solr zk ls /configs -z localhost:9983

3. ./bin/solr zk rm 
4. bin/solr zk cp ./security.json zk:security.json -z localhost:9983
5. bin/solr zk cp file:local/file/path/to/solr.xml zk:/solr.xml -z localhost:2181
------------------------------------------------------------------------------------------------------------------------
## Solr-SQL 

### This error comes because of '-' in the name of core local-enterpriseSearch

"Failed to execute sqlQuery 'SELECT productId FROM local-enterpriseSearch LIMIT 10' against JDBC connection 'jdbc:calcitesolr:'.\nCaused by: Error while executing SQL \"SELECT productId FROM local-enterpriseSearch LIMIT 10\": parse failed: Encountered \"local\" at line 1, column 23.\nWas expecting one of:\n    \"LATERAL\" ...\n    \"TABLE\" ...\n    \"UNNEST\" ...\n    <IDENTIFIER> ...\n    <HYPHENATED_IDENTIFIER> ...\n    <QUOTED_IDENTIFIER> ...\n    <BACK_QUOTED_IDENTIFIER> ...\n    <BRACKET_QUOTED_IDENTIFIER> ...\n    <UNICODE_QUOTED_IDENTIFIER> ...\n    \"(\" ...\n    ",



-------------------------------------------------------------------------------------------------------------------------
## MultiAuth Plugins

{
    "authentication": {
      "class": "solr.MultiAuthPlugin",
      "schemes": [{
        "scheme": "basic",
        "blockUnknown": true,
        "class": "solr.BasicAuthPlugin",
        "credentials": {
          "solr":"IV0EHq1OnNrj6gvRCwvFwTrZ1+z1oBbnQdiVC3otuq0= Ndd7LKvVBAaZIF0QAVi1ekCfAJXr1GGfLtRUXhgrF8c="
        },
        "forwardCredentials": false
      },
      {
        "scheme": "bearer",
        "class": "solr.JWTAuthPlugin",
          "blockUnknown": true,
          "requireIss": false,
          "principalClaim":"sub",
          "jwk": {
              "kty": "oct",
              "use": "sig",
              "kid": "k1",
              "k": "DhlMCx0Th-XYICEDJIwczb2ShLmwIUXsNV5IhxGicwvCXdSQwOigq9NZurWOvGIpZ_vkOQ6kkuWyMK3fsXjE8sHKtz30A9PhEm8rWw-UB4-MmykBZt4OFP5oKcQtcO_5W9tfUuB6U2QJ1xCLnCEYFQJtI3RTo5ykJRha1B7nWGw",
              "alg": "HS512"
          }
      }]
    }
  }

  <!-- ==================================================================================================== -->

  ## Link for genrating the Basic Auth Password with salt

  https://gist.github.com/rmalchow/51f5b23c2f59c687b001bfcdbf4bad5c

  https://stackoverflow.com/questions/74939937/how-to-create-solr-password-hash

  https://github.com/ansgarwiechers/solrpasswordhash

<!-- ==============================================================================================

 -->


 curl -u solr:SolrRocks -H 'Content-type:application/json' -d '{
   "set-user-role" : {"solr": ["admin","dev"],
                      "harry": null}
}' http://localhost:8983/solr/admin/authorization


curl --user solr:SolrRocks http://localhost:8983/solr/admin/authentication -H 'Content-type:application/json' -d '{
  "set-user": {"tom" : "TomIsCool" ,
               "harry":"HarrysSecret"}}'

<!-- ==============================
 -->
 {
    "responseHeader": {
        "status": 0,
        "QTime": 0
    },
    "authorization.enabled": true,
    "authorization": {
        "class": "solr.RuleBasedAuthorizationPlugin",
        "permissions": [
            {
                "name": "security-edit",
                "role": "admin"
            }
        ],
        "user-role": {
            "solr": "admin"
        }
    }
}

<!-- ==================================================================================================================== -->

## Create a user in solr-cloud
URL: Method POST
http://localhost:8983/solr/admin/authentication

Payload

{
    "set-user": {
        "basic": {"Krewe":"Krewe123!"}
    }
}


-First I have uploaded the changed security.json
and then I have assigned it to the admin user of jwt_token
-And the I created the BasicUser from postman
-And then created the readOnlyKrewCollection role
-And then I have assigned the role to the BasicUser

krewe
Ht5#nkrewe

Change the order of permission by using before clause

With local-enterpriseSearch search admin role not working check for that
<!-- ==================================================================================================================================================== -->
# Permission and Authorization

Understand how Role-Based-Plugin and rules work in Solr:

Authentication: It deals with user creation, user-password update
Authorization: It deals with permissions and role allotment and it also maps roles to users.

Custom Permission Setup:
Below are the options through which we can configure our custom permission with the help of the available set of pre-defined 
- name
- collection
- path
- method
- params
- role

## How Rule Matching Works in Solr:
Generally, the order of permissions does not matter, but the preferred order of permissions should be from top to down, progressing from more specific to generalized levels of permission.

In cases where multiple permissions match an incoming request, Solr chooses the first matching permission and ignores all others—even if those other permissions would match the incoming request!
The ordering Solr uses is complex. Solr attempts to check first for any permissions that are specific or relevant to the incoming request (if not found, it moves on to more general permissions; if permission is not restricted, the user simply gets access).**only moving on to more general permissions if none of the more specific ones permissions match.**
If the same permission is assigned to two different roles, such as "read" ➝ role1 and "read" ➝ role2, the order is declared as presented here.
Here, the problem arises when user2 (which has role2 permission) attempts to access the "read" permission. Solr initially matches it with the "read" permission assigned to role1 and returns from there to verify if this role is assigned to user2. The answer is no, so access is denied. So keep care for colliding permissions

{"name": "read", "role": "dev"}, 
{"name": "coll-read", "path": "/select", "role": "*"},
{"name": "techproducts-read", "collection": "techproducts", "role": "other", "path": "/select"}, 
{"name": "all", "role": "admin"} 


## Types of RuleBasedAuthorizationPlugin : 
RuleBasedAuthorizationPlugin: Supports both JWT and Basic Auth, deals with the hardcoded mapping of roles➝user but mapping can be updated via API. 
ExternalRoleRuleBasedAuthorizationPlugin: Problem: not able to work with BasicAuth Authentication, deals with dynamic roles that come from JSON-request.

User’s roles may either come from the request itself, then you will use the ExternalRoleRuleBasedAuthorizationPlugin variant of RBAC. If you need to hardcode user-role mappings, then you need to use the RuleBasedAuthorizationPlugin and define the user-role mappings in security.json like this

{
"authentication":{
   "class": "solr.JWTAuthPlugin", 
   "jwksUrl": "https://my.key.server/jwk.json", 
   "rolesClaim": "roles" 
},
"authorization":{
   "class":"solr.ExternalRoleRuleBasedAuthorizationPlugin", 
   "permissions":[{"name":"security-edit",
      "role": "admin"}] 
}}

We expect each JWT token to contain a "roles" claim, which will be passed on to Authorization.

## Conclusion: we are going with RoleBasedPlugin which deals with both JWT and BasicAuth and via API, we can update the mapping(role➝user) via api 


<!-- ===================================================================================================================================== -->
## Core making ways and its Schema:

Either you would use predefined schema or we can directly index data with proper format it it will figure out data type automatically, flexibility if new field came it will index it, other in predefined you got error because of configset.
Here you have to enable some kind of free-fall configuration or I think its auto-enabled.

<!-- ========================================================================================================================================== -->

## Schemaless Schema Design : 

### Schemaless Mode is a set of Solr features that, when used together, allow users to rapidly construct an effective schema by simply indexing sample data, without having to manually edit the schema.

These Solr features, all controlled via solrconfig.xml, are:

- Managed schema: Schema modifications are made at runtime through Solr APIs, which requires the use of a schemaFactory that supports these changes. See the section Schema Factory Configuration for more details.

- Field value class guessing: Previously unseen fields are run through a cascading set of value-based parsers, which guess the Java class of field values - parsers for Boolean, Integer, Long, Float, Double, and Date are currently available.

- Automatic schema field addition, based on field value class(es): Previously unseen fields are added to the schema, based on field value Java classes, which are mapped to schema field types - see Field Type Definitions and Properties.


### You Can Still Be Explicit
Even if you want to use schemaless mode for most fields, 
you can still use the Schema API to pre-emptively create some fields, with explicit types, before you index documents that use them.
Internally, the Schema API and the Schemaless Update Processors both use the same Managed Schema functionality.

Also, if you do not need the *_str version of a text field, you can simply remove the copyField definition from the auto-generated schema and it will not be re-added since the original field is now defined.


Here we have predefined configset through which we can prepare out schemaless core : 
Which has benefits: 
1. Runtime guessing of the fields.
2. And any new field can be index.
3. we can use Schema Api still.

Either we can use directly predifined schemaless modal confiset, or we can make our schemaless confiset by defining the mapping in the 

Note: 
### Once a field has been added to the schema, its field type is fixed. 
As a consequence, adding documents with field value(s) that conflict with the previously guessed field type will fail. For example, after adding the above document, the “Sold” field has the fieldType plongs, but the document below has a non-integral decimal value in this field:

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Types of schema Fields :

### 1. Standared field which has multiple options : 

### 2. Dynamic field : Dynamic fields allow Solr to index fields that you did not explicitly define in your schema.

These are the field whose name starts with *_prefix which allows to index the field which does not have the explicit mapped in mannaged-schema, it will figure out at runtime and match with dynamic field mapps and the option will apply as mentioned.

For example, suppose your schema includes a dynamic field with a name of *_i. If you attempt to index a document with a cost_i field, but no explicit cost_i field is defined in the schema, then the cost_i field will have the field type and analysis defined for *_i.
<dynamicField name="*_i" type="int" indexed="true"  stored="true"/>

### 3. Copy fields : If you want to use the same fields in different different kind of field types then we can use copy-field options, as the copying of value done before the analysis phase so options are applied after copying.
You might want to interpret some document fields in more than one way. Solr has a mechanism for making copies of fields so that you can apply several distinct field types to a single piece of incoming information.

The name of the field you want to copy is the source, and the name of the copy is the destination. In the schema file, it’s very simple to make copies of fields:

<copyField source="cat" dest="text" maxChars="30000" />

- In this example, we want Solr to copy the cat field to a field named text. Fields are copied before analysis, meaning you can have two fields with identical original content, but which use different analysis chains and are stored in the index differently.

- You can't copy copy-filed like copy from here -> there -> elseWhere not possible,
This means that copy fields cannot be chained i.e., you cannot copy from here to there and then from there to elsewhere.
However, the same source field can be copied to multiple destination fields:

<copyField source="here" dest="there"/>
<copyField source="here" dest="elsewhere"/>

- The **maxChars** parameter, an int parameter, establishes an upper limit for the number of characters to be copied from the source value when constructing the value added to the destination field. 
Useful when you want to copy some-data from the source field, but also control the size of index files.

- Both the source and the destination of copyField can contain either leading or trailing asterisks, which will match anything. For example, the following line will copy the contents of all incoming fields that match the wildcard pattern *_t to the text field.:

<copyField source="*_t" dest="text" maxChars="25000" />
Here is a catch if you are using wild-chars in dest then it is must to use in source also, but its vise-versa is not true.

-

## Options : 
### 4.The decision to set stored="true" depends on your use case and requirements. Here are some considerations:

Retrieving Original Values:

If you need to retrieve the original values of a field when querying the index (e.g., for displaying search results or extracting content), you should set stored="true".
Stored fields can be retrieved without the need to go back to the source system. This can be useful for performance and can reduce the number of lookups needed.
Displaying Search Results:

If your application involves displaying search results with snippets or highlighting, having the original content stored allows Solr to generate accurate and meaningful snippets.

## Mailing List ,Invetition for Slack

https://solr.apache.org/community.html#mailing-lists-irc
https://communityinviter.com/apps/apachesolr/apache-solr

--------------------------------------------------------------------------------------------------------------------------------------------
## Score-Field
There is some Score-field in the code, whom we want be touching which helps that, Learn to rank, basically here is workflow where we would use simple-query to filter the data and then we would apply the the complex query on top 100 docs and rank is provided by the query and query is parsed by the rank-Model (which is trained outside the solr and exported inside solr as custom model) and this model rank the docs that how it works.
Feature
q
rq
fl

stored-> sore the data in disk which makes lookup much slower instead of this we have to use doc-values as this follow column fastion to store the data and doc to value which make lookups to faster

---------------------------------------------------------------------------------------------------------------------------------------------------
## PostCode Lookup data Json for japnease

https://www.back4app.com/database/back4app/lisf-of-japan-postal-codes/graphql-playground

Solution
- Index the data using schema less mode and observe what field types are used 
- Study field types and assign best suitable types to fields for optimised searching
- Index the documents 
- Create config set for this core   

### Enable geo filtering and store lat-long data in suitable format 

- Set field type of latitude and longitude as string
- Create processor chain to concate them and create location field
<updateRequestProcessorChain name="uuid-location">
      <processor class="solr.UUIDUpdateProcessorFactory">
        <str name="fieldName">id</str>
      </processor>
        <processor class="solr.CloneFieldUpdateProcessorFactory"> 
            <str name="source">latitude</str> 
            <str name="dest">location</str> 
        </processor> 
        <processor class="solr.CloneFieldUpdateProcessorFactory"> 
            <str name="source">longitude</str> 
            <str name="dest">location</str> 
        </processor> 
       <processor class="solr.ConcatFieldUpdateProcessorFactory"> 
            <str name="fieldName">location</str> 
            <str name="delimiter">,</str> 
        </processor>
      <processor class="solr.LogUpdateProcessorFactory"/>
      <processor class="solr.RunUpdateProcessorFactory" />
     </updateRequestProcessorChain>

  <initParams path="/update/**,/query,/select,/tvrh,/elevate,/spell,/browse">
    <lst name="defaults">
      <str name="df">_text_</str>
      <str name="update.chain">uuid-location</str>
    </lst>
  </initParams>
- Apply geo filtering on location field

- Create composite id for unique identifier 

- Create new field to create and store composite id in schema 
<field name="docType-identifier" type="string" multiValued="false" indexed="true" required="true" stored="true"/>

- Set it as unique key in schema 
  <uniqueKey>country-code-id</uniqueKey>

-  Create update processor chain for composite id 
  <updateRequestProcessorChain name="composite-id">
    <processor class="solr.CloneFieldUpdateProcessorFactory">
      <str name="source">Country</str>
      <str name="source">postcode</str>
      <str name="dest">country-code-id</str>
    </processor>
    <processor class="solr.ConcatFieldUpdateProcessorFactory">
      <str name="fieldName">country-code-id</str>
      <str name="delimiter">-</str>
    </processor>
    <processor class="solr.LogUpdateProcessorFactory" />
    <processor class="solr.RunUpdateProcessorFactory" />
  </updateRequestProcessorChain>

- Create request handler and add chain 
  <requestHandler name="/update" class="solr.UpdateRequestHandler">

    <lst name="defaults">
      <str name="update.chain">composite-id</str>
    </lst>

  </requestHandler>

### Implement Search with partial and full keyword 

To enable exact keyword match in postcode ignoring spaces, add this   - 
      <tokenizer class="solr.KeywordTokenizerFactory"/>
      <filter class="solr.PatternReplaceFilterFactory" pattern="(\s+)" replacement="" replace="all" /> 

To enable partial searching do the following steps - 
Create a copy field for postal code (postcodelike)
Add the following to the copy field definition 
<tokenizer class="solr.KeywordTokenizerFactory"/>
      <filter class="solr.PatternReplaceFilterFactory" pattern="(\s+)" replacement="" replace="all" /> 
<filter class="solr.NGramFilterFactory" minGramSize="1" maxGramSize="10"/> 

-------------------------------------------------------------------------------------------------------------------------------------------------------
## Major Changes from 7.9 to 8.9 version in solr

1. Major Changes 
### DocValues
	     The standard way that Solr builds the index is with an inverted index. This style builds a list  of terms found 
         in all the documents in the index and next to each term is a list of documents that the term appears.
	    This makes search very fast - since users search by terms, having a ready list of term-to-document values make
        the query process faster.
       For other features that we now commonly associate with search, such as sorting, faceting, and highlighting, this
       approach is not very efficient.
       docValues - Build a forward index in a column stride fashion.

      DocValue fields are now column-oriented fields with a document-to-value mapping built at index time. 
      This approach promises to relieve some of the memory requirements of the fieldCache and make lookups for
      faceting, sorting, and grouping much faster.

### Uninvertible
	    If true, indicates that an indexed="true" docValues="false" field can be "un-inverted" at query time to build up
	    large in memory data structure to serve in place of DocValues. Defaults to true for historical reasons, but
	  users are strongly encouraged to set this to false for stability and use docValues="true" as needed.

2.  Performance Impact 
	if you need to scan a field (for faceting/sorting/grouping/highlighting) it will be a slow process, as you will have to
    iterate through all the documents and load each document's fields per iteration resulting in disk seeks.
	Doc Values will be a faster alternative as it is stored in column stride fashion.

	Uninvertible is set to true for backward compatibility but it creates field cache which occupies more memory and
takes more time to process the query. 


----------------------------------------------------------------------------------------------------------------------------------------------------------

### Problem Statement 
Add Japanese post code data in postcodelookup core 

### Solution
Find accurate postal code with latitude and longitude
Verify the data 
Convert data to JSON 
Create a NiFi flow to filter and remove unnecessary fields 
Add Country field
Index data into Solr 

https://www.back4app.com/database/back4app/lisf-of-japan-postal-codes
NIFI (filters the data), jolt filters the json spec

------------------------------------------------------------------------------------------------------------------------------------------
# Suggest, spell

https://doc.sitecore.com/xp/en/developers/91/platform-administration-and-architecture/using-solr-auto-suggest.html

--------------------------------------------------------------------------------------------------------------------------------------------
# configset solrconfig.xml related changes

solrconfig.xml
1. updateRequestProcessorChain -> Here we can mention that we have to use schema-less model or schema. 
2. updateHandler ->  here we can set hard,soft commits,updateLog
3. lib -> Here we can import the lib from lib folder
4. query -> Query section - these settings control query time things like caches


http://wiki.apache.org/solr/GuessingFieldTypes



1. That thing require the refresed-token but we are not going for that we are using the same token for whole time.


  <!-- Update Processors

       Chains of Update Processor Factories for dealing with Update
       Requests can be declared, and then used by name in Update
       Request Processors

       http://wiki.apache.org/solr/UpdateRequestProcessor

    -->

  <!-- Add unknown fields to the schema

       Field type guessing update processors that will
       attempt to parse string-typed field values as Booleans, Longs,
       Doubles, or Dates, and then add schema fields with the guessed
       field types. Text content will be indexed as "text_general" as
       well as a copy to a plain string version in *_str.

       These require that the schema is both managed and mutable, by
       declaring schemaFactory as ManagedIndexSchemaFactory, with
       mutable specified as true.

       See http://wiki.apache.org/solr/GuessingFieldTypes
    -->
    
    
    <!-- The information from solrconfig.xml is just an update chain definition. 
  Unless you *activate* that update chain, it will not take effect.  You
  can only have one update chain active, so if you're currently using the
  "add-unknown-fields" chain commonly found in examples, that will no
  longer be running once you activate this new one. -->

Why are you using an update chain to do what the schema can do natively
with copyField?

## Postalcode init for update etc things : uuid-location is chained
  <initParams path="/update/**,/query,/select,/tvrh,/elevate,/spell,/browse">
    <lst name="defaults">
      <str name="df">_text_</str>
      <str name="update.chain">uuid-location</str>
    </lst>
  </initParams>
  
## EnterpriseSearch: Here we have a composite-id updateRequestProcessorChain which is chained in 
  <requestHandler name="/update" class="solr.UpdateRequestHandler">
    <!-- See below for information on defining
         updateRequestProcessorChains that can be used by name
         on each Update Request
      -->

    <lst name="defaults">
      <str name="update.chain">composite-id</str>
    </lst>

  </requestHandler>

  <!-- ------------------------------------------------------------------------------------------------------------------ -->

  # Analyser, Tokenizer, Filters

  Analyser : In this firstly fields are converted into token stream and then it will tokenized and then on top of that Filters applied. By applying whole     process we would got **term**, Analyser face will run on indexing-doc time as well as for the quering time.

  Analyser is a unit which is composed of filters and the tokenizers, and together this will create the analyser.

  **Term** : This term store the simplified and easy to searchable form with accent removing,lowercasing,whitespacing removing, **And this term is used for Query while querying on this filed**.
  Note: `Big Shot` this actual value stored in the disk and the term might be this `big shot`.  

## Field Values versus Indexed Terms
The output of an Analyzer affects the terms indexed in a given field (and the terms used when parsing queries against those fields) but it has no impact on the stored value for the fields. For example: an analyzer might split "Brown Cow" into two indexed terms "brown" and "cow", but the stored value will still be a single String: "Brown Cow"


There can be 2 senerious
1. Same analyser can be used for index and query phase
2. we can define 2 analyser 1 for index and 1 for query: Some use case needs this implementation

<fieldType name="nametext" class="solr.TextField">
  <analyzer type="index">
    <tokenizer class="solr.StandardTokenizerFactory"/>
    <filter class="solr.LowerCaseFilterFactory"/>
    <filter class="solr.KeepWordFilterFactory" words="keepwords.txt"/>
    <filter class="solr.SynonymFilterFactory" synonyms="syns.txt"/>
  </analyzer>
  <analyzer type="query">
    <tokenizer class="solr.StandardTokenizerFactory"/>
    <filter class="solr.LowerCaseFilterFactory"/>
  </analyzer>
</fieldType>

 at index time the text is tokenized, the tokens are set to lowercase, any that are not listed in keepwords.txt are discarded and those that remain are mapped to alternate values as defined by the synonym rules in the file syns.txt. This essentially builds an index from a restricted set of possible values and then normalizes them to values that may not even occur in the original text.

 At query time, the only normalization that happens is to convert the query terms to lowercase. The filtering and mapping steps that occur at index time are not applied to the query terms. Queries must then, in this example, be very precise, using only the normalized terms that were stored at index time.

3. Analysis for Multi-Term Expansion
In some types of queries (i.e., Prefix, Wildcard, Regex, etc.) the input provided by the user is not natural language intended for Analysis. Things like Synonyms or Stop word filtering do not work in a logical way in these types of Queries.

In that case the 


### Tokenizers : It will take word as input and convert/parse them in the token stream, and while applying tokenization the operation depends upon the type of tokenClass it will generate the token stream.

### Filters : It will take the token-stream as input and filter the words based on stammmers and filters type, we can give some set dict and then it will include only those words.

Filters examine a stream of tokens and keep them, transform them or discard them, depending on the filter type being used.

## There are diffrent types of tokenizers available: StandardTokenizer.
## There are diffrent type of Filters availbale : phonetic, etc 
and Here in analysis section on the UI throw which you can analyse the filed type .It is working as expected or not.

Schema Design /Index insertion/

-----------------------------------------------------------------------------------------------
# Oms Utilization of solr

As solr so much efficient and tunned for search/read efficent. we would maintain the transaction-db where the data-maintains, and on first-startup we would sync all data to solr.

and after that if any Order comes so service run and for that eecas also run where solr-indexing service will trigger which soft-commit the data into the solr.

and On Production side we are maintaing 2 DB ,
1. Transaction DB
2. Read-Heavy Zero-Sync-Time AWS Service managed DB.

---------------------------------------------------------------------------------------------------
