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
const cidadeLongitude =  -49.066;

map.setView([cidadeLatitude, cidadeLongitude], 12); 


L.marker([cidadeLatitude, cidadeLongitude]).addTo(map)
  .bindPopup("Cidade específica"); // V