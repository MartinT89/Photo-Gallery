import cgi
import cgi
import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='05260929Loumei',
                     db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()
title = form.getvalue('art_title')
link = form.getvalue('art_link')
location = form.getvalue('location')
art_type = form.getvalue('type')
artdes = form.getvalue('artdes')
year = form.getvalue('year')
gal_select = form.getvalue('gal_selection')
artist = form.getvalue('art_selection')
gallery_id = 0

if title is not None and link is not None and location is not None and art_type is not None and artdes is not None:
    cur.execute("""SELECT gallery_id FROM gallery.gallery WHERE name='%s'""" % gal_select)
    result = cur.fetchone()
    gallery_id = result[0]
    cur.execute("""SELECT artist_id FROM gallery.artist WHERE name='%s'""" % artist)
    result = cur.fetchone()
    artist_id = result[0]
    cur.execute("""SELECT MAX(detail_id) FROM detail""")
    result = cur.fetchone()
    detail_id = result[0]
    if detail_id is None:
        detail_id = 1
    else:
        detail_id = int(detail_id) + 1
    cur.execute("""INSERT INTO image(title,link,gallery_id,artist_id,detail_id) VALUES('%s','%s',%s,%s,%s)""" % (str(title), str(link), int(gallery_id), int(artist_id), int(detail_id)))
    db.commit()
    cur.execute("""SELECT MAX(image_id) FROM image""")
    result = cur.fetchone()
    image_id = result[0]
    cur.execute("""INSERT INTO gallery.detail(image_id,year,type,location,description) VALUES(%s,%s,'%s','%s','%s')""" % (int(image_id), int(year), str(art_type), str(location), str(artdes)))
    db.commit()

sql = "SELECT * FROM gallery.gallery"
cur.execute(sql)

print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
""")
print("""
<body>
    <div class='container'>
    <br><button onclick="location.href= 'p3.py'"class="btn btn btn-primary btn-sm">Main Page</button>
    <button onclick="location.href= 'modify.py'"class="btn btn btn-primary btn-sm">Modify/Delete</button><br><br>
    <h1>Upload New Image </h1>
    <form action="upload.py" method="POST">
        <input type="text" class='form-control' placeholder='Title'name="art_title">
        <input type="text" class='form-control' placeholder='Image Link'name="art_link">
        <input class='form-control' placeholder='Location' type="text" name="location">
        <input class='form-control' placeholder='Type' type="text" name="type">
        <input class='form-control' placeholder='Description' type="text" name="artdes">
        <input class='form-control' placeholder='Year' type="text" name="year">
        <select class='custom-select' name='gal_selection' placeholder="Select a Gallery">
        <option>Select a Gallery</option>
        """)
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select>""")
print("""<div class="input-group"><select class='custom-select' name='art_selection'>""")
sql = "SELECT * FROM gallery.artist"
cur.execute(sql)
print("""<option>Select an Artist</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[1])
print("""</select><button type="submit" class="btn btn btn-primary" type="button">Upload</button>
        </form>
    </div>
</body>""")
