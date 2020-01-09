import cgi
import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='05260929Loumei',
                     db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()

# For Modifying artist
art_select = form.getvalue('art_select')
art_birth = form.getvalue('art_birth')
art_country = form.getvalue('art_country')
art_des = form.getvalue('art_des')

# For Modifying Gallery
gal_select = form.getvalue('gal_select')
gal_name = form.getvalue('gal_name')
gal_des = form.getvalue('gal_des')

#For Modifying Image
change_img = form.getvalue('change_img')
img_title = form.getvalue('img_title')
img_location = form.getvalue('img_location')
img_type = form.getvalue('img_type')
img_artdes = form.getvalue('img_artdes')
gal_selection = form.getvalue('gal_selection')
img_year = form.getvalue('img_year')
img_art = form.getvalue('img_art')
img_link = form.getvalue('img_link')


# For deleting images
del_img = form.getvalue('del_img')
if art_select is not None:
    cur.execute("""
                UPDATE artist 
                SET birth_year=%s, country='%s', description='%s'
                WHERE name='%s' """ % (int(art_birth), art_country, art_des, art_select ))
    db.commit()

if gal_select is not None:
    cur.execute("""
                UPDATE gallery.gallery 
                SET name='%s', description='%s'
                WHERE name='%s' """ % (gal_name,gal_des,gal_select))
    db.commit()

if del_img is not None:
    cur.execute("""SELECT * FROM image WHERE title='%s'""" % del_img)
    result = cur.fetchone()
    cur.execute("""DELETE FROM image WHERE title='%s'""" % del_img)
    cur.execute("""DELETE from detail where image_id=%s""" % int(result[0]))
    db.commit()

if change_img is not None:
    cur.execute("""SELECT artist_id FROM artist WHERE name='%s'""" % img_art)
    artist_id = cur.fetchone()

    cur.execute("""SELECT gallery_id FROM gallery.gallery where name='%s'""" % gal_selection)
    gallery_id = cur.fetchone()

    cur.execute("""SELECT image_id FROM image WHERE title='%s'""" % change_img)
    result = cur.fetchone()

    cur.execute("""
                    UPDATE detail 
                    SET year=%s, type='%s', location='%s', description='%s'
                    WHERE image_id=%s """ % (int(img_year), img_type, img_location, img_artdes,int(result[0])))

    cur.execute("""
                    UPDATE image 
                    SET title='%s', link='%s', gallery_id=%s, artist_id=%s
                    WHERE image_id=%s """ % (img_title, img_link, int(gallery_id[0]), int(artist_id[0]),int(result[0])))
    db.commit()


sql = "SELECT * FROM artist"
cur.execute(sql)

print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
""")
print("""
<body>
    <div class='container'>
    <br>
    <button onclick="location.href= 'p3.py'"class="btn btn btn-primary btn-sm">Main Page</button>
    <button onclick="location.href= 'upload.py'"class="btn btn btn-primary btn-sm">Upload Image</button><br><br>
    
    <h1>Modify Artist </h1>
    <form action="modify.py" method="POST">
    <select class='custom-select' name='art_select' placeholder="Select an Artist to Modify">
    <option>Select an Artist to Modify</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select>
        <input type="text" class='form-control' placeholder='Birth Year'name="art_birth">
        <input type="text" class='form-control' placeholder='Country'name="art_country">
        <input class='form-control' placeholder='Description' type="text" name="art_des">
        <button type="submit" class="btn btn btn-primary" type="button">Modify</button></form>""")

cur.execute("SELECT * from gallery.gallery")

print("""
  
    <h1>Modify Gallery</h1>
    <form action="modify.py" method="POST">
    <select class='custom-select' name='gal_select' placeholder="Select an Artist to Modify">
    <option>Select a Gallery to Modify</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select>
        <input type="text" class='form-control' placeholder='Gallery Name'name="gal_name">
        <input type="text" class='form-control' placeholder='Description'name="gal_des">
        <button type="submit" class="btn btn btn-primary" type="button">Modify</button></form></form>""")

cur.execute("Select * FROM image")


print("""
    <br><h1>Modify Image</h1>
    <form action="modify.py" method="POST"> 
    <select class='custom-select' name='change_img' placeholder="Select an Image">
    <option>Select an Image to Modify</option>""")
cur.execute("Select * FROM image")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select><input type="text" class='form-control' placeholder='Title'name="img_title">
        <input type="text" class='form-control' placeholder='Image Link'name="img_link">
        <input class='form-control' placeholder='Location' type="text" name="img_location">
        <input class='form-control' placeholder='Type' type="text" name="img_type">
        <input class='form-control' placeholder='Description' type="text" name="img_artdes">
        <input class='form-control' placeholder='Year' type="text" name="img_year">
        <select class='custom-select' name='gal_selection' placeholder="Select a Gallery">
        <option>Select a Gallery</option>
        """)

cur.execute("""SELECT * FROM gallery.gallery""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select>""")
print("""<div class="input-group"><select class='custom-select' name='img_art'>""")

sql = "SELECT * FROM gallery.artist"
cur.execute(sql)

print("""<option>Select an Artist</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select><button type="submit" class="btn btn btn-primary" type="button">Modify</button>
        </form>
""")

print("""
    </div>
    <br><h1>Delete an Image</h1>
    <form>
    <select class='custom-select' name='del_img' placeholder="Select a Gallery">
    <option>Select an Image to Delete</option>""")

cur.execute("Select * FROM image")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select><button type="submit" class="btn btn btn-primary" type="button">Delete</button></form>""")

print("""
</body>""")