from flask import Blueprint, render_template, request, redirect, url_for


profile_bp = Blueprint('profile_bp', __name__, url_prefix = '/siswa')