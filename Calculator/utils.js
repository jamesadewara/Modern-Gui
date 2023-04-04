const obj = [
    {
        "date" : "35 min ago",
        "expression" : "2 x 5",
        "express" : "10",
    }
]

/*function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}
*/

//usage:
//readTextFile("history.json", function(text){
//    var data = JSON.parse(text);
//    obj.push(dara);
//});


function createHistory(){
    //run a for loop to add the details to the recent element id
    var recents = document.getElementById("recents");
    for (value of obj){
        console.log(value.date)
        var activity = document.createElement("div")
        activity.setAttribute("class", "activity-item d-flex")
        recents.append(activity)

        var activity_lbl = document.createElement("div")
        activity_lbl.setAttribute("class", "activite-label")
        activity_lbl.innerText = value.date
        activity.append(activity_lbl)

        var icon = document.createElement("i")
        icon.setAttribute("class", "bi bi-circle-fill activity-badge text-success align-self-start")
        activity.append(icon)

        var activity_content = document.createElement("div")
        activity_content.setAttribute("class", "activity-content")
        activity_content.innerText = value.expression + " = "
        activity.append(activity_content)

        var link = document.createElement("a")
        link.setAttribute("class", "fw-bold text-dark")
        link.innerText = value.express
        activity_content.append(link)
        
    }
}


createHistory();