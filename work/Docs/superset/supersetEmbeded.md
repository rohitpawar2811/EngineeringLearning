    
 1. There are 1 user we would manage which has all access related to see realted to dashboard and all dashbords access plus that user has assigned guest-user role
 
 2. And another org-level-user, for security we are maintaining the organization level user and provide access for perticular embedded dashboard.
 
 3. Through auth api we have to pick token of org-level-user: 
 	1. from org-level-user we generate their token and pass to dashbord fetch api: and get accessible dashboards.
 	2. from admin-user cred we generate token -> provide this to guest-token-generate api as this needs auth, :and we pick guest token and then pass on to frontend.
 
 
 
 1. Get list of of dashboards from org specific user
 	1. Use authtokengen api to get bearer token for org-user
 	2. Simply call the dashboard getting api.
 	3. We can further filter dashboards only embedded one.
 	4. Now we would get all data on frontend side
 	5. Showcase the dashboards in the frontend side.
 2. Now on click to dashboard.
 	1. Request will reach(with dashboard id, rls, etc) -> org-specific oms and request call for featchGuestToken corresponds to guest-user and bearer token of org-user which has permission to generate guest token.
 	2. Now frontend recieved guest-token
 	3. Using this guest-token frontend call the iframe fetch using @superset-embedded lib.
 	4. we can set guest-token expire limit, so we would cache the feached guest token. because iframe refreshal will refresh-iframe in every 5 min.
 	

Enhancement :
	1. Instead of feaching guest token for perticular one dashboard, we can make guest token for all dashboards and send to front where it cached and further calls for dashboards will use the same token.
	2. If we go for above case then dashbords fetch we can't cache, because now access is all in all depends on list of dashboards got from api.
	if we want cache then it must be sort-term, as for updates reflect quick -> ye to karna hi hai

Backend Api Required: 
1. FeatchDashboards
2. GenerateAuthTokenByOrgUser
3. GenerateGuestToken for specific dashboard, RLS, which comes with request , and guest-user cred saved on oms side
 
 
         {
            "type": "dashboard",
            "id": "800fdce7-bd9d-439f-baed-32350be91b04"
        }
        
        1: overhead, security,less-speed,quantity-fit when less dashboards
        2: no-overhead, no-securty,speed high,quantity-fit large as well.

        
 
 =============================================================================================================================================================
## DATE Jan 13 2024
# Ofbiz-UI for SupersetEmbedded

- I can use grovvy and preproccess the getDahboardEvent and get the response json and then render that response json into ftl
- Here we can call event by using form and redirect to again the same page and check that perticular parms are present then render otherwise call the event.

if else condition

<script src="https://unpkg.com/@preset-sdk/embedded"></script>

==============================================================================================================================================================
<div class="panel">
    <div class="panel-heading">
        <div class="panel-title">
            Embedded Dashboard
        </div>
    </div>
    <div class="panel-body">
        <div class="row equal-height-flex">
             <table class="table">
                <tbody>
                 <form class="btn" name="EmbeddedDashboardList" id="fm" action="<@ofbizUrl>getEmbeddedDashboards</@ofbizUrl>" method="get">
                     <button type="button" class="js-confirm-me" data-confirm-message="${uiLabelMap.UploadSolrConfigSetMsg}" name="EmbeddedDashboardList" title="${uiLabelMap.UploadSolrConfigSet}">
                         ${uiLabelMap.UploadSolrConfigSet}
                     </button>
                 </form>
                </tbody>
            </table>
        </div>
    </div>
</div>


1. I would go for 2 pages on where I would show the ListOfDashbords in ListDashboards.ftl 
2. and after cliking on the dashboards we would render the next-view with dashboards details (here we would made a simple Post request with input params which is rendered on ui.)
3. and in processing we would generate the guestToken and all those varible goes on view and then dashboards will render 
4. ,and upon clicking on back button it will came to the main page again where all dashboards are visible.

### Auth True is Remaning I have to do that thing.
### UILabels I have to use.
### Flow check.
### The rendering done code is visible via inspecting the code , and this will also exposing the token and dashboard-id and host, We have to some how make this invisible. 


<head>
    <style>
        #my-superset-container {
            width: 100%;
            height: 850px;
            overflow: hidden;
        }
        #my-superset-container iframe {
            width: 100%;
            height: 100%;
            border: none; /* Remove iframe border */
        }
    </style>
</head>
<div id="my-superset-container"></div>
<script src="https://unpkg.com/@superset-ui/embedded-sdk"></script>
<script>
supersetEmbeddedSdk.embedDashboard({
            id: "50347601-aab1-4310-bf54-17bf7adfebe1", // Replace with your dashboard ID
            supersetDomain: "https://tathya-uat.hotwax.io/",
            mountPoint: document.getElementById("my-superset-container"),
            fetchGuestToken: () => "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7InVzZXJuYW1lIjoiZW1iZWRkZWQiLCJsYXN0X25hbWUiOiJlbWJlZGRlZCIsImZpcnN0X25hbWUiOiJlbWJlZGRlZCJ9LCJyZXNvdXJjZXMiOlt7InR5cGUiOiJkYXNoYm9hcmQiLCJpZCI6IjUwMzQ3NjAxLWFhYjEtNDMxMC1iZjU0LTE3YmY3YWRmZWJlMSJ9XSwicmxzX3J1bGVzIjpbXSwiaWF0IjoxNzA1MTQ0NTEzLjg4NTc3OTksImV4cCI6MTcwNTE2MjUxMy44ODU3Nzk5LCJhdWQiOiJodHRwOi8vdGF0aHlhLXVhdC5ob3R3YXguaW8iLCJ0eXBlIjoiZ3Vlc3QifQ.qoxuvc2uHVe5PToifuFmwlyMTtvbc_SZx-R3yJjGJk8",
            dashboardUiConfig: { hideTitle: false }, // dashboard UI config: hideTitle, hideTab, hideChartControls (optional)
   });
</script>
</#if>

# =============JAN19 2023 the End=====================================================================================================

1. How to hide that token in the app, thats was leaking the security by exposing the token
2. Name ones
3. That one extra service for creating the bulk token of all dashboard for all.
