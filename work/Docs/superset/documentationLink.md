## Superset Link Configuration:

In Superset, links can be incorporated into charts, enabling redirection from the Dashboard page. There are two primary methods to configure this:

1. Using Raw Records Section in Charts:
   - Navigate to the columns section and select "Add Column."
   - Upon clicking, you'll encounter a model with three sections: saved-columns, columns, and SQL Query.
   - A tab will open; click on the SQL Query option and paste the following link:

    ```sql
    CONCAT('<a href="',
           CONCAT("https://qa-oms.hotwax.io/commerce/control/ViewFacility?facilityId=", facility_id)
           ,'" target="_blank">', facility_id, '</a>')
    ```

   - Afterward, you can edit the header, which serves as the label for your column.

2. Using Aggregates Section in Charts:
   - Configure the above process in the matrix section.
   - Upon clicking, you'll encounter a model with three sections: saved-columns, columns, and SQL Query.
   - Select SQL Query and paste the link, then simply edit the header which serves as the label for your column .

After completing these steps, your configuration is ready for use. Just click on Update and test.

### Difference Between Both Methods:

In the first method, Jinja templating cannot be utilized in the Query part, necessitating the use of a hard-coded link. However, the second method allows for Jinja templating. Example:

```sql
CONCAT('<a href="',
       CONCAT("https://{{instance_name}}/commerce/control/ViewFacility?facilityId=", facility_id)
       ,'" target="_blank">', facility_id, '</a>')
```

## Details about the CONCAT Function

Description: Concatenates strings to form an HTML anchor (<a>) tag.

Usage:
CONCAT('<a href="',
       CONCAT("https://{{instance_name}}/commerce/control/ViewFacility?facilityId=", facility_id),
       '" target="_blank">', facility_id, '</a>')

Parameters:
- <a href=": Static part of the anchor tag indicating the start of a hyperlink.
- CONCAT("https://{{instance_name}}/commerce/control/ViewFacility?facilityId=", facility_id): Dynamically generates a URL by concatenating a static URL template with the facility_id. here facility_id is a column name which is included in link.
- '" target="_blank">: Static part of the anchor tag specifying that the link should open in a new tab or window.
- facility_id: Value inserted into the anchor tag as visible text.
- </a>: Static part of the anchor tag indicating the end of the hyperlink.

Return Value: 
Concatenated string representing an HTML anchor tag.

Purpose: 
To generate HTML code for creating a hyperlink dynamically based on the facility_id.
