function message(){
    fetch('http://127.0.0.1:5000/api/message')
        .then(response => {if (response.ok){
            return response.json();}
        }).then(data => {
            console.log(data);
            document.getElementById("response").innerHTML += data.text;
        }).catch(error => {console.error(error)})
}
