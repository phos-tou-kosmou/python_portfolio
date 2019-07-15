import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import useForceUpdate from 'use-force-update';
import axios from 'axios';
import './App.css';



function App() {
  const [number, typeNumber] = useState([]);
  const [note, openNote] = useState(false);

  const forceUpdate = useForceUpdate();

  function recordInput(e) {
    e.preventDefault(); e.persist();

    let newInput = Object.assign({}, e.target.dataset);
    if(number.length <= 10) typeNumber([...number, parseInt(e.target.innerHTML)]);

    console.log(number)

  }

  function deleteInput() {
    number.pop()
    console.log(number)
    typeNumber(number)
    forceUpdate();
    
  }

  function sendText() {
    console.log(number.join(''))
    axios({
      method: 'post',
      url: 'http://0.0.0.0:5000/api/text',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-type': 'application/json',
      },
      data: {
        'listname': number.join('')
      }
    })
    .then((response) => {
      console.log('this is the response from the python server on a post request of listname ', response);
    })
    .catch((error) => {
      console.log('here is the error on a post request from the python server of listname ', error);
    });    
  }; 

  function openMessage() {
    if(window.confirm("Are you sure? This will delete your current message"))
    return openNote(!note);  
  }

  return (
    <div className="App">
      <div id="phone-background">
        <div id="number-display" className="row">
          {number.map(x => {return <div className="col-xs-12">{x}</div>})}
        </div>
        <div className="btn btn-danger phone-button" onClick={() => deleteInput()}>⬅️</div>
        <div className="btn btn-warning phone-button" onClick={() => openMessage()}>✉️</div>
        {note && 
          <div>
            <textarea cols="15" rows="2"/>
            <div className="btn btn-primary phone-button" >📨</div>
            <div className="btn btn-primary phone-button" >📝</div>
          </div>
        }
        <div id="phone-button-container">
          <div>
            <div className="btn btn-primary phone-button" data-value="1" onClick={recordInput}>1</div>
            <div className="btn btn-primary phone-button" data-value="2" onClick={recordInput}>2</div>
            <div className="btn btn-primary phone-button" data-value="3" onClick={recordInput}>3</div>
          </div>
          <div>
            <div className="btn btn-primary phone-button" data-value="4" onClick={recordInput}>4</div>
            <div className="btn btn-primary phone-button" data-value="5" onClick={recordInput}>
              5
            </div>
            <div className="btn btn-primary phone-button" data-value="6" onClick={recordInput}>
              6
            </div>
          </div>
          <div>
            <div className="btn btn-primary phone-button" data-value="7" onClick={recordInput}>
              7
            </div>
            <div className="btn btn-primary phone-button" data-value="8" onClick={recordInput}>
              8
            </div>
            <div className="btn btn-primary phone-button" data-value="9" onClick={recordInput}>
              9
            </div>
          </div>
          <div>
            <div className="btn btn-success phone-button" onClick={sendText}>
            ☎️
            </div>
            <div className="btn btn-primary phone-button" data-value="0" onClick={recordInput}>
            0
            </div>
            <div className="btn btn-danger phone-button">
            ☎️
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
