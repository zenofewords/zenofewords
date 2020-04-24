var path = require('path')
var MiniCssExtractPlugin = require('mini-css-extract-plugin')
var TerserPlugin = require('terser-webpack-plugin')
var WebpackBundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: {
    main: './static/javascript/main',
  },
  output: {
    filename: '[name]_[hash].js',
    path: path.resolve(__dirname, 'staticfiles/bundles'),
    publicPath: 'http://localhost:8080/static/bundles/',
  },
  devtool: 'inline-source-map',
  devServer: {
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
    compress: true,
    hot: true,
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          }
        },
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: 'css-loader',
          },
          {
            loader: 'sass-loader',
            options: {
              implementation: require('sass'),
            }
          },
        ]
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
          },
        ]
      },
    ]
  },
  plugins: [
    new WebpackBundleTracker({
      filename: './webpack-stats.json'
    }),
    new MiniCssExtractPlugin({
      filename: '[name]_[hash].css',
    }),
  ],
  optimization: {
    minimizer: [new TerserPlugin()],
  },
  mode: 'development',
}
