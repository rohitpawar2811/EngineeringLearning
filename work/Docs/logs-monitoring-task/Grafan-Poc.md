# Grafana-POC 

1. Place the .yml file here /etc/grafana/provisioning/alerting -> alerts.yml,contact.yml,policies.yml
2. And then restart the docker container
3. And you will get the whole templates as provisioned import in the grafan.
4. But there was problem that policies.yml was common-one and reffered to all contact-points if you missed the one contact point you will get the error.
5. And another issue is that I am not able to view or edit the provisioned file and imorts 
How can we resolve the 5th point : they mentioned that we have to contact to server adminstrator to update the provisioned file.


1. Practises I have to write 
2. I have to test datasource thing in 2 ways : 
	1. manually yml edit 
	2. from UI
3. Lokie datasource connected or not.
4. Smtp configured and problem we are not able to edit the file


https://sushruthan.medium.com/grafana-smtp-configuration-gmail-a01854ae0469