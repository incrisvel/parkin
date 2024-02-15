const copy =
  "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url =
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, {
  attribution: copy,
});

const map = L.map("map", {
  layers: [layer],
});

const cidadeLatitude =  -26.9187;
const cidadeLongitude =  -49.0660;

const teatroLatitude = -26.9185;
const teatroLongitude =  -49.0680;

map.setView([cidadeLatitude, cidadeLongitude], 17); 


L.marker([teatroLatitude, teatroLongitude]).addTo(map)
  .bindPopup("Sua localização atual");