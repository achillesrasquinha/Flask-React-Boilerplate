import React from "react";
import { connect } from "react-redux";

import Routes from "../Routes";

class App extends React.Component {
    render ( ) {
        return (
            <div>
                <Routes></Routes>
            </div>
        )
    }
};

const mapStateToProps    = state    => ({

});
const mapDispatchToProps = dispatch => ({

});

export default connect(mapStateToProps, mapDispatchToProps)(App);