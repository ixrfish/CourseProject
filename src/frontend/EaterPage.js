import './EaterPage.css';
import React, { Component } from 'react';
import { useNavigate } from 'react-router-dom';
import EaterResult from './EaterResult.js'

class EaterPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            url: '',
            viewResult: false
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({ url: event.target.value });
    }

    handleSubmit(event) {
        alert('An Url was submitted: \n' + this.state.url + "\nScroll down to see result");
        event.preventDefault();

        this.setState({ viewResult: true });
    }

    render() {
        return (
            <div>
            <div className="EaterPage">
                <header className="EaterPage-header">
                    <form onSubmit={this.handleSubmit}>
                    <label>
                    Please enter an Eater url in the box below:
                    <br />
                    <input
                        type="text"
                        name="url"
                        value={this.state.value}
                        onChange={this.handleChange} />
                    </label>
                    <br />
                    <input type="submit" value="Submit" />
                    </form>
                </header>
            </div>
            <div className="EaterPage">
                { (this.state.viewResult) ? (<EaterResult url={this.state.url} />) : "" }
            </div>
            </div>
        );
    }
}

function EaterPageWithNavigate(props) {
    let navigate = useNavigate();
    return <EaterPage {...props} navigate={navigate} />
}

export default EaterPageWithNavigate;
