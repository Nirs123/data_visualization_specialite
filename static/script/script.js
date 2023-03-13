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
                myImg.src = "data:image/png;base64, "+data.image;

                document.getElementById('barbtn').disabled = false;
            }
            else
            {
                alert("Une erreur est parvenue lors de la création de votre graphique")
            }
        })
        return false;
    });
});