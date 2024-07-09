## Smart Brokering Rule Engine


## Azure-AD SAML2.0 SSO

- Developed a feature from scratch as a sole contributor, showcasing strong
individual capabilities.

- Utilized Pec4j-framework with spring-boot for building the SSO backend logic end-to-end.

- Researched and Employed Pec4j-framework and design the implementation-flow specific to client-project.

- Integrated Pec4j-framework and Azure Saml2.0 SSO using Azure AD Idp file.

- Developed api like userSync, roleSync, authCheck etc and ensured generic implementation, so that other other SAML2.0 sso provider also supported.

- Deployed the application on UAT Environment, ensuring backward-compatibility and
reliability.

- Implemented Central-Logout Feature at application level by leveraged single-database capability.

- Utilized Relaystate which preserves client-webapp-link hit state and redirect to same page where user exists.

- Tested code and other resolved issue like same-site, session which caused because of cross-origin call.

- Finally Delivered to client at production.


## Search Integration  

- Integrated Lucene based search-engine Apache solr which makes searching efficient and fast.

- Design enterpriseSearch schema that contains orders data.

- Researched solr library and api for java and employed them in project. 

- Devloped utility class like SolrQuery, SearchServices for using efficently solr in services.

- Implemented the indexing services for syncOrder from OMS whenever an order created in transactional database. 

- Upgrade to solr cloud, ensured backward compatiblity so that solr-standalone still works as is.

- Ensured the scalability by deploying the solr-cloud in clustered mode.

## Restock Inventory on Schedulable

- Understand client Requirement, client has to upload inventory for specific product and it must scheduled.

- Leaveraged Buisness Process/data-model and  design the solution that we can intake inventory as shipment in oms and trigger a job-schduled that will add inventory to facility and update on shopify.

- Implemented the api that process inventory-upload to facility and build UI using react to recieve inventory file with schedule functionality.


## Automated Deployment lifecycle

- Leaveraged Gitlab CI/CD and implemented the script to automate the DockerImage creation process that utilizes AWS ECR api.
- Implemented script for Release and Tag mangement process.
- Utilized Jenkins and GitLab Runner to achieve it and make process flexible.

## Shipping integration c807

- Researched about the c807 api.
- Integrated shiping api for making fulfillment of order.
- Tested all Buisness scenerious like pick pack shipping-label and ship process.

## Hotwax OMS Support 

- Developed Fulfillment Rejection Reason api.
- Return Adjustment Report generation.
- Utilized SQL Server jobs for automated tasks and data processing.

## Apache Superset
- Apache superset configured and led it to production 
- Improved with some adjustment according hotwax-commerce product, 
- Now Organization selling analystics-dashbords in apache superset for reports like user order fulfillment, OrderBrokererd Count etc. with wide variety of vizvalizations.

 
  https://www.pega.com/job-application-thank-you?thank_you=YTVlY2ZjNjItMDI3My00MmRiLWE2OTktZjZmNDg1YzUzOTM1