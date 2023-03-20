// BAR
$(function() 
{
    $('#barbtn').on('click', function() 
    {
        document.getElementById('barbtn').disabled = true;

        let myYear = document.getElementById("year").options[document.getElementById("year").selectedIndex].value;
        let myClass = document.getElementById("class").options[document.getElementById("class").selectedIndex].value;
        let myGender = document.getElementById("gender").options[document.getElementById("gender").selectedIndex].value;
        let myLocation = document.getElementById("location").options[document.getElementById("location").selectedIndex].value;
        $.getJSON('/background_process_bar',
        {
            year:myYear,
            class:myClass,
            gender:myGender,
            location:myLocation
        },function(data)
        {
            if (data.res == true)
            {
                let myRow = document.getElementById('resRow');
                myRow.removeAttribute("hidden");
                let myImg = document.getElementById('resImage');
                myImg.removeAttribute("hidden");
                //myImg.src = "/static/generatedGraphic/" + data.path + ".png";
                let myDLbtn = document.getElementById('downloadBAR');
                //myDLbtn.href ="/static/generatedGraphic/" + data.path + ".png";

                console.log("SCRAP TIME: "+data.scrap_time);
                console.log("GRAPH TIME: "+data.graphic_time);
                console.log("IMAGE TIME: "+data.image_time);

                document.getElementById('barbtn').disabled = false;
            }
            else
            {
                alert("Une erreur est parvenue lors de la création de votre graphique");
                document.getElementById('barbtn').disabled = false;
            }
        })
        return false;
    });
});

// PIE
$(function() 
{
    $('#piebtn').on('click', function() 
    {
        document.getElementById('piebtn').disabled = true;

        let myYear = document.getElementById("year").options[document.getElementById("year").selectedIndex].value;
        let myClass = document.getElementById("class").options[document.getElementById("class").selectedIndex].value;
        let myLocation = document.getElementById("location").options[document.getElementById("location").selectedIndex].value;
        let mySpe = document.getElementById("spe").options[document.getElementById("spe").selectedIndex].value;
        $.getJSON('/background_process_pie',
        {
            year:myYear,
            class:myClass,
            location:myLocation,
            spe:mySpe
        },function(data)
        {
            if (data.res == true)
            {
                let myRow = document.getElementById('resRow');
                myRow.removeAttribute("hidden");
                let myImg = document.getElementById('resImage');
                myImg.removeAttribute("hidden");
                //myImg.src = __dirname + "static/generatedGraphic/" + data.path + ".png";
                let myDLbtn = document.getElementById('downloadPIE');
                //myDLbtn.href = __dirname + "static/generatedGraphic/" + data.path + ".png";

                console.log("SCRAP TIME: "+data.scrap_time);
                console.log("GRAPH TIME: "+data.graphic_time);
                console.log("IMAGE TIME: "+data.image_time);

                document.getElementById('piebtn').disabled = false;
            }
            else
            {
                alert("Une erreur est parvenue lors de la création de votre graphique")
                document.getElementById('piebtn').disabled = false;
            }
        })
        return false;
    });
});

// MAP
$(function() 
{
    $('#mapbtn').on('click', function() 
    {
        document.getElementById('mapbtn').disabled = true;

        let myYear = document.getElementById("year").options[document.getElementById("year").selectedIndex].value;
        let myClass = document.getElementById("class").options[document.getElementById("class").selectedIndex].value;
        let mySpe = document.getElementById("spe").options[document.getElementById("spe").selectedIndex].value;
        let myLocation = document.getElementById("location").options[document.getElementById("location").selectedIndex].value;
        $.getJSON('/background_process_map',
        {
            year:myYear,
            class:myClass,
            spe:mySpe,
            location:myLocation
        },function(data)
        {
            if (data.res == true)
            {
                let myRow = document.getElementById('resRow');
                myRow.removeAttribute("hidden");
                let myImg = document.getElementById('resImage');
                myImg.removeAttribute("hidden");
                //myImg.src = __dirname + "static/generatedGraphic/" + data.path + ".png";
                let myDLbtn = document.getElementById('downloadMAP');
                //myDLbtn.href = __dirname + "static/generatedGraphic/" + data.path + ".png";

                console.log("SCRAP TIME: "+data.scrap_time);
                console.log("GRAPH TIME: "+data.graphic_time);
                console.log("IMAGE TIME: "+data.image_time);

                document.getElementById('mapbtn').disabled = false;
            }
            else
            {
                alert("Une erreur est parvenue lors de la création de votre graphique")
                document.getElementById('mapbtn').disabled = false;
            }
        })
        return false;
    });
});