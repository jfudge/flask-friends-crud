
from flask import Flask, render_template, request, redirect

from models import Friend
from forms import FriendForm, EditFriendForm, DeleteFriendForm
from settings import site_title, mydb, mycursor

import os

friend_app = Flask(__name__)

SECRET_KEY = os.urandom(32)
friend_app.config['SECRET_KEY'] = SECRET_KEY

@friend_app.route("/add-friend")
def add():
 
    get = {
        "add": request.args.get("add")
    }

    form = FriendForm(csrf_enabled=True)

    return render_template(
        "add-friend.html.j2",
        site_title = site_title,
        page_title = site_title + " - Add Friend",
        get = get,
        form = form
    )

@friend_app.route("/create-friend", methods=('GET', 'POST'))
def create():
    
    form = FriendForm(request.form, csrf_enabled=True)

    if form.validate_on_submit():
    
        friend = Friend(form)
    
        query = "INSERT INTO `friends` (`name`, `image`, `invited`) VALUES (%s, %s, %s)"
        value = (friend.name, friend.image, friend.invited)
        mycursor.execute(query, value)
        mydb.commit()

        return redirect('/?add=success')
   
    else:
        return redirect('/add-friend2?add=error')

@friend_app.route("/")
def read():
    get = {
        "add": request.args.get("add"),
        "edit": request.args.get("edit"),
        "delete": request.args.get("delete")
    }

    query = "SELECT * FROM `friends`"
    mycursor.execute(query)

    friends = mycursor.fetchall()

    form = DeleteFriendForm(csrf_enabled=True)

    return render_template(
        "view-friends.html.j2",
        site_title = site_title,
        page_title = site_title + " - View Friends",
        get = get,
        friends = friends,
        form = form
    )

@friend_app.route("/edit-friend")
def edit():
    get = {
        "edit": request.args.get("edit"),
        "id": request.args.get("id")
    }

    query = f"SELECT * FROM `friends` WHERE id='{get['id']}'"
    mycursor.execute(query)

    friend = mycursor.fetchone()

    form = EditFriendForm(csrf_enabled=True)
    form.name.data = friend["name"]
    form.image.data = friend["image"]
    form.invited.data = friend["invited"]
    form.id.data = get["id"]

    return render_template(
        "edit-friend.html.j2",
        site_title = site_title,
        page_title = site_title + " - Edit " + friend["name"],
        friend = friend,
        get = get,
        form = form
    )

@friend_app.route("/update-friend", methods=('GET', 'POST'))
def update():
    
    form = EditFriendForm(csrf_enabled=True)
    
    id = form.id.data

    if form.validate_on_submit():
       
        friend = Friend(form)
       
        query = f"UPDATE `friends` SET name=%s, image=%s, invited=%s WHERE id='{id}'"
        value = (friend.name, friend.image, friend.invited)
        mycursor.execute(query, value)
        mydb.commit()

        return redirect('/?edit=success')
    else:
        return redirect('/edit-friend?edit=error')


@friend_app.route("/delete-friend", methods=('GET', 'POST'))
def delete():

   form = DeleteFriendForm(csrf_enabled=True)
   id = form.id.data

   if form.validate_on_submit():

        query = f"DELETE FROM `friends` WHERE id='{id}'"
        mycursor.execute(query)
        mydb.commit()

        return redirect('/?delete=success')
    