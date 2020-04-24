var config = require('./webpack.config.js')
var WebpackBundleTracker = require('webpack-bundle-tracker')

config.mode = 'production'
config.plugins = [
  new WebpackBundleTracker({filename: './webpack-stats-prod.json'}),
]
module.exports = config
