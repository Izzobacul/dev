

var r = new Request("http://api.open-notify.org/iss-now.json")
console.log(access_token)

fetch(r)
.then(response => response.json())
.then(j => {
    var mymap = L.map('mapid').setView([j['iss_position']['latitude'], j['iss_position']['longitude']], 2);
    var marker = L.marker([j['iss_position']['latitude'], j['iss_position']['longitude']]).addTo(mymap);
    L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${access_token}`, {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);
})
