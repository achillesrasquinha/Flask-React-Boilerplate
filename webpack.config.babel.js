import path from "path";
import webpack from "webpack";

import CleanWebpackPlugin from "clean-webpack-plugin";

import MiniCSSExtractPlugin from "mini-css-extract-plugin";

const DEVELOPMENT = process.env.APP_ENVIRONMENT === "development";

const PATH        = { };
PATH.ROOT         = path.dirname(__filename);
PATH.BASE         = path.join(PATH.ROOT,   "app");

PATH.CLIENT       = path.join(PATH.BASE,   "client");
PATH.SOURCE       = path.join(PATH.CLIENT, "app");

PATH.PUBLIC       = path.join(PATH.BASE,   "public");
PATH.ASSETS       = path.join(PATH.PUBLIC, "assets");

PATH.NODE_MODULES = path.join(PATH.ROOT,   "node_modules");

export default {
    entry: PATH.SOURCE,
    output: {
                 path: path.join(PATH.ASSETS, "js"),
           publicPath: "/assets/js/",
             filename: "bundle.js",
    },
    mode: DEVELOPMENT ? "development" : "production",
    stats: "errors-only",
    devtool: "source-map",
    module: {
        rules: [
            {
                   test: /\.jsx?$/,
                exclude: /node_modules/,
                    use: "babel-loader"
            },
            {
                   test: /\.scss$/,
                    use: [
                        DEVELOPMENT ? "style-loader" : MiniCSSExtractPlugin.loader,
                        "css-loader",
                        "sass-loader"
                    ]
            }
        ]
    },
    plugins: [
        new CleanWebpackPlugin([
            path.join(PATH.ASSETS, "css"),
            path.join(PATH.ASSETS, "js"),
        ]),
        DEVELOPMENT && new webpack.HotModuleReplacementPlugin(),
        new MiniCSSExtractPlugin({
            filename: path.join("../css", DEVELOPMENT ? "styles.css" : "styles.[hash].min.css")
        })
    ].filter(Boolean),
    resolve: {
        modules: [
            PATH.NODE_MODULES
        ],
        extensions: [".js", ".jsx", ".scss"]
    }
}