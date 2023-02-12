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
<!--css external-->
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
<!--css external end-->
 </head>
<body>
<div class="container-fluid">
 <!--Header marquee-->
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
<!--//Header marquee end-->

<!-- second header online library-->
<div class="row bg-info">
  <div class="col-sm-4">
   <i class="fa fa-institution fa-3x " style="color:white;"></i>
  </div>
   <div class="col-sm-4 h1" style="color:white">Online Library</div>
   <div class="col-sm-4"></div>
</div> 
<!--//End of header online library-->
<!--Third header navbar-->
<div class="row" >
  <div class="col-sm-12 navbar navbar-expand-sm navbar-light bg-success ">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target=   "#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label= "Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
      <a class="nav-item nav-link menu text-white active" href="home.py" style="color:black;font-size:25px;">Home </a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="about.py" style="color:black;font-size:25px;">About</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="services.py" style="color:black;font-size:25px;">Services</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="digi.py" style="color:black;font-size:25px;">Book Gallary</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="Registration.py" style="color:black;font-size:25px;">Registration</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="login.py" style="color:black;font-size:25px;"> Admin Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="userlogin.py" style="color:black;font-size:25px;"> User Login</a>&nbsp;&nbsp;
      <a class="nav-item nav-link menu text-white" href="contact.py" style="color:black;font-size:25px;">Contact</a>&nbsp;&nbsp;
      </div>
   </div>
  </div>
</div>
<!--//End of Third header navbar-->
   
<!--sliding Image-->
<div class="row" >
  <div class="col-sm-12 p-0" >
	<div id="carouselExampleIndicators"  height="500px" class="carousel slide" data-ride="carousel">
     <ol class="carousel-indicators">
       <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
       <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
     </ol>
  <div class="carousel-inner">
      <div class="carousel-item active">
       <img src="image/lib1.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="image/lib2.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="image/lib3.jpg" class="d-block w-100" alt="...">
      </div>
	  <div class="carousel-item">
        <img src="image/lib4.jpg" class="d-block w-100" alt="...">
      </div>
	   <div class="carousel-item">
        <img src="image/lib5.jpg" class="d-block w-100" alt="...">
      </div>
    </div>
    <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
  </div>
</div>
<!--//sliding Image end-->

<!--button-->
<div class="row m-4">
  <div class="col-sm-12" >
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
    <a href="pdf/HTML.pdf" download><button style="height:150px;width:200px;background:blue;COLOR:WHITE">DOWNLOAD HTML</button></a>
    &nbsp;&nbsp;&nbsp;
   <a href="pdf/HTML&CSS.pdf" download><button style="height:150px;width:200px;background:red;color:white">DOWNLOAD HTML&CSS</button></a>
   &nbsp;&nbsp;&nbsp;
   <a href="pdf/JAVASCRIPT.pdf" download><button style="height:150px;width:200px;background:pink;color:white">DOWNLOAD JAVASCRIPT</button></a>&nbsp;&nbsp;&nbsp;
   <a href="pdf/BOOTSTRAP.pdf" download> 
   <button style="height:150px;width:200px;background:tan;color:white">DOWNLOAD BOOTSTRAP</button></a>&nbsp;&nbsp;&nbsp;
   <a href="pdf/PYTHON.pdf" download> <button style="height:150px;width:200px;background:skyblue;COLOR:WHITE">DOWNLOAD PYTHON</button>&nbsp;&nbsp;&nbsp; </a><br/><br/>
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
   <a href="pdf/JAVA.pdf" download><button style="height:150px;width:200px;background:blue;COLOR:WHITE">DOWNLOAD JAVA</button></a>
   &nbsp;&nbsp;&nbsp;
  <a href="pdf/C.pdf" download><button style="height:150px;width:200px;background:red;color:white">DOWNLOAD C</button></a>
   &nbsp;&nbsp;&nbsp;
  <a href="pdf/C++.pdf" download> <button style="height:150px;width:200px;background:pink;COLOR:WHITE">DOWNLOAD C++</button></a>&nbsp;&nbsp;&nbsp;
  <a href="pdf/DBMS.pdf" download><button style="height:150px;width:200px;background:black;color:white">DOWNLOAD DBMS</button>&nbsp;&nbsp;&nbsp;
  <a href="pdf/DATASTRUCTURE.pdf" download ><button style="height:150px;width:200px;background:skyblue;COLOR:WHITE"> DATA STRUCTURE</button>&nbsp;&nbsp;&nbsp;</a>
 </div>
</div>
 <!--//button-->

<!-- Section: Testimonials  -->
<section class="text-center my-3 bg-success" >
  <!-- Section heading -->
  <h2 class="h1-responsive font-weight-bold my-5">Feedbacks</h2>
  <div class="wrapper-carousel-fix ">
    <!-- Carousel Wraer -->
    <div id="carousel-example-1" class="carousel no-flex testimonial-carousel slide carousel-fade" data-ride="carousel"data-interval="false">
      <!--Slides-->
      <div class="carousel-inner" role="listbox">
        <!--First slide-->
        <div class="carousel-item active">
          <div class="testimonial">
            <!--images-->
            
              <img src="image/feedback1.jpg" class="rounded-circle img-fluid" alt="First library image" style="height:150px;width:160px">
            <!--Content-->
            <p>
              <i class="fa fa-quote-left"></i>This is library for only purpose to raead books and you can gain more knowledge. This library provid you free registration.After registration you login and access books gallary.Many books are aviable the library 
			  books for study.This library structure is not complecated...
            </p>
            <h4 class="font-weight-bold">Santosh Yadav</h4>
            <h6 class="font-weight-bold my-3">Student of Information Technology</h6>
            <!--Review-->
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star-half-full"> </i>
          </div>
        </div>
        
        
        <!--Second slide-->
        <div class="carousel-item">
          <div class="testimonial">
            <!--Avatar-->
            <div class="avatar mx-auto mb-4">
              <img src="https://mdbootstrap.com/img/Photos/Avatars/img%20(31).jpg" class="rounded-circle img-fluid"
                alt="Second sample avatar image" style="height:150px">
            </div>
            <!--Content-->
            <p>
              <i class="fa fa-quote-left"></i> Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut
              odit
              aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque
              porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia
              non numquam eius modi tempora incidunt ut labore. </p>
            <h4 class="font-weight-bold">Maria Kate</h4>
            <h6 class="font-weight-bold my-3">Professor of Information tecnology(IIMA)</h6>
            <!--Review-->
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
          </div>
        </div>
        <!--Second slide-->
        <!--Third slide-->
        <div class="carousel-item">
          <div class="testimonial">
            <!--Avatar-->
            <div class="avatar mx-auto mb-4">
              <img src="https://mdbootstrap.com/img/Photos/Avatars/img%20(3).jpg" class="rounded-circle img-fluid"
                alt="Third sample avatar image" style="height:150px">
            </div>
            <!--Content-->
            <p>
              <i class="fa fa-quote-left"></i> Duis aute irure dolor in reprehenderit in voluptate velit esse
              cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
              culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus
              error sit voluptatem accusantium doloremque laudantium.</p>
            <h4 class="font-weight-bold">John Doe</h4>
            <h6 class="font-weight-bold my-3">Front-end Developer in NY</h6>
            <!--Review-->
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
            <i class="fa fa-star blue-text"> </i>
          </div>
        </div>
        <!--Third slide-->
        
      </div>
      <!--Slides-->
      <!--Controls-->
      <a class="carousel-control-prev left carousel-control" href="#carousel-example-1" role="button"
        data-slide="prev">
        <span class="icon-prev" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next right carousel-control" href="#carousel-example-1" role="button"
        data-slide="next">
        <span class="icon-next" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
      <!--Controls-->
    </div>
    <!-- Carousel Wrapper -->
  </div>
</section>





<!--footer content-->
<div class="container-fluid" style="margin-top:-16px" >
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
       &nbsp;&nbsp;&nbsp; <a href="https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faboutme.google.com%2Fu%2F0%2F%3Freferer%3Dgplus&followup=https%3A%2F%2Faboutme.google.com%2Fu%2F0%2F%3Freferer%3Dgplus&flowName=GlifWebSignIn&flowEntry=ServiceLogin"><i class="fa     fa-google-plus-square" style="color:red;font-size:45px;"></i></a>
      </td>
     </tr>
    </table>
   </div>
 </div>
</div>
<!-- copyright content-->
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
</body>

</html>"""