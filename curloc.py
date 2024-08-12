import streamlit as st
from streamlit.components.v1 import html

# HTML and JavaScript to request the user's location
location_script = """
<script>
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else { 
        document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    document.getElementById("location").innerHTML = 
    "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            document.getElementById("location").innerHTML = "User denied the request for Geolocation."
            break;
        case error.POSITION_UNAVAILABLE:
            document.getElementById("location").innerHTML = "Location information is unavailable."
            break;
        case error.TIMEOUT:
            document.getElementById("location").innerHTML = "The request to get user location timed out."
            break;
        case error.UNKNOWN_ERROR:
            document.getElementById("location").innerHTML = "An unknown error occurred."
            break;
    }
}

getLocation();
</script>
<div id="location">Fetching location...</div>
"""

# Display the HTML and JavaScript
st.markdown("## Current Location")
html(location_script, height=100)
