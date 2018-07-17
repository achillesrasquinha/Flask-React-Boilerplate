import createHistory from "history/createBrowserHistory";
import { createStore, applyMiddleware } from "redux";
import { routerMiddleware } from "react-router-redux";

import reducers from "./reducers";

const history     = createHistory();

const middlewares = [
	routerMiddleware(history)
]
const store       = createStore(reducers,
	applyMiddleware(...middlewares)
)

export { store, history };