const fs = require('fs');

module.exports = {
  devServer: {
    host: '0.0.0.0',
    port: 8444, 
    https: true,
    key: fs.readFileSync('/opt/gnuhealth/certs/gnuhealthfed.key'),
    cert: fs.readFileSync('/opt/gnuhealth/certs/gnuhealthfed.crt'),
    hotOnly: false,
  },
}
