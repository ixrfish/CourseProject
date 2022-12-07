import React, { Component } from 'react';

export default class EaterResult extends Component {
    constructor(props) {
        super(props);
        this.state = {}
        this.updateAndNotify();
    }

    componentDidUpdate(prevProps) {
      if (prevProps.text !== this.props.text) {
        this.updateAndNotify();
      }
    }

    updateAndNotify = () => {
        fetch('/parse/regex/pyap$url=' + encodeURIComponent(this.props.url))
            .then((response) => {
                return response.json();
             })
            .then(data => {
                this.setState({ pyapResult: data});
            });

        fetch('/parse/regex/commonregex$url=' + encodeURIComponent(this.props.url))
            .then((response) => {
                return response.json();
             })
            .then(data => {
                this.setState({ commonregexResult: data});
            });

        fetch('/parse/nlp/spacy$url=' + encodeURIComponent(this.props.url))
            .then((response) => {
                return response.json();
             })
            .then(data => {
                this.setState({ spacyResult: data});
            });

        fetch('/parse/crawler$url=' + encodeURIComponent(this.props.url))
            .then((response) => {
                return response.json();
             })
            .then(data => {
                this.setState({ crawlerResult: data});
            });
    }

    mapAddress(result, type) {
        if (result != null) return result.map(address => <td key={type+"_"+address}> {address} </td>) ;
    }

    convertToArray(result) {
        if (result != null) {
            let vals = Object.values(result);
            vals.sort();
            return vals;
        }
    }

    getCount(result) {
        if (result != null) {
            return result.length;
        }
    }

    getOverlap(groundTruth, toCompare) {
        if (groundTruth != null && toCompare != null) {
            let count = groundTruth.map(groundTruthElement => {
                return toCompare.filter(toCompareElement => {
                    if (groundTruthElement.includes(toCompareElement.trim())) {
                        return true;
                    }
                }).length
            }).filter(ele => ele > 0);
            return count.length;
        }
    }

    getPrecision(groundTruth, toCompare) {
        let overlap = this.getOverlap(groundTruth, toCompare);
        let groundTruthCount = this.getCount(groundTruth);

        return overlap / groundTruthCount;
    }

    render() {
        return (
            <div>
                <p> URL: { this.props.url } </p>
                <table>
                    <thead>
                        <tr>
                            <th> type </th>
                            <th> result count </th>
                            <th> overlap count </th>
                            <th> precision </th>
                            <th> addresses </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th> crawler </th>
                            <th> { this.getCount(this.convertToArray(this.state.crawlerResult)) } </th>
                            <th> { this.getOverlap(this.convertToArray(this.state.crawlerResult), this.convertToArray(this.state.crawlerResult)) } </th>
                            <th> { this.getPrecision(this.convertToArray(this.state.crawlerResult), this.convertToArray(this.state.crawlerResult)) } </th>
                            { this.mapAddress(this.convertToArray(this.state.crawlerResult), "crawler") }
                        </tr>
                        <tr>
                            <th> pyap </th>
                            <th> { this.getCount(this.state.pyapResult) } </th>
                            <th> { this.getOverlap(this.convertToArray(this.state.crawlerResult), this.state.pyapResult) } </th>
                            <th> { this.getPrecision(this.convertToArray(this.state.crawlerResult), this.state.pyapResult) } </th>
                            { this.mapAddress(this.state.pyapResult, "pyap") }
                        </tr>
                        <tr>
                            <th> commonregex </th>
                            <th> { this.getCount(this.state.commonregexResult) } </th>
                            <th> { this.getOverlap(this.convertToArray(this.state.crawlerResult), this.state.commonregexResult) } </th>
                            <th> { this.getPrecision(this.convertToArray(this.state.crawlerResult), this.state.commonregexResult) } </th>
                            { this.mapAddress(this.state.commonregexResult, "commonregex") }
                        </tr>
                        <tr>
                            <th> spacy </th>
                            <th> { this.getCount(this.state.spacyResult) } </th>
                            <th> { this.getOverlap(this.convertToArray(this.state.crawlerResult), this.state.spacyResult) } </th>
                            <th> { this.getPrecision(this.convertToArray(this.state.crawlerResult), this.state.spacyResult) } </th>
                            { this.mapAddress(this.state.spacyResult, "spacy") }
                        </tr>
                    </tbody>
                </table>
            </div>
        );
    }
}
