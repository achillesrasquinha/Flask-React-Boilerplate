import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";

import app   from "./containers/App/reducer";
import modal from "./components/Modal/reducer";

export default combineReducers({
    router: routerReducer,
    app, modal
})