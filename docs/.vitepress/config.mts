import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: 'Climweb',
  description: 'Help to configure climweb instance by adding meteorological products.',
  themeConfig: {
    logo: {
      src: '/wmo-logo.png',
      alt: 'Climweb',
    },
    nav: [
      { text: 'Home', link: '/' },
      {
        text: 'Products',
        link: '/products/global/00_natural_coloured_enhanced_RGB',
        activeMatch: '/products/',
      },
    ],
    sidebar: {
      '/home/': sidebarHome(),
      '/products/': sidebarProducts(),
    },
    socialLinks: [{ icon: 'github', link: 'https://github.com/wmo-raf/climweb' }],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © Climweb',
    },

    search: {
      provider: 'local',
    },
  },
})
function sidebarHome() {
  return [
    {
      text: 'Introduction',
      link: '/00_introduction',
    },
    {
      text: 'Get started',
      link: '/01_getting-started',
    },
  ]
}
function sidebarProducts() {
  return [
    {
      text: 'Products',
      link: '/products/global/00_natural_coloured_enhanced_RGB',
      items: [
        {
          text: 'Global',
          items: [
            {
              text: 'Natural Colour Enhanced RGB',
              link: '/products/global/00_natural_coloured_enhanced_RGB',
            },
            {
              text: 'Precipitation Rate at Ground',
              link: '/products/global/01_precipitation_rate_at_ground',
            },
            {
              text: 'Rapidly Developing Thunderstorms',
              link: '/products/global/02_rapidly_developing_thunderstorms',
            },
            { text: 'Infrared Imagery', link: '/products/global/03_infrared_imagery' },
            { text: 'Active Fire Monitoring', link: '/products/global/04_active_fire_monitoring' },
          ],
        },
        {
          text: 'Dust',
          items: [{ text: 'Dust RGB', link: '/products/dust/01_dust_rgb' }],
        },
        {
          text: 'Rainfall',
          items: [
            {
              text: 'Pentadal Rainfall Estimates - CHIRPS',
              link: '/products/rainfall/01_pentadal_rainfall_estimates_chirps',
            },
            {
              text: 'Pentadal Rainfall Anomalies - CHIRPS',
              link: '/products/rainfall/02_pentadal_rainfall_anomalies_chirps',
            },
            {
              text: 'Monthly Rainfall Estimates - CHIRPS',
              link: '/products/rainfall/03_monthly_rainfall_estimates_chirps',
            },
            {
              text: 'Monthly Rainfall Anomalies - CHIRPS',
              link: '/products/rainfall/04_monthly_rainfall_anomalies_chirps',
            },
            {
              text: 'Pentadal Rainfall Estimates - TAMSAT',
              link: '/products/rainfall/05_pentadal_rainfall_estimates_tamsat',
            },
            {
              text: 'Pentadal Rainfall Anomalies - TAMSAT',
              link: '/products/rainfall/06_pentadal_rainfall_anomalies_tamsat',
            },
            {
              text: 'Monthly Rainfall Estimates - TAMSAT',
              link: '/products/rainfall/07_monthly_rainfall_estimates_tamsat',
            },
            {
              text: 'Monthly Rainfall Anomalies - TAMSAT',
              link: '/products/rainfall/08_monthly_rainfall_anomalies_tamsat',
            },
          ],
        },
        {
          text: 'Precipitation',
          items: [
            {
              text: 'Pentadal Rainfall Estimates - CHIRPS (USGS)',
              link: '/products/precipitation/01_pentadal_rainfall_estimates_chirps_usgs',
            },
          ],
        },
        {
          text: 'Environment',
          items: [
            { text: 'NDVI - Pentadal', link: '/products/environment/01_pentadal_ndvi' },
            {
              text: 'NDVI Anomaly - Pentadal',
              link: '/products/environment/02_pentadal_ndvi_anomaly',
            },
            {
              text: 'Dust Optical Depth Forecast (550nm)',
              link: '/products/environment/03_dust_optical_depth_forecast',
            },
            {
              text: 'Dust Surface Concentration Forecast (µg/m³)',
              link: '/products/environment/04_dust_surface_concentration_forecast',
            },
          ],
        },
        {
          text: 'Alerts',
          items: [
            { text: 'Dust Warning Advisory', link: '/products/alerts/01_dust_warning_advisory' },
          ],
        },
      ],
    },
  ]
}
