const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const WebpackBundleTracker = require('webpack-bundle-tracker')

module.exports = {
  mode: 'development',
  entry: {
    base: './static/javascript/base',
    pages: './static/javascript/pages',
    home: './static/javascript/home',
    queries: './static/javascript/queries',
  },
  output: {
    filename: '[name]_[contenthash].js',
    path: path.resolve(__dirname, 'staticfiles/bundles'),
    publicPath: 'http://localhost:8080/static/bundles/',
  },
  devtool: 'eval-source-map',
  devServer: {
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
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader',
        ]
      },
    ]
  },
  plugins: [
    new WebpackBundleTracker({
      filename: './webpack-stats.json',
    }),
    new MiniCssExtractPlugin({
      filename: '[name]_[contenthash].css',
    }),
  ],
}
