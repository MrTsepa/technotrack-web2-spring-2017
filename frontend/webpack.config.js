const webpack = require('webpack');
const BundleTracker  = require('webpack-bundle-tracker');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const NODE_ENV = process.env.NODE_ENV || 'development';

module.exports = {
    entry: [
        // 'webpack-dev-server/client?http://localhost:3000',
        // 'webpack/hot/only-dev-server',
        './index.jsx'
    ],
    context: `${__dirname}/static_src`,
    output: {
        path: `${__dirname}/static/build/`,
        filename: 'indexBundle-[hash].js',
        publicPath: 'static/build/',
    },
    watch: true,
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                include: `${__dirname}/static_src`,
                loaders: [
                    // 'react-hot-loader',
                    'babel-loader?presets[]=react&presets[]=es2015&presets[]=stage-1',
                ]
            },
            {
                test: /\.scss$/,
                use: [
                    { loader: 'style-loader' },
                    { loader: 'css-loader' },
                    {
                        loader: 'sass-loader',
                        options: {
                            includePaths: [
                                './node_modules',
                            ]
                        }
                    }
                ]
            },
        ]
    },
    plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
        // new webpack.optimize.UglifyJsPlugin({
        //     compress: {
        //         warnings: false,
        //         unsafe: true
        //     }
        // }),
        // new webpack.HotModuleReplacementPlugin(),
        new BundleTracker({ filename: './webpack-stats.json'})
    ]
};
