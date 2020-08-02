import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {
  constructor() {
    super();
    this.state = {
      isPredicted:false,
      stopSignPrediction:0,
      input:false,
      showAlert:false,
      alertText:"",
      data: [],
    };
  }

  inputMethod = () => {
    let i = !this.state.input;
    this.setState({input:i});
  }

  uploadHandler = (event) => {
    console.log(event.target.files[0])
    const data = new FormData()
    data.append('file', event.target.files[0])
    console.log(data)
    axios.post("/predict_upload", data, {
         // receive two    parameter endpoint url ,form data
    }).then(res => { // then print response status
      console.log(res)
      console.log(res.data)
      var data = res.data
      this.setState({stopSignPrediction: data, isPredicted: true})
      this.setState({alertText:String(this.stopSignPrediction)})
 })
}

render(){
  return (
    <div className="App">

      <div className="HeaderImage">
      </div>
      <div className="Intro">
        <p>Detect stop sign images using deep learning.</p>
        <p class="Alert">
        {this.state.isPredicted ? String("Prediction complete: "+ this.state.stopSignPrediction) : null}
        </p>
        <input className="Input" type="file" name="file" onChange={this.uploadHandler}/></div>
    </div>
      );
    }
}

export default App;
