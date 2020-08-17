import {words} from './words.js'

var word_count = 0
var secs = 0
var running = false;

function gen_words(){
    w = []
    for (var i=0; i<230; i++){
        var r = Math.floor(Math.random() * 2999);
        w.push(words[r])
    }
    return(w)
}

var w = gen_words();
var first = document.getElementById("first")
first.innerText = w[0]
var rest = document.getElementById("rest")
rest.innerText = w.slice(1).join(" ")

function update_words(){
    w.shift()
    document.getElementById("first").innerText = w[0]
    document.getElementById("rest").innerText = w.slice(1).join(" ")
    document.getElementById("in").value = ""
}

function check_input(){
    var inp = document.getElementById("in");
    var v = inp.value;
    var l = v.length
    if (v.includes(" ")){
        if (v == w[0] + " "){
            word_count++
        }
        update_words()
    }
    if (v != w[0].slice(0, l)){
        first.style.color = "red";
    }else{
        first.style.color = "black";
    }
    return(v);
}

function time(){
    secs += 0.01
    document.getElementById("time").innerText = secs.toFixed(1)
    if (secs >= 10){
        document.getElementById("score").innerText = word_count
        document.getElementById("score").style.display = 'all';
        clearInterval(t)
    }
}

function update(){
    var v = check_input();
    if (v != ""){
      running = true;
    }
    if (running){
      time();
    }
}

//setInterval(check_input, 100)
var t = setInterval(update, 10)
