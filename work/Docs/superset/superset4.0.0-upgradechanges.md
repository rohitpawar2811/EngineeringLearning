## Key Changes in Superset 4.0.0

1. **Alerts and Reports Modal Redesign:**
   - The modal for alerts and reports has undergone a significant redesign for improved usability and aesthetics.

2. **Tags Enhancement:**
   - Tags are now accessible via the TAGGING_SYSTEM feature flag. 
   - Separate models are enabled, and REST API support for tags has been added.

3. **Changelog File Structure Update:**
   - The format and structure of the changelog file have been revised to accommodate the limitation of long files not being supported in GitHub.

4. **Enhanced Drag and Drop Functionality:**
   - Users can now enjoy a seamless drag and drop experience in both dashboards and charts.

5. **Feature Flag Updates:**
   - Introduction of VERSIONED_EXPORT, DASHBOARD_FILTERS_EXPERIMENTAL, ENABLE_EXPLORE_JSON_CSRF_PROTECTION, ENABLE_TEMPLATE_REMOVE_FILTERS, REMOVE_SLICE_LEVEL_LABEL_COLORS, CLIENT_CACHE, DASHBOARD_CACHE, DASHBOARD_NATIVE_FILTERS_SET, ENABLE_EXPLORE_DRAG_AND_DROP, DISABLE_DATASET_SOURCE_EDIT, DASHBOARD_NATIVE_FILTERS, and GENERIC_CHART_AXES feature flags.
   - Deprecation of DASHBOARD_CROSS_FILTERS, ENABLE_JAVASCRIPT_CONTROLS, and KV_STORE feature flags.
   - DASHBOARD_VIRTUALIZATION and DRILL_BY feature flags are now enabled by default.

6. **Removals:**
   - Filterbox, FilterSet, and Profile features have been removed, along with the Redirect API.

7. **SQL-Lab Updates:**
   - Several changes have been made to business logic in SQL-Lab for improved functionality.

8. **Country Maps Management via Jupyter Notebook:**
   - All country maps are now managed via Jupyter Notebook. Users can dynamically add more countries to it for exploration purposes.

9. **Sunburst Chart Migration:**
   - The shift to Sunburst chart visualization has been migrated to ECharts for better performance and features.


---------------------------------------------------------------------------------------------------------------------------------------------------------

# Migrations_utils.py

Here we are using alembic.operation

What is the use of alembic in Python?
Alembic is a database migration tool that works with SQLAlchemy, a popular Python library for interacting with relational databases. Alembic allows you to manage changes to your database schema in a version-controlled way, keeping it in sync with your application code.

https://thinhdanggroup.github.io/alembic-python/#:~:text=Alembic%20is%20a%20database%20migration,sync%20with%20your%20application%20code.


-----------------------------------------------------------------------------------------------------------------------------------------------------------
#### Switching to server side sessions

Server side sessions offer benefits over client side sessions on security and performance.
By enabling server side sessions, the session data is stored server side and only a session ID
is sent to the client. When a user logs in, a session is created server side and the session ID
is sent to the client in a cookie. The client will send the session ID with each request and the
server will use it to retrieve the session data.
On logout, the session is destroyed server side and the session cookie is deleted on the client side.
This reduces the risk for replay attacks and session hijacking.

Superset uses [Flask-Session](https://flask-session.readthedocs.io/en/latest/) to manage server side sessions.
To enable this extension you have to set:

``` python
SESSION_SERVER_SIDE = True
```

Flask-Session offers multiple backend session interfaces for Flask, here's an example for Redis:

``` python
from redis import Redis

SESSION_TYPE = "redis"
SESSION_REDIS = Redis(host="redis", port=6379, db=0)
# sign the session cookie sid
SESSION_USE_SIGNER = True
```

----------------------------------------------------------------------------------------------------------------------------------------

### Content Security Policy (CSP)  
https://www.geeksforgeeks.org/flask-security-with-talisman/
https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html

Superset uses the [Talisman](https://pypi.org/project/flask-talisman/) extension to enable implementation of a
[Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), an added
layer of security that helps to detect and mitigate certain types of attacks, including
Cross-Site Scripting (XSS) and data injection attacks.

A CSP makes it possible for server administrators to reduce or eliminate the vectors by which XSS can
occur by specifying the domains that the browser should consider to be valid sources of executable scripts.
A CSP-compatible browser will then only execute scripts loaded in source files received from those allowed domains,
ignoring all other scripts (including inline scripts and event-handling HTML attributes).

A policy is described using a series of policy directives, each of which describes the policy for
a certain resource type or policy area. You can check possible directives
[here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy).

It's extremely important to correctly configure a Content Security Policy when deploying Superset to
prevent many types of attacks. Superset provides two variables in `config.py` for deploying a CSP:

- `TALISMAN_ENABLED` defaults to `True`; set this to `False` in order to disable CSP
- `TALISMAN_CONFIG` holds the actual the policy definition (*see example below*) as well as any
other arguments to be passed to Talisman.

When running in production mode, Superset will check at startup for the presence
of a CSP. If one is not found, it will issue a warning with the security risks. For environments
where CSP policies are defined outside of Superset using other software, administrators can disable
this warning using the `CONTENT_SECURITY_POLICY_WARNING` key in `config.py`.

#### CSP Requirements

* Superset needs the `style-src unsafe-inline` CSP directive in order to operate.

  ```
  style-src 'self' 'unsafe-inline'
  ```

* Only scripts marked with a [nonce](https://content-security-policy.com/nonce/) can be loaded and executed.
Nonce is a random string automatically generated by Talisman on each page load.
You can get current nonce value by calling jinja macro `csp_nonce()`.

  ```
  <script nonce="{{ csp_nonce() }}">
  /* my script */
  </script>
  ```

- Some dashboards load images using data URIs and require `data:` in their `img-src`

  ```
  img-src 'self' data:
  ```

- MapBox charts use workers and need to connect to MapBox servers in addition to the Superset origin

  ```
  worker-src 'self' blob:
  connect-src 'self' https://api.mapbox.com https://events.mapbox.com
  ```

* Other CSP directives default to `'self'` to limit content to the same origin as the Superset server.

In order to adjust provided CSP configuration to your needs, follow the instructions and examples provided in
[Content Security Policy Reference](https://content-security-policy.com/)


#### Other Talisman security considerations

Setting `TALISMAN_ENABLED = True` will invoke Talisman's protection with its default arguments,
of which `content_security_policy` is only one. Those can be found in the
[Talisman documentation](https://pypi.org/project/flask-talisman/) under _Options_.
These generally improve security, but administrators should be aware of their existence.

In particular, the option of `force_https = True` (`False` by default) may break Superset's Alerts & Reports
if workers are configured to access charts via a `WEBDRIVER_BASEURL` beginning
with `http://`.  As long as a Superset deployment enforces https upstream, e.g.,
through a load balancer or application gateway, it should be acceptable to keep this
option disabled. Otherwise, you may want to enable `force_https` like this:

```python
TALISMAN_CONFIG = {
    "force_https": True,
    "content_security_policy": { ...
```

----------------------------------------------------------------------------------------------------------------------------------------------