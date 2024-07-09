# Setup Monitoring Alerts for New Instances

### Introduction
This document outlines the process of setup monitoring alert for any new Instance.

### Process 
This process consists of preparing the generic-templates for alert-rules, and then transform it using transformation_script.sh. After that you have to run import_script.sh which uploads the alert-rules to target instance.
1. generic templates : We need to prepare generic-templates for alert-rules, Although we had already prepared templates for oms, maarg, tathya, nifi and we can add on further on it. 
2. transformation_script.sh : This script transforms the generic-templates into actual templates based on inputs like instance, instance-url, folder-name, job_name, instance_type. After performing scripts work it will create a temp dir which contains alert-rules.json, contact-point.json, notification-policy.json.
3. import_script.sh : This script will upload or we can setup the alerts on the grafana instance, Here this script consists of some input and after providing them it will pick the transformed-templates fils form `\temp` dir and setup on the target instance and also remove temp dir.

### Steps for transformation_script.sh
1. Clone the GitLab repository: `git clone https://git.hotwax.co/devops/grafana-monitoring.git`
2. Navigate to the script folder: `cd ./script`
3. Install prerequisites: `sudo apt-get update` followed by `sudo apt-get install jq`
4. Run the command: `sudo bash transformation_script.sh`
5. After 4th step you have asked for inputs which is must example:
``` 
instance="sm-uat"
folder="sm-uat"
job_name="{job=\"sm-uat.hotwax.io\"}"
instance_url="https://sm-uat.hotwax.io/"
instance_type="oms" 

read -p "Enter instance: " instance
read -p "Enter folder: " folder
read -p "Enter job name: " job_name
read -p "Enter instance URL: " instance_url
read -p "Enter instance type: " instance_type
```
6. In above input instance_type can be oms, maarg, tathya, nifi.
7. After performing input providing step script simply create the `temp` dir which contains alert, contact-point, notification-policy.


### Steps for transformation_script.sh
1. Clone the GitLab repository: `git clone https://git.hotwax.co/devops/grafana-monitoring.git`
2. Navigate to the script folder: `cd ./script`
3. Install prerequisites: `sudo apt-get update` followed by `sudo apt-get install jq`
4. Run the command: `bash import_script.sh`
5. After 4th step you have asked for inputs which is must example:
``` 
   Enter the grafana_host : http://localhost:3000/
   Enter the grafana_username : admin
   Enter the grafana_password :
   Enter the loki_datasource_uuid (Optional will featch default loki-UUID ): YOUR_TARGET_LOKI_DATASOURCE_UUID`
```
6. Use the above command to import all alerts, contact points, and policies from `temp` dir.


Sure, here's the entire content formatted in a way that you can easily copy:



"name": "&Instance errors",
"folder": "&Folder-main",
 &JobName
"Team": "&Instance",
"alert-rule-id-type": "&Instance-alert",
"Instance URL": "&InstanceURL",

"alert-rule-id-type": "&Instance-alert",
 "Team": "&Instance",
 "Instance URL": "&InstanceURL",
&JobName

nodata
Aparts from all this error we have to find what other stack will causeing the process.

Master List of Errors is continuesly evloving list we will introduce the critical errors as we find out
Resource-list: like mentioning error-list etc.

1. We have to first analysis the for breaking-changes of current to upgraded-version which we are using.

2. We need to analysis for pached changes on superset we had done.

3. We have to analysis   

2. Test upgrade-process for local-superset setup,


https://app.clickup.com/t/86cv6qf3f


SOP update
setup_monitoring_for_new_instances.md
Null pointer one context : Here when I am sending the data error also have to send.
Nifi-templates
tathya-production rule-setup
Condition evalution is right or not can we check for that.
Pending Period 5m yet can we have to set to 0.

Setup on the production for all instances.


https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/state-and-health/

