#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"

print """

<html>
 <head>
      <meta charset="utf-8" >
      <meta name="viewport" content="width=device-width, initial-scale=1" />
		<link href="css/bootstrap.min.css" rel="stylesheet"/>
		<link rel="css/stylesheet" href="animate.css" />
		<link rel="css/stylesheet" href="hover.css" />
		<script src="js/jquery-3.3.1.slim.min.js" ></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js" ></script>
		<script src="js/wow.js"></script>
        <link rel="stylesheet" href="  https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css " />
<!--enternal css--> 
 <style>
  .active{
   background-color:grey;
   border-radius:20px;
   }
   .active:hover
   {
    background:green;
   }
   .menu:hover
   {
    background-color:orange;
    border-radius:20px;
    }
 </style>
<!--//Enternal css end-->
</head>
<body>
   <div class="container-fluid">
  <div class="row">
    <div class="col-sm-1 bg-light p-0" >
    <img src="image/news.jpg" style="height:30px;width:120px"/>
    </div>
      <div class="col-sm-11 bg-light ">
       <marquee style="" scrollamount="20" scrolldelay="5" direction="left" onmouseover="this.stop()" onmouseout="this.start()">
       <a href="#" style="color:red">This is news of online library |</a> &nbsp;
       <a href="#" style="color:red">This is news books are aviable in library |</a> &nbsp;
       <a href="#" style="color:red">This is new you can read for knowladge |</a> &nbsp;
       <a href="#" style="color:red">Information Technology! Computer Science! Electric Books aviable |</a>
       </marquee>
      </div>
 </div>

<div class="row bg-info">
<div class="col-sm-4">
<i class="fa fa-institution fa-3x " style="color:white;"></i>
</div>
<div class="col-sm-4 h1" style="color:white">Online Library</div>
<div class="col-sm-4"></div>
</div> 
   <div class="row" >
<div class="col-sm-12 navbar navbar-expand-sm navbar-light bg-success ">
 
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link menu text-white" href="home.py" style="color:black;font-size:25px;">Home </a>&nbsp;&nbsp;
      <a class="nav-item active nav-link menu text-white" href="about.py" style="color:black;font-size:25px;">About</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="services.py" style="color:black;font-size:25px;">Services</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="digi.py" style="color:black;font-size:25px;">Book Gallary</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="Registration.py" style="color:black;font-size:25px;">Registration</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="login.py" style="color:black;font-size:25px;"> Admin Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="userlogin.py" style="color:black;font-size:25px;"> User Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="contact.py" style="color:black;font-size:25px;">Contact</a>&nbsp;&nbsp;
    
    </div>
  </div>
  </div>

   <div class="container-fluid">
     <div class="row bg-secondary" style="text-align:center;font-size:35px">
      <div class="col-sm-12 h1" STYLE="COLOR:YELLOW">
     ABOUT US
     </div>
   </div>
    
    <!--about us-->
     <div class="row bg-primary">
      <div class="col-sm-6" style="text-align:center">
      <h1 style="color:yellow">About us</h1>
     <p style="color:white"> The library is far more than just a place full of books-although we do have millions of print and digital resources for you to 
     explore! Our diverse staff are skilled in the areas of digital literacy, research support, innovation and much more. No matter which campus you're on, you can find expert 
     guidance and advice at our servie  desk or through our  Library Chat service.
     
     
      </div>
       <div class="col-sm-6 p-3" style="text-align:center">
       <img src="image/about.jpg" class="rounded-circle img-fluid" alt="First library image" style="height:200px;width:210px">
       </div>
       </div>
     <!--//about us-->
     
     <!--Our vision-->
     <div class="row bg-info">
     <div class="col-sm-6" style="text-align:center">
     <h1 style="color:yellow">Our Vision</h1>
          
     <p style="color:white;">
       The online library perspective to equip of their students and faculity with the knowladge, skill, scholorship and 
       to meet the challenges and demads of globalization. To realze its parent university vision, it is impertive
       that the Global Library and comparable with the best globally. 
     </div>
     <div class="col-sm-6 p-3" style="text-align:center">
     <img src="image/vision.jpg" class="rounded-circle img-fluid" alt="First library image" style="height:200px;width:210px">
     </div>
     </div>
     
     <!--our mission-->
      <div class="row bg-dark">
     <div class="col-sm-6" style="text-align:center">
     <h1 style="color:yellow">Our mission</h1>
       <p style="color:white">
         The mission of the online Library is to provide support for teaching and research and outreach program of the University by 
         providing access to up-to-date globle sources of information and learning resourse though state-of-art technology and services. The library 
         aspires to meet the challenge of providing global up-to-date information to local users and local information to global users.
       </div>
     <div class="col-sm-6 p-3" style="text-align:center">
     <img src="image/mission.jpg" class="rounded-circle img-fluid" alt="First library image" style="height:200px;width:210px">
     </div>
     </div>
     
   <!--our mission-->
<!--footer content-->
<div class="row  bg-success" style="text-align:center;color:white">
<div class="col-sm-3">
<h3>About Us :</h3>
This is online Library
here you can read more books and 
download in pdf and purchase for limited 
time.
</div>
<div class="col-sm-3">
<h3>Important Links :<h3>
<a href="home.py">Home</a><br/>
<a href="about.py">About us</a><br/>
<a href="service.py">Services</a><br/>
<a href="contact.py">Contact</a><br/>
</div>
<div class="col-sm-3" style="text-align:left">
<h3>Conatct :</h3>
 <i class="fa fa-globe" style="color:skyblue;font-size:22px"></i> <a href="#">&nbsp;&nbsp;www.onlinelibrary.com</a><br/><br/>
   
   <i class="fa fa-phone" style="color:skyblue;font-size:22px"></i>&nbsp; <b>7355651198</b><br/><br/>
    <i class="fa fa-envelope-o" style="color:skyblue;font-size:22px" ></i>&nbsp;&nbsp;santoshkumarsy05@gmial.com<br/></br><br/>
   
</div>
<div class="col-sm-3">
<h3>Follow Us</h3>
<table>
   
     <td styele="height:">
   <a href="https://www.facebook.com/" target="blank"> <i class="fa fa-facebook-square" style="color:blue;font-size:45px;"></i></a>
   </td>
   <td styele="height:">
   &nbsp;&nbsp;&nbsp;<a href="https://twitter.com/" target="black"> <i class="fa fa-twitter-square" style="color:skyblue;font-size:45px;"></i></a>
   </td>
   <td styele="height:">
   &nbsp;&nbsp;&nbsp; <a href="https://www.whatsapp.com/" target="blank"><i class="fa fa-whatsapp" style="color:green;font-size:45px;"></i></a>
   </td><br/><br/>
   <td styele="height:">
   &nbsp;&nbsp;&nbsp; <a href="https://www.instagram.com/" target="blank"><i class="fa fa-instagram" style="color:orange;font-size:45px;"></i></a>
   </td>
   
   <td styele="height:">
   &nbsp;&nbsp;&nbsp; <a href="https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faboutme.google.com%2Fu%2F0%2F%3Freferer%3Dgplus&followup=https%3A%2F%2Faboutme.google.com%2Fu%2F0%2F%3Freferer%3Dgplus&flowName=GlifWebSignIn&flowEntry=ServiceLogin" target="blank"><i class="fa fa-google-plus-square" style="color:red;font-size:45px;"></i></a>
   </td>
   </tr>
   </table>
</div>
</div>

<!--copyright content-->
<div class="row bg-info" style="color:white">
<div class="col-sm-6">
Copyright &copy; 2019 online library
</div>
<div class="col-sm-6" style="text-align:Center">
Developed by :-Santosh kumar yadav (Information Technology)
</div>
</div>
<!--//copyright content-->   
 </div>     
     </div>
   </body>
</html>"""
