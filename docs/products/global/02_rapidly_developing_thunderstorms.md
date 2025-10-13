---
outline: deep
---

# Rapidly Developing Thunderstorms

![WMS Layer](/wms/msg_fes_rdt.png)

## Dataset

| **Input**                               |             **Value**              |
| --------------------------------------- | :--------------------------------: |
| **Title**                               |  Rapidly Developing Thunderstorms  |
| **Category**                            |             Satellite              |
| **Subcategory**                         |           Near Realtime            |
| **Layer Type**                          |    Web Map Service – WMS Layer     |
| **Summary**                             | EUMETSAT, Updated every 15 minutes |
| **Published**                           |                 ✅                 |
| **Public**                              |                 ✅                 |
| **Initially Visible on Map by default** |                 ❌                 |
| **Multi-temporal**                      |                 ✅                 |
| **Multi-layer**                         |                 ❌                 |
| **Near realtime**                       |                 ✅                 |
| **Current time method**                 | Latest available date from source  |
| **Auto Update interval in minutes**     |                 15                 |
| **Enable Clipping by shape**            |                 ❌                 |

## Layer

| **Input**                                |            **Value**             |
| ---------------------------------------- | :------------------------------: |
| **Dataset**                              | Rapidly Developing Thunderstorms |
| **Title**                                | Rapidly Developing Thunderstorms |
| **Default**                              |                ✅                |
| **Display Format for DateTime Selector** |        Hour minute:second        |

## WMS GetMap Configuration

| **Input**                    |                **Value**                |
| ---------------------------- | :-------------------------------------: |
| **Base url for WMS**         | https://view.eumetsat.int/geoserver/wms |
| **WMS Version**              |                  1.3.0                  |
| **Pixel Width**              |                   256                   |
| **Pixel Height**             |                   256                   |
| **Transparency**             |                   ✅                    |
| **Spatial Reference System** |                EPSG:3857                |
| **Output Format**            |                   PNG                   |

## WMS Request Layers

| **Input**                    |  **Value**  |
| ---------------------------- | :---------: |
| **WMS Request Layer 1 Name** | msg_fes:rdt |

## WMS GetCapabilities Configuration

| **Input**                          |                      **Value**                      |
| ---------------------------------- | :-------------------------------------------------: |
| **Request Time from capabilities** |                         ✅                          |
| **Get Capabilities URL**           | https://view.eumetsat.int/geoserver/msg_fes/rdt/ows |
| **Get Capabilities Layer Name**    |                         rdt                         |

## More Info

- [Learn More](https://data.eumetsat.int/product/EO:EUM:DAT:0023): Rapidly Developing Thunderstorms is a geostationary meteorological product for nowcasting applications. Using mainly MSG satellite data, it provides information on clouds related to significant convective systems.
