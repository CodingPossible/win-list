from flask import Flask, render_template 

def apology(message, code=400):
    return render_template("apology.html", message=message), code