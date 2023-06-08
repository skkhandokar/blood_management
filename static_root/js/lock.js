

var a;
function passlog()
{
   if (a==0)
   {
    document.getElementById("passwordlog").type="password";
   
    return a=1;
   }
   else
   {
    document.getElementById("passwordlog").type="text";

    return a=0;
   }
}


var p;
function pass()
{
   if (p==0)
   {
    document.getElementById("password").type="password";
    document.getElementById("confirm-password").type="password";
   
    return p=1;
   }
   else
   {
    document.getElementById("password").type="text";
    document.getElementById("confirm-password").type="text";

    return p=0;
   }
}


var c;
function passchange()
{
   if (c==0)
   {
    document.getElementById("id_old_password").type="password";
    document.getElementById("id_new_password1").type="password";
    document.getElementById("id_new_password2").type="password";
   
    return c=1;
   }
   else
   {
    document.getElementById("id_old_password").type="text";
    document.getElementById("id_new_password1").type="text";
    document.getElementById("id_new_password2").type="text";

    return c=0;
   }
}