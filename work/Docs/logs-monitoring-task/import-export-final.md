# April 8 2024

1. Alert Post, GET options are available here but problem is that we can not POST the bulk rules at a time. Another things to point that we have to call the GET Api and get the payload and then we have to do some manipulations and then post.

2. Blocker was datasource in that the Lokie ID was diffrent and we have to configuraly handle it for multiple datasources.

3. Notification-policy by default only one and others one's would create is inside it means nested policy.
so PUT, Delete methods are only available. PUT/POST will replace the whole content

4. Contact Point import is same as the Alert-rule , we can't be able import it in bulk so we have to manage the flow and we know that 1 cp has multiple points configured, so if we hit multiple times we got multiple point.

Here Now I have to check for teraforme and recommended ways to perform this thing  

https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/

https://github.com/grafana/grafana/issues/48623

http://www.m3mobile.net/en/industry

------------------------------------------------------------------------------------
# Apr 9 2024:

## PHPLDAPADMIN

draft-behera-ldap-password-policy-08.txt.

This should be done by me 
Default and User Specific Password Policy I have to change the old default password policy defined there with the new one.

DIT, ldif file I have to change the location for that is etc/ldab/schema/

- And the refrences for that was
https://www.zytrax.com/books/ldap/ch6/ppolicy.html?ref=tobru.ch#pwdpolicyattributes
https://www.zytrax.com/books/ldap/ch6/ppolicy.html?ref=tobru.ch
https://tobru.ch/openldap-password-policy-overlay/

https://kb.brightcomputing.com/knowledge-base/how-do-i-define-a-password-policy-in-ldap/


## Terraform with grafana
- We have the variabel we can dynamically replace in the templates.
- We have to manage the exported templates of the grafana in the terraform.
- There is terraform configuration file we have to configure and for applying `terraform apply`.

References
1. [Terraform Provisioning in Grafana Documentation](https://grafana.com/docs/grafana/latest/alerting/set-up/provision-alerting-resources/terraform-provisioning/)
2. [Grafana Alerting Resources Setup Documentation](https://grafana.com/docs/grafana/latest/alerting/set-up/provision-alerting-resources/)
3. [Provisioning Alerting Examples Repository](https://github.com/grafana/provisioning-alerting-examples/blob/main/config-files/README.md)

https://registry.terraform.io/providers/grafana/grafana/latest/docs

## My Work I have to do
1. Password
2. Terraform
3. Terraform Learning basic Architecture how we are learning it.
4. What is terraform provider
5. I have to write the bash script regards to there is 2 instances I am importing templates to another instance with proper configurations
6. There is another use-case for in-instance level duplicate whole template with different-job id.
7. And then document on it.

git-lab api
directory maintained we would use that
and we have to Poc on what was the diffrence on the content of get api and the exported content. because only exported content works perfectly or might ulta hai eshi ka.
Folder dir etc we have to check for that.

1. Fetch the data from git-hub.
2. then transform the data like datasource-id of loki.
3. Resource should be UI-editable.
4. Then post on the target instance.
5. Github-api 
6. github-token
7. and other source and target credentials

# Api Using and planing for provisioning

1. Folder-API
https://grafana.com/docs/grafana/latest/developers/http_api/folder/
2. Provisioning API
https://grafana.com/docs/grafana/latest/developers/http_api/alerting_provisioning/#:~:text=The%20Alerting%20provisioning%20API%20can,tool%20and%20Cortex%20tool%20respectively.
3. Datasource API
https://grafana.com/docs/grafana/latest/developers/http_api/data_source/

--------------------------------------------------------------------------------------------------------------------------------

## Export alerts in provisoining formate:

/api/v1/provisioning/alert-rules/:uid/export
/api/v1/provisioning/alert-rules/export

## Normal-Api formate get

/api/v1/provisioning/alert-rules
/api/v1/provisioning/alert-rules/:uid	

DELETE  /api/v1/provisioning/alert-rules/:uid	
POST	/api/v1/provisioning/alert-rules	

## Folder And Group related api

GET	/api/v1/provisioning/folder/:folderUid/rule-groups/:group : get a rule group in normal formate

PUT	/api/v1/provisioning/folder/:folderUid/rule-groups/:group : interval update only

GET	/api/v1/provisioning/folder/:folderUid/rule-groups/:group/export : export in provisioning file formate
	
	
# Findings
- I have succefully hit the api by copying only Rule-data form the export. and here cache was that the exported files are only meant for provisioning in file system only.
- We are only able to download templates at folder level or group level.
- Provisioned files are only for provisoned setup which is non editable
- The difference b/w both provisoned and non provisioned was that in provisioned there is extra layer and covered in rule-group, while non-provisioned one does'nt have the rule-group layer the folder and other namespace related details come in same level, through which api easily creates the alert.

- So I thing we have to prefer the json non-provisioned data for alert creation.

Difference is this

        "id": 2,
        "uid": "f69b047c-9b06-4563-846e-36bb7a4ecf75",
        "orgID": 1,
        "folderUID": "bdhm0ox7ji9kwd",
        "ruleGroup": "SM-uat Errors",
        
        
- We can post the data one at a time.

- Now I have to check for edit of lokie datasource thing.
- Second Here I have to if we are going with provisioned-format then we want FolderUID.

**Problem** and we get folderUID only when there is another folder which is already created.
soln -> we manually create the folder ID here and then give input to script and also ruleGroup
soln2 -> Find api post which creates folder as well rulegroup(not-existed only then) while posting the data.


- we need must folderUID other blank folder created 

Create folder
POST /api/folders

Creates a new folder.
response extract 
{
    "id": 7,
    "uid": "cdii12oza6n0gd",
    "orgId": 0,
    "title": "Example-UAT-MAIN",
    "url": "/dashboards/f/cdii12oza6n0gd/example-uat-main",
    "hasAcl": false,
    "canSave": true,
    "canEdit": true,
    "canAdmin": true,
    "canDelete": true,
    "createdBy": "admin",
    "created": "2024-04-12T09:57:30.364651774Z",
    "updatedBy": "admin",
    "updated": "2024-04-12T09:57:30.364651861Z",
    "version": 1
}


- Check for folder it already exits or not.
- We would use provisioned one data file to extract folder details and then go for creating folder.

------------------------------------------------------------------------------------
We can datasource by name lokie :how we know which dataource we would find from json data.

Get a single data source by name
GET /api/datasources/name/:name


----------------------------------------------------------------------------------------------------------------------------------------------------

Data parsing I have to figure out that how much data I wanted from the json 
that was the one complicated task.
Just insert thing right now
1. Extract from the provisioned file.
2. Divide in some var $Folder-name, $group-name, $Actual-data-toPost
3. Now we have to $target-instance,user,pass -> we will post the whole data into the targeted instance.

