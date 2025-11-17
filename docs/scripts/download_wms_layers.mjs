import fs from "fs";
import path from "path";

const wmsLayers = [
  // --- EUMETSAT ---
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:rgb_naturalenhncd"],
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:rgb_dust"],
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:h60b"],
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:rdt"],
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:ir108"],
  ["https://view.eumetsat.int/geoserver/wms", "msg_fes:fire"],

  // --- CHIRPS ---
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "pentadal_chirps_rainfall_estimate"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "pentadal_chirps_rainfall_anomaly"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "monthly_chirps_rainfall_estimate"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "monthly_chirps_rainfall_anomaly"],

  // --- TAMSAT ---
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "tamsat_pentadal_rainfall_estimate_rfe"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "tamsat_pentadal_rainfall_anomaly_rfe"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "tamsat_monthly_rainfall_estimate_rfe"],
  ["http://20.56.94.119/gsky/ows/rainfall-estimates", "tamsat_monthly_rainfall_anomaly_rfe"],

  // --- USGS ---
  ["https://dmsdata.cr.usgs.gov/geoserver/fews_chirps_global_pentad_data/chirps_global_pentad_data/wms",
    "chirps_global_pentad_data"],
  ["https://dmsdata.cr.usgs.gov/geoserver/fews_eviirsndvi_africa_pentad_data/eviirsndvi_africa_pentad_data/wms",
    "eviirsndvi_africa_pentad_data"],
  ["https://dmsdata.cr.usgs.gov/geoserver/fews_eviirsndvi_africa_pentad_anom/eviirsndvi_africa_pentad_anom/wms",
    "eviirsndvi_africa_pentad_anom"],

  // --- Dust Forecast ---
  ["http://20.56.94.119/gsky/ows/dust-forecast", "od550_dust"],
  ["http://20.56.94.119/gsky/ows/dust-forecast", "sconc_dust"],
];

// ---------------------------------------------
// 2. Constant GetMap parameters
// ---------------------------------------------
const params = {
  SERVICE: "WMS",
  VERSION: "1.3.0",
  REQUEST: "GetMap",
  FORMAT: "image/png",
  TRANSPARENT: "true",
  STYLES: "",
  TIME: "2025-10-12T15:15:00Z",
  CRS: "EPSG:3857",
  WIDTH: 1281,
  HEIGHT: 996,
  BBOX: "-4554203.020722416,-4917533.4489256255,8081548.881484727,4906985.59447665",
};

const outputDir = path.resolve("docs/public/wms");
fs.mkdirSync(outputDir, { recursive: true });

// Helper function to build URL
const buildGetMapUrl = (baseUrl, layerName) => {
  const query = new URLSearchParams({ ...params, LAYERS: layerName });
  return `${baseUrl}?${query.toString()}`;
};

// ---------------------------------------------
// 3. Download all layers
// ---------------------------------------------
const downloadWmsLayer = async (baseUrl, layerName) => {
  const url = buildGetMapUrl(baseUrl, layerName);
  const safeName = layerName.replace(/[:/]/g, "_") + ".png";
  const filePath = path.join(outputDir, safeName);

  console.log(`Downloading ${layerName}...`);
  console.log(url);

  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const buffer = await res.arrayBuffer();
    fs.writeFileSync(filePath, Buffer.from(buffer));
    console.log(`✅ Saved ${filePath}\n`);
  } catch (err) {
    console.error(`❌ Failed ${layerName}: ${err.message}\n`);
  }
};

// ---------------------------------------------
// 4. Run downloads sequentially
// ---------------------------------------------
(async () => {
  for (const [baseUrl, layerName] of wmsLayers) {
    await downloadWmsLayer(baseUrl, layerName);
  }
})();
