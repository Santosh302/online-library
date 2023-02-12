#!c:/python27/python.exe
print "content-type:text/html\r\n\r\n"

import MySQLdb
db=MySQLdb.connect("127.0.0.1","root","","library")
cursor=db.cursor()


sel="select * from registration"
cursor.execute(sel)
data=cursor.fetchall()
print """ <head>
 
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
 background:url('image/back3.jpg');
 background-size:100%;
 color:white;
 </style>
 </head>
<body class="back">
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
      <a class="nav-item nav-link menu text-white active" href="allregistration.py" style="color:black;font-size:25px;">All Registration</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="changepass.py" style="color:black;font-size:25px;">Change Password</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="logoutcode.py" style="color:black;font-size:25px;">Logout</a>&nbsp;&nbsp;
     
    </div>
  </div>
  </div>
  </div>

  <h1>Show data</h1>
   <table border="1">
     <tr>
	 <th>ID</th>
	 <th>Name</th>
	 <th>Mobile</th>
	 <th>Email</th>
	 <th>Password</th>
     <th>gender</th>
	 <th>city</th>
     </tr>"""
for abc in data:
  print"""<tr>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  </tr>"""%(abc[0],abc[1],abc[2],abc[3],abc[4],abc[5],abc[6])
print"""</table>
</body>
</html>"""