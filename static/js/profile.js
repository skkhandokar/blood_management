
var a=1;
function show()
{
   if (a==0)
   {
   //  document.getElementById("blood_info").style.display="inline";
    myheading=document.getElementById("show");
    myheading.innerHTML="Close Full Information";
    return a=1;
   }
   else
   {
 //  document.getElementById("blood_info").style.display="none";``````````````````````````````````````````````````
    myheading=document.getElementById("show");
    myheading.innerHTML="close Full Information";
    return a=0;
   }
}

function toggle_visibility(id) {
   var e = document.getElementById(id);
   if(e.style.display == 'block')
     e.style.display = 'none';
     
   else
     e.style.display = 'block';
 }

// function sho2()
// {
//    document.getElementById('blood_info').style.display="block"
//    document.getElementById('show').style.display="none"
// }

// function hide()
// {
//    document.getElementById('blood_info').style.height="0px"
//    document.getElementById('blood_info').style.display="none"
//    document.getElementById('show').style.display="inline"
// }