fetch("http://127.0.0.1:5000/test2")
.then(resp => resp.json())
.then(data => console.log(data))