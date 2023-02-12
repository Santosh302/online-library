#!C:/python27/python.exe
print "content-type:text/html\r\n\r\n"
import cgi,cgitb
form=cgi.FieldStorage()
id=form.getvalue("id")

print """

<html>
<head>
<link href="css/bootstrap.min.css" rel="stylesheet"/>
		<link rel="stylesheet" href="css/animate.css" />
		<link rel="stylesheet" href="css/hover.css" />
		<script src="js/jquery-3.3.1.slim.min.js" ></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js" ></script>
		<script src="js/wow.js"></script>
		 <link rel="stylesheet" href="css/font-awesome.css"/>

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
 .photo{
 height:200px;
 width:200px;
 padding:10px;
 margin-left:15px;
 }
 .active{
background-color:grey;
border-radius:20px;
}
.active:hover
{
 background:green;
}
  .menu:hover{
  background-color:orange;
  border-radius:20px;
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
      
      <a class="nav-item nav-link active menu text-white" href="logout.py" style="color:black;font-size:25px;">Log Out</a>&nbsp;&nbsp;
     
      &nbsp;&nbsp;
      &nbsp;&nbsp;
     <a class="nav-item nav-link menu text-white" href="userchangepass.py?id=%s" style="color:black;font-size:25px;">Chenge-Password</a>
    </div>
  </div>
  </div>
  </div>
  
  
  
  <!--Header-->
 <div class="row bg-light">
  <div class="col-sm-12 H1" style="text-align:center;COLOR:blue">
     BOOKS FOR STUDY
   </div>
  </div>
<!--//header-->


<!--images GALLARY-->
  <div class="row back p-5">
    <div class="col-sm-12" style="padding-left:70px">
  <a href="pdf/HTML&CSS.pdf" target="_blank"><img src="image/HTMLCOV.jpg" alt="..." class="rounded wow bounce photo"></a>
<a href="pdf/JAVASCRIPT.pdf" target="_blank"><img src="image/JAVASCRIPT.jpg" alt="..." class="rounded-top wow flash photo"></a>
<a href="pdf/BOOTSTRAP.pdf" target="_blank"><img src="image/boot.jpg" alt="..." class="rounded-right wow pulse photo"></a>
<a href="pdf/PYTHON.pdf" target="_blank"><img src="image/python.jpg" alt="..." class="rounded-bottom wow shake photo"></a>
<a href="pdf/JAVA.pdf" target="_blank"><img src="image/java.jpg" alt="..." class="rounded-left wow shake photo"></a>
<a href="pdf/C.pdf" target="_blank"><img src="image/c.jpg" alt="..." class="rounded photo wow tada"></a>
<a href="pdf/cplus.pdf" target="_blank" ><img src="image/cplus.jpg" alt="..." class="rounded-top photo wow wobble"></a>
<a href="pdf/DBMS.pdf" target="blank"><img src="image/dbms.jpg" alt="..." class="rounded-right photo wow bounceIn"></a>
<a href="pdf/DATASTRUCTURE.pdf" target="blank"><img src="image/ds.jpg" alt="..." class="rounded-bottom photo wow bounceIndown"></a>
<a href="pdf/PHP.pdf" target="_blank"><img src="image/php.jpg" alt="..." class="rounded-left photo wow tada"></a>
 <a href="pdf/ASP.NET.pdf" target="_blank"><img src="image/asp.jpg" alt="..." class="rounded-left wow shake photo"></a>
<a href="pdf/OS.pdf" target="_blank"><img src="image/OS.jpg" alt="..." class="rounded photo wow tada"></a>
<a href="pdf/dccn.pdf" target="_blank "><img src="image/dccn.jpg" alt="..." class="rounded-top photo wow wobble"></a>
<a href="pdf/ITI.pdf" target="blank"><img src="image/iti.jpg" alt="..." class="rounded-right photo wow bounceIn"></a>
<a href="pdf/DATASTRUCTURE.pdf" target="blank"><img src="image/ds.jpg" alt="..." class="rounded-bottom photo wow bounceIndown"></a>
</div>
</div>
  
  
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
  
   </tr>
   </table>
  
</div>
</div>
  
  
  
     </div>
 </body>

</html>"""%id