l = Math.random() * (85)
t = Math.random() * (85)

xspeed = Math.random() * (0.1-0.05) + 0.05
yspeed = 0.15-xspeed
logo = document.getElementById("logo")
logo.style.filter = "sepia(1000%) contrast(50%) saturate(500%) hue-rotate(" + Math.random() * 360 + "deg)"

function update(){
    logo = document.getElementById("logo")
    l+=xspeed
    t+=yspeed
    var x = false;
    var y = false;
    if (l>85 || l<0){
        xspeed*=-1
        x = true;
        logo.style.filter = "sepia(1000%) contrast(50%) saturate(500%) hue-rotate(" + Math.random() * 360 + "deg)"
    }
    if (t>85 || t<0){
        yspeed*=-1
        y = true;
        logo.style.filter = "sepia(1000%) contrast(50%) saturate(500%) hue-rotate(" + Math.random() * 360 + "deg)"
    }
    if (x && y){
        alert("CORNER!!!")
    }
    logo.style.left = l+'%';
    logo.style.top = t+'%';
}
var s = setInterval(update, 1)