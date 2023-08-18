import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for, flash

from models import app, db, User, Club, Event, Post, Comment, ClubMember, EventMember, PostMember, CommentMember

app = app

@app.route('/')

if __name__ == '__main__':
    app.run(debug=True)