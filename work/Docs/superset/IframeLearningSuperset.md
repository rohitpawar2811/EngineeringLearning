## IFrame In Superset

A message channel is created using the MessageChannel() constructor. Once created, the two ports of the channel can be accessed through the MessageChannel.port1 and MessageChannel.port2 properties (which both return MessagePort objects.) The app that created the channel uses port1, and the app at the other end of the port uses port2 — you send a message to port2, and transfer the port over to the other browsing context using window.postMessage along with two arguments (the message to send, and the object to transfer ownership of, in this case the port itself.)

When these transferable objects are transferred, they are no longer usable on the context they previously belonged to. A port, after it is sent, can no longer be used by the original context.

The other browsing context can listen for the message using onmessage, and grab the contents of the message using the event's data attribute. You could then respond by sending a message back to the original document using MessagePort.postMessage.

When you want to stop sending messages down the channel, you can invoke MessagePort.close to close the ports.

Find out more about how to use this API in Using channel messaging.

https://developer.mozilla.org/en-US/docs/Web/API/Channel_Messaging_API
https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API

https://medium.com/@huamichaelchen/end-to-end-example-of-setting-up-superset-embedded-dashboard-f72fc985559

There is another way of embedding the superset Dashboard by making customUserAuthorizer and 
https://www.tetranyde.com/blog/embedding-superset


$(document).on('click', '.dt-is-filter', function() {
    // Get the URL from the clicked element
    var id = $(this).text(); // Assuming the URL is the text content of the element
    var redirectUri = "https://ebike-uat.hotwax.io/commerce/findOrder/" + id;
    // Open the URL in a new tab
    window.open(redirectUri, '_blank');
});

https://stackoverflow.com/questions/3690812/capture-click-on-div-surrounding-an-iframe