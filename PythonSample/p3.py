import cgi
import pymysql
import datetime
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='05260929Loumei',
                     db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()
gallery = form.getvalue('galleryname')
description = form.getvalue('description')
artname = form.getvalue('artname')
birth = form.getvalue('birth')
country = form.getvalue('country')
artdes = form.getvalue('artdes')

if gallery is not None and description is not None:
    cur.execute("""INSERT INTO gallery.gallery(name,description) VALUES('%s','%s')""" % (gallery, description))
    db.commit()
if artname is not None:
    cur.execute("""INSERT INTO artist(name,birth_year,country,description) VALUES('%s',%s,'%s','%s')"""
                % (artname, int(birth), country, artdes))
    db.commit()
sql = "SELECT * FROM gallery.gallery"
cur.execute(sql)



print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
""")
print("""<body>""")
print("""<h1>Good Morning!</h1>""" )
print("""<button onclick="location.href= 'upload.py'"class="btn btn btn-primary btn-lg">Upload Image</button>
         <button onclick="location.href= 'modify.py'"class="btn btn btn-primary btn-lg">Modify/Delete</button><br><br>""")
print("""<div class="container">
          <div class='row'>""")

print("""<div class="col" id='gal_select'><form action="gallery.py" method='POST'>""")
print("<h1>Select a Gallery</h1>")
print("""<div class="input-group"><select class='custom-select' name='gal_selection'><option>Select a Gallery</option>""")
for result in cur.fetchall():
    print("""<option value='%s'>%s (%s)</option>""" % (result[1], result[1], result[2]))
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>""")
print("""</form></div></div>""")


print("<h1>Images By Artist</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group"><select class='custom-select' name='art_selection'><option>Select an Artist</option>""")
sql = "SELECT * FROM gallery.artist"
cur.execute(sql)
for result in cur.fetchall():
    print("""<option value='%s'>%s (%s)</option>""" % (result[1], result[1], result[4]))
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>""")
print("""</form></div></div>""")


cur.execute("""SELECT DISTINCT(type) FROM detail""")

print("<h1>Images By Type</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group"><select class='custom-select' name='type_select'><option>Select by Type</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[0])
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>
        </form></div></div>""")


print("<h1>Images By Year</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group">
        <input class='form-control' placeholder='Year One' type="text" name="year_one">
        <input class='form-control' placeholder='Year Two' type="text" name="year_two">
        <div class="input-group-append"><button type="submit" class="btn btn btn-primary" type="button">Choose</button>
        </form></div></div>""")

cur.execute("""SELECT DISTINCT(location) FROM detail""")

print("<h1>Images By Location</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group"><select class='custom-select' name='location_select'><option>Select by Location</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[0])
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>
        </form></div></div>""")

print("""</div>""")

print("""<div class="col" id='gal_upload'><span id='gal'>
        <h1>Create a Gallery</h1><form action="p3.py" method="POST">
        <input type="text" class='form-control' placeholder='Gallery Name'name="galleryname">
        <input class='form-control' placeholder='Gallery Description' type="text" name="description"><br></span>
        <button type="submit" class='btn btn-primary id='hello''>Submit</button><br>
        </form>
        
        <h1>Create an Artist</h1><form action="p3.py" method="POST">
        <input type="text" class='form-control' placeholder='Artist Name'name="artname">
        <input class='form-control' placeholder='Birth year' type="text" name="birth">
        <input class='form-control' placeholder='Country' type="text" name="country">
        <input class='form-control' placeholder='Description' type="text" name="artdes"><br>
        <button type="submit" class='btn btn-primary id='hello''>Submit</button>
        </form><br>""")

cur.execute("""SELECT DISTINCT(country) FROM artist""")

print("<h1>Artist by Country</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group"><select class='custom-select' name='art_location'><option>Select by Country</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[0])
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>
        </form></div></div>""")

cur.execute("""SELECT DISTINCT(birth_year) FROM artist""")

print("<h1>Artist by Birth Year</h1>")
print("""<form action="gallery.py" method='POST'><div class="input-group"><select class='custom-select' name='art_birthyear'><option>Select by Birth Year</option>""")
for result in cur.fetchall():
    print("""<option>%s</option>""" % result[0])
print("""</select>
        <div class="input-group-append">
        <button type="submit" class="btn btn btn-primary" type="button">Choose</button>
        </form></div></div>""")

print("""</div>""")
print("""</div>""")

print("""</body>""")

print("""<style>
    #gal{
        text-align: center;
    }
    .container{
        width: 50%;
    }
    body{
        width: 100%;
        position: absolute;
        background-size: cover;
        background-image: url("https://images.unsplash.com/photo-1531579766052-06ad0bb58728?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1166&q=80");
    }
    #gal_select{
        width: 50%;
        text-align: center;
        color: white;
        padding-top: 15.5%;
        padding-bottom: 100%;
        overflow-x: hidden;
        overflow-y: auto;
    }
    
    #gal_upload{
        width: 50%;
        color: white;
        padding-top: 10.5%;
        padding-bottom: 100%;
        overflow-x: hidden;
        overflow-y: auto;
    }
    
    #gal_upload button {
        border: none;
        color: black;
        background-color: white;
        float: right;
    }
    .btn-group-lg>.btn, .btn-lg {
        margin-right: 1%;
        margin-top: 1%;
        float: right;
    }
    
</style>""")