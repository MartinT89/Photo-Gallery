import cgi
import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='05260929Loumei',
                     db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()
galleryname = form.getvalue('gal_selection')
artist = form.getvalue('art_selection')
type_select = form.getvalue('type_select')
year_one = form.getvalue('year_one')
year_two = form.getvalue('year_two')
location_select = form.getvalue('location_select')
art_location = form.getvalue('art_location')
art_birthyear = form.getvalue('art_birthyear')

if galleryname is not None:
    gal_title = str(galleryname) + " Gallery"

if artist is not None:
    gal_title = str(artist) + " Gallery"

if type_select is not None:
    gal_title = str(type_select) + " Gallery"

if year_one and year_two is not None:
    gal_title = str(year_one) + " - " + str(year_two) + " Gallery"

if location_select is not None:
    gal_title = str(location_select) + " Gallery"

if art_location is not None:
    gal_title = "Artists From " + str(art_location)

if art_birthyear is not None:
    gal_title = "Artists Born " + str(art_birthyear)

print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
""")

print("""
        <div class="container"><h1>%s</h1>
        <button onclick="location.href = 'p3.py'" class="btn btn btn-primary btn-sm">Choose New Gallery</button>
        <button onclick="location.href= 'upload.py'"class="btn btn btn-primary btn-sm">Upload Image</button>
        <button onclick="location.href= 'modify.py'"class="btn btn btn-primary btn-sm">Modify/Delete</button>
        </div><br><br><br><br>
        
        <body> """ % gal_title)


if galleryname is not None:
    cur.execute("""SELECT gallery_id FROM gallery.gallery WHERE name='%s'""" % galleryname)
    result = cur.fetchone()
    gal_id = result[0]
    cur.execute("""SELECT * FROM image WHERE gallery_id=%s """ % int(gal_id))
    result = cur.fetchall()
    for row in result:
        print("""<form action="image_dis.py" id='%s'  method='POST'>
        <input class='form-control' type="text" name="img_value" hidden='true' value='%s'>""" % (row[1], row[1]))
        print("""</form>""")
        print("""<figure><img src='%s' onclick="document.getElementById('%s').submit();">
                            <figcaption>%s</figcaption></figure>
                                  """ % (row[2], row[1], row[1]))

if artist is not None:
    cur.execute("""SELECT artist_id FROM artist WHERE name='%s'""" % artist)
    result = cur.fetchone()
    art_id = result[0]
    cur.execute("""SELECT * FROM image WHERE artist_id=%s """ % int(art_id))
    result = cur.fetchall()
    for row in result:
        print("""<form action="image_dis.py" id='%s'  method='POST'>
        <input class='form-control' type="text" name="img_value" hidden='true' value='%s'>""" % (row[1], row[1]))
        print("""</form>""")
        print("""<figure><img src='%s' onclick="document.getElementById('%s').submit();">
                            <figcaption>%s</figcaption></figure>
                                  """ % (row[2], row[1], row[1]))

if type_select is not None:
    cur.execute("""SELECT image_id FROM detail WHERE type='%s'""" % type_select)
    result = cur.fetchall()
    for row in result:
        cur.execute("""SELECT * FROM image WHERE image_id=%s""" % row[0])
        image = cur.fetchone()
        print("""<form action="image_dis.py" id='%s'  method='POST'>
                <input class='form-control' type="text" name="img_value" hidden='true' value='%s'>""" % (
        image[1], image[1]))
        print("""</form>""")
        print("""<figure><img src='%s' onclick="document.getElementById('%s').submit();">
                                    <figcaption>%s</figcaption></figure>
                                          """ % (image[2], image[1], image[1]))

if year_one and year_two is not None:
    cur.execute("""SELECT image_id FROM detail WHERE year >= %s AND year <= %s""" % (int(year_one), int(year_two)))
    result = cur.fetchall()
    for row in result:
        cur.execute("""SELECT * FROM image WHERE image_id=%s""" % row[0])
        image = cur.fetchone()
        print("""<form action="image_dis.py" id='%s'  method='POST'>
                        <input class='form-control' type="text" name="img_value" hidden='true' value='%s'>""" % (
            image[1], image[1]))
        print("""</form>""")
        print("""<figure><img src='%s' onclick="document.getElementById('%s').submit();">
                                            <figcaption>%s</figcaption></figure>
                                                  """ % (image[2], image[1], image[1]))

if location_select is not None:
    cur.execute("""SELECT image_id FROM detail WHERE location='%s'""" % location_select)
    result = cur.fetchall()
    for row in result:
        cur.execute("""SELECT * FROM image WHERE image_id=%s""" % row[0])
        image = cur.fetchone()
        print("""<form action="image_dis.py" id='%s'  method='POST'>
                        <input class='form-control' type="text" name="img_value" hidden='true' value='%s'>""" % (
            image[1], image[1]))
        print("""</form>""")
        print("""<figure><img src='%s' onclick="document.getElementById('%s').submit();">
                                            <figcaption>%s</figcaption></figure>
                                                  """ % (image[2], image[1], image[1]))

if art_location is not None:
    cur.execute("""SELECT * FROM artist WHERE country='%s'""" % art_location)
    result = cur.fetchall()
    for row in result:
        print("""<h2>%s<br></h2><h3>%s</h3><h4>Birth Year:%s <br>Country:%s</h4><br>  """ % (row[1], row[4], row[2], row[3]))

if art_birthyear is not None:
    cur.execute("""SELECT * FROM artist WHERE birth_year=%s""" % art_birthyear)
    result = cur.fetchall()
    for row in result:
        print("""<h2>%s<br></h2><h3>%s</h3><h4>Birth Year:%s <br>Country:%s</h4><br>  """ % (row[1], row[4], row[2], row[3]))

print("""</body>""")

print("""<style>
        .container button{
            display: inline;
            float: right;
            position: relative;
        }
        
        .container{
            width: 100%
        }

	        
	    h1 {
            text-align: center;	    
	    }

figure{
    width: 30%;
    height: 40%;
    margin:1.66%;
    float: left;
}

img {
    width: 100%;
    height: 100%;
    float: left;
}

figcaption {
    background-color: #222;
    color: #fff;
    font: italic sans-serif;
    width: 100%;
    padding: 5px;
    text-align: center;
}

.btn-group-sm>.btn, .btn-sm {
    margin-left: 1%
}
         </style>
         
""")