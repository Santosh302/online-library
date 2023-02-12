#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"

print"""
<html>
 <head>
 
 <meta charset="utf-8" >
<meta name="viewport" content="width=device-width, initial-scale=1" />
		<link href="css/bootstrap.min.css" rel="stylesheet"/>
		<link rel="stylesheet" href="css/animate.css" />
		<link rel="stylesheet" href="css/hover.css" />
		<script src="js/jquery-3.3.1.slim.min.js" ></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js" ></script>
		<script src="js/wow.js"></script>
		 <link rel="stylesheet" href="css/font-awesome.css"/>
         <link rel="stylesheet" type="text/css" href="css/icone-effect.css">

<script>
wow = new WOW(
                      {
                      boxClass:     'wow',      // default
                      animateClass: 'animated', // default
                      offset:       0,          // default
                      mobile:       true,       // default
                      live:         true        // default
                    }
                    );
                    wow.init();
</script>
 <style>
 .carousel-item img
    	{
    		height: 400px;
    	}
  .menu:hover{
  background-color:orange;
  border-radius:20px;
  }
  .banner a{
  color:white;
  text-decoration:none;
  }
 .active{
background-color:grey;
border-radius:20px;
}
.back{
 background:transparent;
 background:url('image/back1.jpg');
 background-size:100%;
 color:white;
 
}
 </style>
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
      <a class="nav-item nav-link menu text-white " href="home.py" style="color:black;font-size:25px;">Home </a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="about.py" style="color:black;font-size:25px;">About</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="services.py" style="color:black;font-size:25px;">Services</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="digi.py" style="color:black;font-size:25px;">Book Gallary</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="Registration.py" style="color:black;font-size:25px;">Registration</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white active" href="login.py" style="color:black;font-size:25px;"> Admin Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="userlogin.py" style="color:black;font-size:25px;"> User Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="contact.py" style="color:black;font-size:25px;">Contact</a>&nbsp;&nbsp;
    
    </div>
  </div>
  </div>
  </div>
 
<!--login page-->
 
<div class="row back p-0" style="height:440px;">
<div class="col-sm-4"></div>
<div class="col-sm-4 p-4">
<h3 style="color:orange">Admin login :</h3><br/>
<form action="logcode.py" method="post">
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" name="text3">
   
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" name="text4">
  </div>
  <div class="form-group form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
<div class="col-sm-4"></div>
</div>
</div>
</div>
<!--//login in-->
<!--footer content-->
<!--footer content-->
<div class="row p-2 bg-success" style="text-align:center;color:white">
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
<!--//copyright content->    
  
</div>
</html>"""