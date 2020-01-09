import cgi
import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='05260929Loumei',
                     db= 'gallery')
cur = db.cursor()
form = cgi.FieldStorage()
img_value = form.getvalue('img_value')

cur.execute("""SELECT * FROM image WHERE title='%s'""" % img_value)
result = cur.fetchone()

cur.execute("""SELECT * FROM image WHERE image_id=%s""" % int(result[0]))
image = cur.fetchone()
cur.execute("""SELECT * FROM detail WHERE image_id=%s""" % int(result[0]))
detail = cur.fetchone()
cur.execute("""SELECT name from artist where artist_id=%s""" % int(result[4]))
artist = cur.fetchone()

print("Content-Type: text/html")
print()
print("""<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <div class="container"><h1>%s</h2>
        <button onclick="location.href = 'p3.py'" class="btn btn btn-primary btn-sm">Choose New Gallery</button>
        <button onclick="location.href= 'upload.py'"class="btn btn btn-primary btn-sm">Upload Image</button>
        <button onclick="location.href= 'modify.py'"class="btn btn btn-primary btn-sm">Modify/Delete</button>
        </div><br><br><br><br>
""" % img_value)

print("""<body>""")
print("""<div class="container">
          <div class='row'>""")

print("""<div class="col">""")
print("""<h3>Artist: %s</h3>""" % artist[0])
print("""<h3>Year: %s</h3>""" % detail[2])
print("""<h3>Type: %s</h3>""" % detail[3])
print("""<h3>Location: %s</h3>""" % detail[6])
print("""<h3>Description: %s</h3>""" % detail[7])
print("</div>")
print("""<div class="col">""")
print("""<img src='%s'>""" % image[2])
print("</div>")

print("""</div></div>""")
print("""</body>""")
print("""<style>""")
print("""
    .row{
        height: 100%;
    }
    img {
        width:100%;
        height:50%;
        margin:1.66%;
        float: right;
    }
""")
print("""</style>""")