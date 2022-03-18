"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app
from flask import render_template, request, redirect, url_for,flash, session, send_from_directory
from .form import PropertyForm
from .models import Property
from . import db
from werkzeug.utils import secure_filename

###
# Routing for your application.
###
MYDIR = os.path.dirname(__file__)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET','POST'])
def create():
    form = PropertyForm()
    if form.validate_on_submit():
        Title = form.Title.data
        NumOfBed = form.NumOfBed.data
        NumOfBath = form.NumOfBath.data
        Location = form.Location.data
        Price = form.Price.data
        Type = form.Type.data
        Description = form.Description.data
        Photo = form.Photo.data
        Photoname = secure_filename(Photo.filename)
        if len(Photoname) > 100:
            Photoname = Photoname[-100:]
        Photo.save(os.path.join(MYDIR + '/',app.config['UPLOAD_FOLDER'],Photoname))
        property = Property(Title,NumOfBed,NumOfBath,Location,Price,Type,Description,Photoname)
        db.session.add(property)
        db.session.commit()
        flash("Property Successfully Added")
        return redirect(url_for('properties'))
    return render_template('create.html', form=form)

@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties = properties)

@app.route('/properties/<propertyid>')
def property(propertyid):
    property = Property.query.get(propertyid)
    return render_template('property.html', property=property)


@app.route('/nice/<image>')
def get_image(image):
    return send_from_directory(os.path.join(MYDIR + '/',app.config['UPLOAD_FOLDER']),image)




###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
