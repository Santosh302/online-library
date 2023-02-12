#!c:/python27/python.exe
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
form=cgi.FieldStorage()
id=form.getvalue("id")
print id;
print """
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

 </style>
 </head>
<body>
<div class="container-fluid">

<div class="row bg-info">
<div class="col-sm-4">
<i class="fa fa-institution fa-3x " style="color:white;"></i>
</div>
<div class="col-sm-4 h1" style="color:white">Welcome Admin</div>
<div class="col-sm-4"></div>
</div> 
<div class="row" >
<div class="col-sm-12 navbar navbar-expand-sm navbar-light bg-success ">
 
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div class="navbar-nav">
      <a class="nav-item nav-link menu text-white " href="profile.py" style="color:black;font-size:25px;">Home </a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="allcontact.py" style="color:black;font-size:25px;">All Contact</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="allregistration.py" style="color:black;font-size:25px;">All Registration</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white active" href="changepass.py" style="color:black;font-size:25px;">Change Password</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="logoutcode.py" style="color:black;font-size:25px;">Logout</a>&nbsp;&nbsp;
     
    </div>
  </div>
  </div>
  </div>

   
<!--sliding Image-->
<div class="container">
<div class="row bg-danger" style=color:white>
	<div class="col-sm-3"></div>
	<div class="col-sm-6">
	<h1>Change Password</h1><br>
	<form action="chengepasscode.py" method="post">
	<input type="text" class="form-control" hidden value="%s" name="id" id="exampleInputPassword1" placeholder="Old Password" name="text4">
  <div class="form-group">
    <label for="exampleInputPassword1">Old Password</label>
    <input type="password" class="form-control" name="opass" id="exampleInputPassword1" placeholder="Old Password" name="text4">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">New Password</label>
    <input type="password" class="form-control" name="npass" id="exampleInputPassword1" placeholder="New Password" name="text4">
  </div>
   <div class="form-group">
    <label for="exampleInputPassword1">Confirm Password</label>
    <input type="password" class="form-control" name="cpass" id="exampleInputPassword1" placeholder="Confirm Password" name="text4">
  </div>
  <button type="submit" class="btn btn-primary form-control">Submit</button>
</form>
	</div>
	<div class="col-sm-3"></div>
</div>
 <!--//button-->
<!--//button-->
 <!-- Section: Testimonials  -->

"""%id