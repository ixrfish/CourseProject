import React, { Component, useEffect } from 'react';

class EaterResult extends Component {
    constructor(props) {
        super(props);
        fetch('/parse/regex/pyap$url=' + this.props.url).then(res => res.json()).then(data => {
          this.setState({regex: data});
        });
    }

    render() {
        return (
            <div>
                <p> {this.props.url} </p>
                <p> {this.state.regexResult} </p>
            </div>
        );
    }

}
export default EaterResult;