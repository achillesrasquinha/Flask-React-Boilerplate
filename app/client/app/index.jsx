import "../scss/App.scss";

import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { ConnectedRouter } from "react-router-redux";
import { IntlProvider } from "react-intl";

import { store, history } from "./store";
import App from "./containers/App";


const element 	  = document.getElementById("app");

const render  	  = (App, HotAppContainer = null) => {
	let provider  = (
		<Provider store={store}>
			<IntlProvider locale="en">
				<ConnectedRouter history={history}>
					<App />
				</ConnectedRouter>
			</IntlProvider>
		</Provider>
	);

	if ( HotAppContainer ) {
		provider = (
			<HotAppContainer>
				{provider}
			</HotAppContainer>
		);
	}

	ReactDOM.render(provider, element);
};

render(App);

if ( module.hot ) {
	import("react-hot-loader").then(({ AppContainer }) => (
		module.hot.accept("./containers/App", () => {
			const App = require("./containers/App").default;
			render(App, AppContainer);
		})
	))
}