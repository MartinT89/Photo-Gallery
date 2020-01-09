import cgi

form= cgi.FieldStorage()
title = form.getvalue('Title')
artist = form.getvalue('Artist')
des = form.getvalue('Description')
image = form.getvalue('Image')
year = form.getvalue('Year')

title2 = form.getvalue('Title2')
artist2 = form.getvalue('Artist2')
des2 = form.getvalue('Description2')
image2 = form.getvalue('Image2')
year2 = form.getvalue('Year2')
print("Content-Type: text/html")
print()
print("""<body>
            <button onclick="first()">First Image</button> <button onclick="second()">Second Image</button><br>
            <div><h3 id="main_title">Title: %s </h3><h3 id="main_art">Artist: %s </h3><h3 id=main_year>Year: %s</h3><h3 id=main_des>Description: %s </h3></div>
                <img src="%s" id="main_img">

          </body>""" % (title,artist,year,des,image))
          
          
print("""<script>
            function first(){
                document.getElementById("main_title").innerHTML = "Title: %s"
                document.getElementById("main_art").innerHTML = "Artist: %s"
                document.getElementById("main_year").innerHTML = "Year: %s"
                document.getElementById("main_des").innerHTML = "Description: %s"
                document.getElementById("main_img").src = "%s"              
            }
            
            function second(){
                document.getElementById("main_title").innerHTML = "Title: %s"
                document.getElementById("main_art").innerHTML = "Artist: %s"
                document.getElementById("main_year").innerHTML = "Year: %s"
                document.getElementById("main_des").innerHTML = "Description: %s"
                document.getElementById("main_img").src = "%s"              
            }
         
         </script>""" % (title,artist,year,des,image,title2,artist2,year2,des2,image2))

